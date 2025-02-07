from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.user_form_submission,name="home"),
   path('user_read/',views.user_read,name="read"),
   path('update-user/<int:user_id>/', views.update_user, name='update_user'),
   path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
   path('fuser/<int:user_id>/',views.fuser,name="read_user"),
    
]
