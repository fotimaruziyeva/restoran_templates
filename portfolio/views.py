from django.shortcuts import render
from portfolio.forms import ContactForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .bot import send_message
from .models import Contact,Team,MenuItem,MenuCategory


def home_view(request):
   categories=MenuCategory.objects.all()
   team=Team.objects.all()
   menu=MenuItem.objects.all()
   context={
     "team": team,
     "menu":menu,
     'categories': categories,
   }
   return render(request=request,template_name='index.html',context=context)



class ContactListView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message= form.cleaned_data.get('message')
        text = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        send_message(text)
        
        Contact.objects.create(name=name, email=email, message=message)
        return super().form_valid(form)

class MenuListView(ListView):
  model =MenuItem
  template_name = 'menu.html'
  context_object_name = 'menu_items'
    
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MenuCategory.objects.all()
        context['menu_items'] = MenuItem.objects.all()
        return context


class ServiceListView(ListView):
  model = Contact
  template_name = 'service.html'
  

class AboutListView(ListView):
  model = Team
  template_name = 'about.html'
  context_object_name='team'
  
  def get_queryset(self):
        return Team.objects.all()
  
