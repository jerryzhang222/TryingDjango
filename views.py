from django.shortcuts import render
from .forms import EmailForm, JoinForm
from .models import Join

def home(request):

# Using regular forms
#    form = EmailForm(request.POST or None)
#    if form.is_valid():
#        email = form.cleaned_data['email']
#        new_join, created = Join.objects.get_or_create(email=email)

# Using model forms
    form = JoinForm(request.POST, request.FILES or None)
    if form.is_valid():
    #    new_join = form.save(commit = False)
    #    email = form.cleaned_data['email']
    #    new_join, created = Join.objects.get_or_create(email=email)
        new_join = form.save()
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)
