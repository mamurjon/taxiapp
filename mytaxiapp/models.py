from _decimal import Decimal
from django.utils import timezone
from django.db import models
from django.contrib.gis.db import models as models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from utils.filename import RandomFileName


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, db_index=True)

    @classmethod
    def filter_active(cls):
        return cls.objects.filter(is_active=True, )

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        now = timezone.now()
        user = self.model(phone_number=phone_number, last_login=now, **extra_fields)
        user.set_password(password)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def update_rating_for(self, user):
        reviews = list(user.reviews.all())
        total_rating = 0
        for review in reviews:
            total_rating += review.rating
        user.rating = total_rating / len(reviews)
        user.save()

    def update_rating_for_all(self):
        users = self.all().filter(is_active=True)
        for user in users:
            self.update_rating_for(user)


class User(PermissionsMixin, AbstractBaseUser, BaseModel):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    phone_number = models.CharField(max_length=64, unique=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    year_of_birth = models.IntegerField(blank=True, null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        :return: string
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        :return: string
        """
        return self.first_name


class Car(BaseModel):
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=63, blank=True, null=True)
    car_photo = models.ImageField(upload_to=RandomFileName('cars'), blank=True, null=True)
    brand = models.CharField(max_length=300, blank=True, null=True, verbose_name="Car Firm")
    model = models.CharField(max_length=300, blank=True, null=True)
    seats = models.SmallIntegerField(default=4, blank=True, )
    color = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.brand, self.model)


class Driver(User):
    car = models.ForeignKey(to=Car, related_name='driver', on_delete=models.CASCADE)
    gender = models.CharField(blank=True, null=True, max_length=20)
    biography = models.TextField(blank=True, null=True)
    experience = models.CharField(blank=True, null=True, max_length=256)
    driver_photo = models.ImageField(upload_to=RandomFileName('users'), blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=Decimal('0.0'))

    def __str__(self):
        return self.phone_number


class Offer(BaseModel):
    user = models.ForeignKey(User, related_name='offer_user', null=True, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='offer_driver', null=True, on_delete=models.CASCADE)
    start_place = models.CharField(max_length=127)
    finish_place = models.CharField(max_length=127)
    pickup_date = models.DateField(blank=True, null=True, unique=False)
    pickup_time = models.TimeField(blank=True, null=True, unique=False)
    offer_price = models.CharField(max_length=63, null=True, blank=True)
    location_from = models.PointField(geography=True, srid=4326, null=True, blank=True)
    location_to = models.PointField(geography=True, srid=4326, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    NEW = 'new'
    ACCEPTED = 'accepted_by_driver'
    DRIVER_CAME = 'driver_came'
    CUSTOMER_IN_THE_CAR = 'customer_in_the_car'
    OFFER_COMPLETED = 'completed'

    STATUS_GROUP = (
        (NEW, _('new')),
        (ACCEPTED, _('accepted_by_driver')),
        (DRIVER_CAME, _('driver_came')),
        (CUSTOMER_IN_THE_CAR, _('customer_in_the_car')),
        (OFFER_COMPLETED, _('completed'))
    )
    status = models.CharField(max_length=127, choices=STATUS_GROUP, default=NEW)

    @classmethod
    def filter_active(cls):
        """
        Filter Rides such that only active and pickup_date is less than or equal to current date
        :return: Queryset
        """
        return cls.objects.filter(models.Q(is_active=True))

