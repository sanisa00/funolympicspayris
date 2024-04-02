from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('', views.home, name="home"),
    path('event/', views.event, name="event"),
    path('schedule/', views.schedule, name="schedule"),
    path('livestream/<str:pk>/', views.livestream, name="livestream"),
    path('about/', views.about, name="about"),
    path('update-user/', views.updateUser, name="update-user"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

