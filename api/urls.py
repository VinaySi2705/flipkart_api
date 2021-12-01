from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (CategoryView,
                    RegisterView,
                    ChangePasswordView,
                    ProductView)



router = DefaultRouter()
router.register('category',CategoryView)
router.register('product',ProductView)
urlpatterns = [
   path('',include(router.urls)),
   path('accounts/',include('rest_framework.urls')),
   path('register/',RegisterView.as_view()),
   path('change_password/', ChangePasswordView.as_view()),
   path('password_reset/', include('django_rest_passwordreset.urls'), name='password_reset'),
]
