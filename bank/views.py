from xml.parsers.expat import model
from attr import fields
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView
from importlib_metadata import files
from bank.models import Customer
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView,UpdateView,DeleteView





class BankView(ListView):
    model=Customer
    context_object_name='bank'

class BankCreate(CreateView):
    model=Customer
    fields="__all__"
    success_url=reverse_lazy('bank:bank')

    
class BankDetail(DetailView):
    model=Customer
    context_obeject_name='bank:bank'
    
class BankUpdate(UpdateView):
    model=Customer
    fields='__all__'
    success_url=reverse_lazy('bank:bank')



class BankDelete(DeleteView):
    model=Customer
    fields='__all__'
    success_url=reverse_lazy('bank:bank')



    
