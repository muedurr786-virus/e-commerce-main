from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('register/',registerPage,name='register'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('admin_profile/',adminProfilePage,name='admin_profile'),
    path('customer_profile/',customerProfilePage,name='customer_profile'),
    
    
    path('add_category/',categoryAddpage,name='add_category'),
    path('add_product/',productAddPage,name='add_product'),
    path('view_product/<int:id>/',viewProductPage,name='view_product'),
    path('product_order/<int:id>/',productOrderPage,name='product_order'),
    path('review/<int:id>/',reviewPage,name='review'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
