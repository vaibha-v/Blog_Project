from django.urls import re_path, include
from blog import views

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^about/', views.AboutView.as_view(), name='about'),
    re_path(r'post/(?P<pk>\d+)$',
            views.PostDetailView.as_view(), name='post_details'),
    re_path(r'^post/new', views.PostCreateView.as_view(), name='post_create'),
    re_path(r'post/(?P<pk>\d+)/update',
            views.PostUpdateView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete',
            views.PostDeleteView.as_view(), name='post_delete'),
    re_path(r'^draft/$', views.PostDraftView.as_view(), name='post_draft'),
    re_path(r'^post/(?P<pk>\d+)/comment/', views.approve_comment_to_post,
            name='approve_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/',
            views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/',
            views.revove_comment, name='revove_comment'),
    re_path(r'^comment/(?P<pk>\d+)/publish/',
            views.post_publish, name='post_publish'),
]
