from django.urls import path
from .views import UserRegisterView, ProductListView

urlpatterns = [
    path("", UserRegisterView.as_view(), name="user_register"),
    path("productos/", ProductListView.as_view(), name="productos_lista"),
]
