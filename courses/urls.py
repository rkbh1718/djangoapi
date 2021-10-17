from django.urls import path,include
from django.contrib import admin
from. import views
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('courses', views.CourseView)

admin.site.site_header = "Rajneesh APi work "
admin.site.site_title = "Rajneesh Api Wala"
admin.site.index_title = "Welcome to Rajneesh Api"

urlpatterns = [
   path('', include(router.urls)),

]
