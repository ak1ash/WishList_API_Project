from rest_framework import serializers
from .models import PrivateWish, PublicWish, AccessModel


class PrivateWishSerializer(serializers.ModelSerializer):
    class Meta():
        model = PrivateWish
        fields = (
            'wish_id',
            'wish',
            'amount_wished',
            'destination_uri',
            'image_uri'
        )


class PublicWishSerializer(serializers.ModelSerializer):

    class Meta():
        model = PublicWish
        fields = (
            'wish_id',
            'wish',
            'amount_wished',
            'amount_granted'
        )

class AccessModelSerializer(serializers.ModelSerializer):

    class Meta():
        model = AccessModel
        fields = (
            'access_uuid',
            'access_level'
        )