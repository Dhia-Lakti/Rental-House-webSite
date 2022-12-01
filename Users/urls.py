from django.urls import path
from .views import getAllUsers, AddUser, getUserById, updateUserById, deleteUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', getAllUsers, name='getAllUsers'),
    path('add', AddUser, name='AddUser'),
    path('<int:user_id>', getUserById, name='getUserById'),
    path('update/<int:user_id>', updateUserById, name='updateUserById'),
    path('delete/<int:user_id>', deleteUser, name='deleteUser'),
    
    

]
