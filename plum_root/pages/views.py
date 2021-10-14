from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page
from .forms import ContactForm

#index view
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #assert False
            
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['subject'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection = con
            )

            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

# Create your views here.
def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title' : pg.title,
        'content' : pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list' : Page.objects.all(),
    }
    #assert False
    #return HttpResponse("<h1><b>Plum Homepage</b></h1>")
    return render(request, 'pages/page.html', context)