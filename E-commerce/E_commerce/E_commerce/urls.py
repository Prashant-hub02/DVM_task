
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.urls import include



urlpatterns = [

    # Errors Page
    path('404',views.Error404,name='404'),
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    path('',views.HOME,name='home'),
    path('product/<slug:slug>',views.PRODUCT_DETAILS,name='product_detail'),

    # account urls
    path('account/my-account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.REGISTER,name='handleregister'),
    path('account/login',views.LOGIN,name='handlelogin'),


    path('accounts/', include('django.contrib.auth.urls')),
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)