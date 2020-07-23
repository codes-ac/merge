from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

def index(request):
    post = Post.objects.all().order_by("-views")[:2]
    return render(request, 'home/index.html',{'posts':post})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(desc)<5:
            messages.warning(request,'Fill the form correctly...')
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request,'Succesfully submitted...')

    return render(request, 'home/contact.html')


def search(request):
    search = request.GET['query']
    if len(search)>50:
        messages.warning(request,"Entered text size is too large, please refine your search...")
        post = []
    else:
        postTitle = Post.objects.filter(title__icontains=search)
        postContent = Post.objects.filter(content__icontains=search)
        post = postTitle.union(postContent)
    return render(request, 'home/seacrh.html', {'post':post, 'query':search})



def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['userName']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        all = [fname, lname,email,username,pass1,pass2]
        # if all == []:
        #     messages.success(request,'Your Codes_AC Account has been successfully created')
        #     return redirect('home')


        if len(username)>10:
            messages.error(request,'Sign up  Failed, username is too long...')
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,'Sign Up failed, password does not match...')
            return redirect('home')


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your Codes_AC Account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 Not Found')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('home')

        else:
            messages.error(request,'Invalid Credentials...')
            return redirect('home')

    return HttpResponse('404 Not Found')

def userlogout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect('home')


    