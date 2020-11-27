from django.urls import path
from . import views

urlpatterns=[

    path('<str:my_name>',views.purchase,name="purchase"),
    path('placed/<str:my_name>',views.placed,name="placed")

]