"""
URL configuration for ekart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # path('features/', views.features),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('filterbyprice/', views.filterbyprice),

    # path('home/', views.home),
    path('logout/', views.user_logout, name="logout"),
    
    # path("login/", views.login),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("viewcart/", views.viewcart),
    # path("order/", views.order),
    path("", views.allproducts, name="allproducts"),
    path("catfilter/<cf>/", views.catfilter),
    # path("product/", views.product),
    path("sortbyprice/<sv>/", views.sortbyprice),
    path("search/", views.search, name= "search"),
    path('product_details/<pid>/', views.product_details, name='product_details'),
    path("addcart/<pid>/", views.cart),
    path("updateqty/<x>/<cid>/", views.updateqty),
    path("removecart/<cid>/",views.removecart)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  