from django.urls import path,include
from . import views
urlpatterns=[
             path('',views.start,name="todoapp"),
             path('add',views.start,name="add"),
             path('submit',views.submit,name="submit"),
             path('delete/<int:id>',views.delete,name='delete'),
             path('edit/<int:id>',views.edit,name='edit'),
             path('list',views.list,name='list'),
             path('sortdata',views.sortdata,name='sortdata'),
             path('search',views.search,name='search'),
             path('update/<int:id>',views.update,name='update')
]
