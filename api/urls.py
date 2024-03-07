from django.urls import path

from api.views import auth_view,views

urlpatterns = [
    path("login/",auth_view.login,name="login"),
    path("singup/",auth_view.singup,name="signup"),
    # path("test_token/",auth_view.test_token,name="test_token"),
    # user prifile routes
    path("user_profile",views.UserProfileListCreateView.as_view(),name="test"),
    path("user_profile/<int:pk>/",views.UserProfileRetrieveUpdateDestroyView.as_view(),name="test"),
    # pakages routes
    path('packages/', views.PackageListCreateView.as_view()),
    path('packages/<int:pk>/', views.PackageRetrieveUpdateDestroyView.as_view()),
    # services routes
    path("services/",views.ServiceListCreateView.as_view()),
    path("services/<int:pk>/",views.ServiceRetrieveUpdateDestroyView.as_view()),
    # booking routes
    path("boking/",views.BookingListCreateView.as_view()),
    path("boking/<int:pk>/",views.BookingRetrieveUpdateDestroyView.as_view()),
    # tab routes
    path("tags/",views.TagListCreateView.as_view()),
    path("tags/<int:pk>/",views.TagRetrieveUpdateDestroyView.as_view())
]
