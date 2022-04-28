from django.urls import path
from .views import  BankDelete, BankUpdate, BankView,BankDetail,BankCreate
from  django.contrib.auth.views import LogoutView



app_name='bank'
urlpatterns = [
    path('',BankView.as_view(),name='bank'),
    path('create/',BankCreate.as_view(),name='bank-create'),
    path('detail/<int:pk>/',BankDetail.as_view(),name='bank-detail'), 
    path('update/<int:pk>/',BankUpdate.as_view(),name='bank-update'), 
    path('delete/<int:pk>/',BankDelete.as_view(),name='bank-delete'), 
   
]
