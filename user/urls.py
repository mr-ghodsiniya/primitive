from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", views.UserLogin.as_view()),
    path("verify/", views.UserVerify.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("create-post/", views.PostCreate.as_view()),
    path("get-post/<int:pk>/", views.PostRetrieve.as_view()),
    path("update-post/<int:pk>/", views.PostUpdate.as_view()),
    path("delete-post/<int:pk>/", views.PostDelete.as_view()),
]