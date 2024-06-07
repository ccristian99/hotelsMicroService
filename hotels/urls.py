from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hotels/register', views.register_hotels, name='register_hotels'),
    path('api/hotels/', views.list_hotels, name='list_hotels'),
    path('api/hotels/city/<str:city>/', views.list_hotels_city, name='list_hotels_citys'),
    path('api/hotels/url/<int:id>/', views.list_hotels_id_url, name='list_hotels_id_url'),
    path('api/hotels/<int:id>/', views.hotel_by_id, name='hotel_by_id'),
    path('api/hotels/<str:hotelname>/', views.hotel_by_name, name='hotel_by_name'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)