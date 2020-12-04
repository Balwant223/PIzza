from django.urls import path
from . import views

app_name='App'
urlpatterns = [
    path('',views.pizzas_list,name='All_pizza List'),
    path('add',views.create_pizza,name='Add_pizza'),
    path('update/<int:id>',views.alter_pizza,name='Alter_pizza'),
]