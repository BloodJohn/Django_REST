from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework import viewsets

# @api_view(['GET'])
# def api_root(request, format=None):
#     """
#     The entry endpoint of our API.
#     """
#     return Response({
#         'users': reverse('user-list', request=request),
#         'groups': reverse('group-list', request=request),
#     })


class UserList(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of users.
    """
    # model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(viewsets.ModelViewSet):
    """
    API endpoint that represents a single user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class GroupList(generics.ListCreateAPIView):
#     """
#     API endpoint that represents a list of groups.
#     """
#     model = Group
#     serializer_class = GroupSerializer
#
#
# class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API endpoint that represents a single group.
#     """
#     model = Group
#     serializer_class = GroupSerializer
