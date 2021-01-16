from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import PublicWish, PrivateWish, AccessModel
from rest_framework import status
from .serializers import PrivateWishSerializer, PublicWishSerializer, AccessModelSerializer
from django.http import JsonResponse
import requests

# Create your views here.
@api_view(['POST'])
def access_uuid_generator(request):
    if request.method == "POST":
        access_level_data = JSONParser().parse(request)
        access_level_serializer = AccessModelSerializer(data=access_level_data)

        if access_level_serializer.is_valid():
            access_level_serializer.save()
            print("Access uuid level" + str(JsonResponse(access_level_serializer.data)))
            return JsonResponse(access_level_serializer.data, status=status.HTTP_201_CREATED)

        print("Bad request with Access uuid" + str(JsonResponse(access_level_serializer.data)))
        return JsonResponse(access_level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])  # private
def private_wish_view(request, pk):
    #Check if access model contains access level of string private

    access_uuid_header = request.headers['UUID']
    access_data = AccessModel.objects.get(access_uuid=access_uuid_header)


    if str(access_data.access_level) == "private":

        if request.method == "POST":
            wish_list_data = JSONParser().parse(request)
            private_wish_serializer = PrivateWishSerializer(data=wish_list_data)
            public_wish_serializer = PublicWishSerializer(data=wish_list_data)
            if public_wish_serializer.is_valid():
                public_wish_serializer.save()
                print("Able to create Public wish list mirror")
            if private_wish_serializer.is_valid():
                private_wish_serializer.save()
                print("Able to create private wish List mirror" + str(JsonResponse(private_wish_serializer.data)))
                return JsonResponse(private_wish_serializer.data, status=status.HTTP_201_CREATED)

            print("Bad request with wish List" + str(JsonResponse(private_wish_serializer.data)))
            return JsonResponse(private_wish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            private_wish = PrivateWish.objects.get(pk=pk)

        except PrivateWish.DoesNotExist:
            return JsonResponse({'message': 'The wish does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            private_wish_serializer = PrivateWishSerializer(private_wish)
            return JsonResponse(private_wish_serializer.data)

        elif request.method == 'DELETE':
            count = private_wish.delete()
            print("Successfully deleted wish...")
            return JsonResponse({'message': 'Wish was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            wish_list_data = JSONParser().parse(request)
            wish_serializer = PrivateWishSerializer(private_wish, data=wish_list_data)
            if wish_serializer.is_valid():
                wish_serializer.save()
                print("Able to Update wish list" + str(JsonResponse(wish_serializer.data)))
                return JsonResponse(wish_serializer.data)
            print("Bad request with wish List" + str(JsonResponse(wish_serializer.data)))
            return JsonResponse(wish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def public_wish_view(request, pk):
    # Check if access model contains access Level of string public.

    access_uuid_header = request.headers['UUID']
    access_data = AccessModel.objects.get(access_uuid=access_uuid_header)

    if str(access_data.access_level) == "public":

        try:
            public_wish = PublicWish.objects.get(pk=pk)

        except PublicWish.DoesNotExist:
            return JsonResponse({'message': 'The wish does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            # all_wishes = PublicWish.objects.all()
            public_wish_serializer = PublicWishSerializer(public_wish)
            return JsonResponse({'wish_details': public_wish_serializer.data}, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            wish_list_data = JSONParser().parse(request)
            wish_serializer = PublicWishSerializer(public_wish, data=wish_list_data)
            if wish_serializer.is_valid():
                wish_serializer.save()
                print("Public user able to Update wish list" + str(JsonResponse(wish_serializer.data)))
                return JsonResponse(wish_serializer.data)
            print("Bad request with wish List" + str(JsonResponse(wish_serializer.data)))
            return JsonResponse(wish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)