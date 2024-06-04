from django.urls import path
from . import views 
urlpatterns = [
     path('',views.post,name="post"),
     path('home/' ,views.home,name='home'),
     path('details/<int:id>',views.details,name='details'),
     path('delete/<int:id>',views.delete,name='delete'),
     path('update/<int:id>',views.update,name='update'),
     path('create/',views.create,name='create'),
]
