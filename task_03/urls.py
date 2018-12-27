from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/detail/', views.restaurant_detail, name='restaurant-detail'),
    path('restaurants/detail/<int:rest_id>',
         views.restaurant_detail, name='restaurant-detail'),
    path('restaurants/', views.RestaurantList.as_view(), name="restaurant-list")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
