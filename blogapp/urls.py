from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.UpdatePost.as_view(), name='post_update'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='new_post'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDelete.as_view(), name='delete_post'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^draft/$', views.DraftView.as_view(), name='draft_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.create_comment, name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.delete_comment, name='delete_comment'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

]