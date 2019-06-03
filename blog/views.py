from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, "home.html", {"blogs":blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {"blog":blog_detail})

def new(request): #new.html 띄어주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() #블로그라는 클래스로 부터 블로그라는 개체 생성
    blog.title = request.GET['title'] #new.html에서 넘어온 title을 blog.title변수에 넣어라
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
