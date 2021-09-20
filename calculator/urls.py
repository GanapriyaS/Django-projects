from django.urls import path,include
from . import views
urlpatterns=[
             path('',views.start,name="calculator"),
             path('calc',views.calc,name="calc")
]
