from django.shortcuts import render,redirect
from film.models import Film
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from film.forms import filmform
# def home(request):
#     k = Film.objects.all()
#     return render(request,'home.html',{'b':k})
# def add(request):
#     if (request.method == "POST"):
#         n=request.POST['n']
#         d=request.POST['d']
#         r=request.POST['r']
#         t= request.POST['t']
#         s= request.POST['s']
#         a= request.POST['a']
#         m= request.POST['m']
#         c=request.FILES['c']
#         b=Film.objects.create(name=n,desc=d,director=r,writer=t,Starring=s,release_year=a,running_time=m,cover=c)
#         b.save()
#         return home(request)
#     return render(request,'add.html')
# def view_movie(request,p):
#     b=Film.objects.get(id=p)
#     return render(request,'view.html',{'b':b})
# def update_movie(request,p):
#         film=Film.objects.get(id=p)
#         form=filmform(instance=film)
#         if (request.method == "POST"):
#             form=filmform(request.POST, request.FILES, instance=film)
#             if form.is_valid():
#                 form.save()
#             return home(request)
#         return render(request,'update.html',{'form':form})
# def delete_movie(request,p):
#     if request.method=="POST":
#         film=Film.objects.get(id=p)
#         film.delete()
#         return home(request)
#     return render(request,'delete.html')

class detailview(DetailView):
    model=Film
    template_name="view.html"
    context_object_name="b"
class movielistview(ListView):
    model=Film
    template_name="home.html"
    context_object_name="b"
class createview(CreateView):
    model=Film
    template_name="add.html"
    fields=['name','desc','cover','director','writer','Starring','release_year','running_time']
    success_url=reverse_lazy('home')
class deleteview(DeleteView):
    model=Film
    template_name="delete.html"
    success_url=reverse_lazy('home')
class updateview(UpdateView):
    model=Film
    template_name="update.html"
    fields=['name','desc','cover','director','writer','Starring','release_year','running_time']
    success_url=reverse_lazy('home')