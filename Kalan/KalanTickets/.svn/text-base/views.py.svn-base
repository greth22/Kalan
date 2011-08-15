# Create your views here.
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from Kalan.KalanTickets.models import *
from Kalan.KalanTickets.forms import CreateTicket, AddEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    return HttpResponse("NOTHING TO SEE HERE")

@login_required
def tagView(request, tag):
    return render_to_response("TagPage.html",{'tag': Tag.objects.filter(text=tag)[0]})

@login_required
def dashboard(request):
    return render_to_response("ProtoQueue.html", {'tickets': Ticket.objects.all()})

@login_required
def ticket(request, ticket_id):
    try:
        tid = int(ticket_id)
    except ValueError:
        raise Http404()        
    
    return render_to_response("Ticket.html", {'ticket':Ticket.objects.filter(id=tid)[0]})

@login_required
def search(request, search_terms):
    return HttpResponse("You were searching for '%s'" % search_terms)

@login_required
def createTicket(request):
    if request.method == 'GET':
        form = CreateTicket(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            if not (Account.objects.filter(name=cd['account'])):
                acc = Account.objects.create(name=cd['account'])
            else:
                acc = Account.objects.filter(name=cd['account'])[0]
            
            ticket = Ticket.objects.create(subject=cd['subject'])
            ticket.account = [acc]
            ticket.save()
            
            return HttpResponseRedirect('/Tickets/id/%s' % ticket.id)
    else:
        form = CreateTicket()
    
    return render_to_response('CreateTicket.html', {'form': form})

@login_required
def addEntry(request, ticket_id):    
    try:
        tid = int(ticket_id)
    except ValueError:
        return Http404()
    
    if request.method == 'GET':
        form = AddEntry(request.GET)
        if form.is_valid():            
            
            cd = form.cleaned_data
            ticket = Ticket.objects.filter(id=tid)[0]
            Entry.objects.create(subject=cd['subject'],ticket_id=tid,body=cd['body'])
            
            return HttpResponseRedirect('/Tickets/id/%s' % tid)
    else:
        form = AddEntry()
    
    return render_to_response('AddEntry.html', {'form': form, 'id': tid})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect to success
        return HttpResponseRedirect('/Tickets/')
    else:
        # invalid login
        return render_to_response('LoginPage.html', {'errors': ("Invalid Login")})
    
#def loginSuccessRedirect(request):
    
        
