from django.urls import path

from . import views

app_name = "portal"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("schedule/", views.schedule, name="schedule"),
    path("schedule/<slug:class_slug>/", views.schedule, name="schedule_class"),
    path("news/", views.news_list, name="news"),
]
