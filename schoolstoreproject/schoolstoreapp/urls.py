from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('click/<int:std_id>/',views.click,name='click'),
    path('form/', views.std_form, name='std_form'),
    path('getcourse/',views.getcourse,name='getcourse')
]