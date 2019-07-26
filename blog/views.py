from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost
from .models import Blog, BlogComent
# Create your views here.

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'blogs':blogs,'posts':posts})
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')
def blogpost(request):
        if request.method =='POST':
            form = BlogPost(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.pub_date=timezone.now()
                post.save()
                return redirect('home')
        else:
            form = BlogPost()
            return render(request,'new.html',{'form':form})
def blogedit(req, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    return render(req, 'blogedit.html', {'blog_edit':blog})

def blogupdate(req, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.title = req.POST['title']
    blog.body = req.POST['content']
    blog.save()
    return redirect('/blog/'+str(blog_id))

def blogdelete(req, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('/')

def comentcreate(req, blog_id):
    if (req.method =='POST'):
        blog = get_object_or_404(Blog, id=blog_id)
        blog.blogcoment_set.create(content=req.POST['coment_content'])
    return redirect('/blog/' + str(blog_id))

def comentdelete(req, coment_id):
    coment = get_object_or_404(BlogComent, id=coment_id)
    blog_id = coment.blog.id
    coment.delete()
    return redirect('/blog/'+ str(blog_id))