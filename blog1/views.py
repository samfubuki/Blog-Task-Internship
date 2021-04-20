from django.shortcuts import render
from .forms import BlogForm
from .models import BlogDatabase
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        form = BlogForm()
        candidates = BlogDatabase.objects.all()
        return render(request,'blog1/home.html',{'candidates':candidates,'form':form})
    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'blog1/home.html',{'form':form})

class CandidateView(View):
    def get(self,request, pk):
        candidate = BlogDatabase.objects.get(pk=pk)
        return render(request,'blog1/candidate.html',{'candidate':candidate})
