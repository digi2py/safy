from django.shortcuts import render
from blog.models import Post, Comment
from django.http import HttpResponse

# Create your views here.


def home(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, 'core/home.html', data)

def posts(request, post_number):
    post = Post.objects.get(id=post_number)
    posts = Post.objects.all()
    if request.method == 'POST':
        commenter = request.user
        comment = request.POST.get('comment')
        
        commentsave = Comment(
            commenter = commenter, 
            comment = comment,
            post = Post.objects.get(id = post_number)
            ).save()
        
    post = Post.objects.get(id = post_number)
    filtered_comment = Comment.objects.filter(post=post, active = True)
    data = {'post':post, 'posts':posts, 'comments':filtered_comment}
    
    
    
    return render(request, 'core/post.html', data)