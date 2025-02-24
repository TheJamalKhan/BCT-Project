"""
URL configuration for mobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
"""
URL configuration for mobile project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from store import views 

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# # ]

# from django.urls import path
# # from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/', views.home, name='home'),
#     path('cart/', views.cart_view, name='cart'),  # Fixed this line
#     path('add_to_cart/<int:mobile_id>/', views.add_to_cart, name='add_to_cart'),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from store import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/', views.home, name='home'),
#     path('cart/', views.cart_view, name='cart'),
#     path('add_to_cart/<int:mobile_id>/', views.add_to_cart, name='add_to_cart'),
# ]
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:mobile_id>/', views.add_to_cart, name='add_to_cart'),
]

