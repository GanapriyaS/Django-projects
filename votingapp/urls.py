from django.urls import path,include
from . import views
urlpatterns=[
             path('',views.start,name="voting"),
             path('getQuery',views.getQuery,name="getQuery"),
             path('sort',views.sort,name="sort")
]
