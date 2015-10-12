from django.shortcuts import render, HttpResponseRedirect
from .forms import EmailForm, JoinForm
from .models import Join
import uuid

def get_ip(request):
    try:
       x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
       if x_forward:
           ip = x_forward
       else:
           ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip
    
def get_ref_id():
    ref_id = str(uuid.uuid4())[:8]
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id
        
def share(request, ref_id):
    context = {"ref_id": ref_id}
    template = "share.html"
    return render(request, template, context)

def home(request):

# Using regular forms
#    form = EmailForm(request.POST or None)
#    if form.is_valid():
#        email = form.cleaned_data['email']
#        new_join, created = Join.objects.get_or_create(email=email)

# Using model forms
    form = JoinForm(request.POST, request.FILES or None)
    if form.is_valid():
        new_join = form.save(commit = False)
    #    email = form.cleaned_data['email']
    #    new_join, created = Join.objects.get_or_create(email=email)
        new_join.ref_id = get_ref_id()
        new_join.ip_address = get_ip(request)
        new_join = form.save()
        return HttpResponseRedirect("/%s" %(new_join.ref_id))
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)
