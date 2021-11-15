from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Quote
from .forms import QuoteForm
from pages.models import Page

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class QuoteView(DetailView):
    model = Quote
    context_object_name = 'quote'

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'

    def get_context_data(self, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    return  render(request, 'quotes/quote.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})



# Create your views here.
