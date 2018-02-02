from mytaxiapp.models import User, Driver, Car, Offer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'year_of_birth',
            'email',
            'date_joined',
        )


class DriverSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'year_of_birth',
            'email',
            'date_joined',
            'car',
            'gender',
            'biography',
            'experience',
            'driver_photo',
            'rating',
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'id',
            'car_number',
            'car_photo',
            'brand',
            'model',
            'seats',
            'color',
        )


class OfferSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Offer.STATUS_GROUP)

    class Meta:
        model = Offer
        fields = (
            'id',
            'user',
            'start_place',
            'finish_place',
            'pickup_date',
            'pickup_time',
            'offer_price',
            'location_from',
            'location_to',
            'created',
            'status',
        )


class OfferDetailSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Offer.STATUS_GROUP)
    driver_phone_number = serializers.CharField(max_length=31, allow_null=True, allow_blank=True)
    driver_car_number = serializers.CharField(max_length=31, allow_null=True, allow_blank=True)
    start_place = serializers.ReadOnlyField()
    finish_place = serializers.ReadOnlyField()
    pickup_date = serializers.ReadOnlyField()
    pickup_time = serializers.ReadOnlyField()
    offer_price = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = Offer
        fields = (
            'id',
            'user',
            'driver',
            'driver_phone_number',
            'driver_car_number',
            'start_place',
            'finish_place',
            'pickup_date',
            'pickup_time',
            'offer_price',
            'created',
            'status',
        )
