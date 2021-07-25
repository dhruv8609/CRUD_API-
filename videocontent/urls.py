from django.urls import path, include
from videocontent.views import (
    get_video,
    update_video,
    delete_video,
    create_video,
    get_all_video,
    get_video_views
)
from . import views
from rest_framework import routers

app_name = "videocontent"


# router = routers.DefaultRouter()
# router.register('video/', views.VideoView)
urlpatterns = [
    path('all/', get_all_video, name="videolist"),
    path('views/<slug>', get_video_views, name="views_all"),
    path('<slug>', get_video, name="detail"),
    path('update/<slug>', update_video, name="update"),
    path('delete/<slug>', delete_video, name="delete"),
    path('create/', create_video, name="create")
    # path('', include(router.urls))

]
