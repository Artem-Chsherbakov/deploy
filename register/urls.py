from django.contrib import admin
from django.urls import path, include
from . import views

#app_name = 'register'

urlpatterns = [

    path('list/<str:Model>', views.list_user,
         name = "list_u"
         ),
    path('new/<str:Model>/', views.new_user, name = 'new_u'),
    path('erase/<str:Model>/<str:k1>', views.erase_user, name = 'erase_u'),
    path('update/<str:Model>/<str:k1>', views.update_user, name = 'update_u'),
    path('show_one/<str:Model>/<str:k1>', views.show_one, name = 'show_one')

]