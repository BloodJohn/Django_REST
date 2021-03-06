from django.urls import path

from blog.apiViews import BlogList
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('blogapi/', BlogList.as_view({'get': 'list'}), name='blog-list'),
    path('blogapi/<int:post_id>/', BlogList.as_view({'get': 'record'}), name='blog-detail'),

    path('blogapi/', BlogList.as_view({'post': 'create'}), name='blog-create'),
    path('blogapi/<int:post_id>/', BlogList.as_view({'put': 'update'}), name='blog-update'),
    path('blogapi/<int:post_id>/', BlogList.as_view({'delete': 'delete'}), name='blog-delete'),
]