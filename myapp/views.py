from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from . models import *

def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'blogs': blogs})
def home(request):
    return render(request, 'index.html')
# Create your views here.
def login_view(request):
    return render(request,'login.html')
def register(request):

   if request.method == "POST":

       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       place = request.POST['place']
       username = request.POST['username']
       password = request.POST['password']

       user = User.objects.create_user(
           username=username,
           password=password,
           email=email
       )

       UserProfile.objects.create(
           USER=user,
           name=name,
           email=email,
           phone=phone,
           place=place
       )

       return redirect('login')

   return render(request,'register.html')

def admin_home(request):
   return render(request,'admin_home.html')
def user_home(request):
   blogs = Blog.objects.all()
   return render(request,'user_home.html',{'blogs':blogs})

def my_blogs(request):
   blogs = Blog.objects.filter(USER=request.user)
   return render(request,'my_blogs.html',{'blogs':blogs})
def view_blogs_admin(request):

   blogs = Blog.objects.all()

   return render(request,'view_blogs_admin.html',{'blogs':blogs})
def add_blog(request):

   if request.method == "POST":

       title = request.POST['title']
       content = request.POST['content']
       image = request.FILES.get('image',None)

       Blog.objects.create(
           USER=request.user,
           title=title,
           content=content,
           image=image
       )

       return redirect('my_blogs')

   return render(request,'add_blog.html')

def login_view(request):

   if request.method == "POST":

       username = request.POST['username']
       password = request.POST['password']

       user = authenticate(request, username=username, password=password)

       if user is not None:

           login(request, user)

           if user.is_superuser:
               return redirect('admin_home')

           else:
               return redirect('user_home')

   return render(request,'login.html')

def edit_blog(request,id):

   blog = Blog.objects.get(id=id)

   if request.method == "POST":

       blog.title = request.POST['title']
       blog.content = request.POST['content']

       if 'image' in request.FILES:
           blog.image = request.FILES['image']

       blog.save()

       return redirect('my_blogs')

   return render(request,'edit_blog.html',{'blog':blog})


def delete_blog(request,id):

   blog = Blog.objects.get(id=id)

   blog.delete()

   return redirect('my_blogs')

def view_blogs_admin(request):
    blog=Blog.objects.all()
    return render(request,'view_blogs_admin.html',{'blogs':blog} )
    
def view_blogs_user(request):
    user=UserProfile.objects.all()
    return render(request,'view_blogs_user.html',{'users':user} )
