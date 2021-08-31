from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from .forms import BooksForm
from Auther_access.models import Book


def home(request):
    return render(request,'index.html')

@login_required
def Dashboard(request):
    return render(request,'Dashboard.html')

#def Login(request):
 #   return render(request,'login.html',)

def Register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form =UserCreationForm()

    return render(request,'registration/register.html',{'form':form})



#def Logout(request):
 #   return render(request,'logout.html')


def Homepage(request):
    return render(request,'home.html')


def BBooks(request, entries_per_page=3):
    ACCOUNTS_PER_PAGE = entries_per_page
    storage = Book.objects.all()
    if request.method == "GET":
        user = request.GET.get('user')
        if user:
            storage = Book.objects.all().filter(Q(title__icontains=user)).distinct()

        p = Paginator(storage.all(), ACCOUNTS_PER_PAGE)
        page = request.GET.get('page', 1)
    #       Books = paginator.page(3)
    #       Books = paginator.page(paginator.num_pages)

    try:
        Books = p.get_page(page)
    except PageNotAnInteger:
        Books = p.page(ACCOUNTS_PER_PAGE)
    except EmptyPage:
        Books = p.page(p.num_pages)

    context = {
        'Books': Books,
    }
    return render(request,'Book.html',context)


def Upload(request):
    if request.method == 'POST':
        form =BooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Books')
    else:
        form = BooksForm
    return render (request,'upload.html',{'form':form})

def Delete(request,pk):
    if request.method =='POST':
        book =Book.objects.get(pk=pk)
        book.delete()
    return redirect('Books')