from django.urls import path

from familymembers import views

urlpatterns = [
    path('', views.home),
    path('addmember', views.f1, name='addmember'),
    path('show', views.f2, name='show'),
    path('addmemberaction', views.addmemberlogic),
    path('edit/<int:id>', views.editfunction, name='edit'),
    path('delete/<int:id>', views.deletefunction, name='delete'),
    path('addexpense', views.addexpensefunction, name='addexpense'),
    path('saveexpensedata', views.saveexpensedatafunction),
    path('showexpense', views.showexpensefunction, name='showexpense'),
    path('editexpense/<int:id>', views.editexpensefunction, name='editexpense'),
    path('deleteexpense/<int:id>', views.deleteexpensefunction, name='deleteexpense'),
]