from django.conf.urls import url
from django.urls import path

import patterns as patterns
from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from quickstart.views import UserList, UserDetail
# from quickstart.views import UserList, GroupList

urlpatterns = [
    # path(r'^$', 'api_root'),
    path('users/', UserList.as_view({'get': 'list'}), name='user-list'),
    path('users/<pk>/', UserDetail.as_view({'get': 'retrieve'}), name='user-detail'),

    # path('groups', GroupList.as_view(), name='group-list'),
    # path('groups/<pk>/', GroupDetail.as_view({'get': 'retrieve'}), name='group-detail'),
]

# Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
# urlpatterns += patterns('',
#                         url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#                         )
