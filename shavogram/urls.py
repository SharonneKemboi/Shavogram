from . import views
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r"^ajax/like/$",views.like, name = 'like'),
    re_path(r"^ajax/comment/$",views.comment, name = "comment"),
    re_path(r"^ajax/follow/$", views.follow, name = "follow"),
    re_path(r"^ajax/follow/profile/$", views.follow_in_profile, name = "follow_in_profile"),
    re_path(r"^add/picture$", views.add_picture, name = "add_picture"),
    re_path(r"^profile/(\d+)/$", views.profile, name = "profile" ),
    re_path(r"^profile/update/$", views.update_profile, name = "update_profile"),
    re_path(r"search/$", views.search_user, name = "search"),
    re_path(r"^feed/$", views.feed, name = "feed"),
    re_path(r"^accounts/profile/$", views.my_profile, name = "my_profile")


    
      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

