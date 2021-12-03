from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (CategoryView,
                    RegisterView,
                    ChangePasswordView,
                    ProductView,
                    CartView)



router = DefaultRouter()
router.register('category',CategoryView)
router.register('product',ProductView)
router.register('cart',CartView)
urlpatterns = [
   path('',include(router.urls)),
   path('accounts/',include('rest_framework.urls')),
   path('register/',RegisterView.as_view()),
   path('change_password/', ChangePasswordView.as_view()),
   #please install django_rest_passwordreset
   path('password_reset/', include('django_rest_passwordreset.urls'), name='password_reset'),
]
