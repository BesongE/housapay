from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserLoginAPIView, UserRegisterAPIView, UserLogoutAPIView, Goods, getRoutes


urlpatterns = [
    path("login/", UserLoginAPIView.as_view(), name="user_login"),
    path("register/", UserRegisterAPIView().as_view(), name="user_register"),
    path('obtain_token/', obtain_auth_token, name='api_token_auth'),
    path("logout/", UserLogoutAPIView.as_view(), name="user_logout"),
    path('get_routes/', getRoutes, name="get_routes"),
    #Non Auth urls
    
    path('goods/',Goods.as_view(), name='goods'),
    # path('goods/',goods, name='goods'),
]