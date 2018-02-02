from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import permissions

from mytaxiapp.models import (User, Driver, Car, Offer)
from .serializers import (UserSerializer, DriverSerialiser, CarSerializer, OfferSerializer, OfferDetailSerializer)


class UserProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # lookup_field = 'pk'

    # def get_object(self):
    #     return User.filter_active().get(phone_number=self.request.user)


class DriverProfileView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerialiser


class OfferListView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = OfferSerializer


class RideListView(generics.ListCreateAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self, *args, **kwargs):
        return self.request.user.offer_user.select_related().all().filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RideDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OfferDetailSerializer
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(Offer, id=self.kwargs[self.lookup_field], user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save(user=self.request.user)
        instance.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = OfferDetailSerializer
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(Offer, id=self.kwargs[self.lookup_field], user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save(user=self.request.user)
        instance.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
