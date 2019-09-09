from django.shortcuts import render,redirect,get_list_or_404
from .models import Review
from .models import Website
from .forms import WebsiteForm,ReviewForm
from django.contrib.auth.models import  User  

# Create your views here.
def home(request):
    title='Featured'
    webs=Website.objects.all()
    # webs = Website.objects.all()
    return render(request,'index.html',{'webs':webs,'title':title,'reviews':'reviews'})

def add_website(request):
    title = 'Post website'
    user=request.user
    if request.method=='POST':
        user = request.user
        owner =Website(owner=user)
        form = WebsiteForm(request.POST,request.FILES,instance=owner)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =WebsiteForm()
    return render (request,'website.html',{'form':form,'title':title})
        
def review(request):
    title = 'Website Review'
    if request.method=='POST':
        form =ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ReviewForm()
    return render(request,'review.html',{'form':form,'title':title})
def my_sites(request):
    title='Your Posted sites'
    user = request.user
    sites = Website.objects.all().filter(owner__username=user)
    # site = sites.reviews.all()[1]
    # reviews=site.reviews.all()
    # review= get_list_or_404(Website,reviews='pk')
    # print(reviews)
    # for review in reviews:
    #     tit=review.title
        # print(title)
        # return review.title
    return render (request,'sites.html',{'title':title,'sites':sites,'reviews':'reviews'})

