from django.contrib import admin
from django.urls import path
from rating import views


urlpatterns = [
    path('', views.add_rating, name='rating'),
    path('admin/', admin.site.urls),
]
