from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

def blogHome(request):
    
    post = Post.objects.all().order_by("-pub_date")
    return render(request, 'blog/blogHome.html',{'posts':post})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    
    comments = BlogComment.objects.filter(post=post, parent=None).order_by("-timestamp")
    replies = BlogComment.objects.filter(post=post,).exclude(parent=None).order_by("-timestamp")
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    return render(request, 'blog/blogPost.html',{'post':post, 'comments':comments, 'replyDict':replyDict})
    

def postComment(request):
    if request.method == 'POST': 
        user = request.user
        postId = request.POST.get('postId')
        post = Post.objects.get(sno=postId)
        parent = request.POST.get('replyId')
        comment = request.POST.get('comment')
        reply = request.POST.get('reply')
       
        
        if parent =="":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.warning(request, "comment added")
          
        else:
            parent = BlogComment.objects.get(sno=parent)
            
            comment = BlogComment(comment=reply, user=user, post=post, parent=parent)
            comment.save()
            messages.warning(request, "reply added")
            
        return redirect(f"/bloghome/blog/{post.slug}")

        
    
def postBlog(request):
    if request.method == "POST":
        author = request.user.first_name
        title = request.POST['title']
        content = request.POST['content']
        slug = request.POST['slug']
        image = request.FILES['image']
        slugAll = Post.objects.all()
        slugCheck = ""
        for i in range(slugAll.count()):
            slugCheck = slugCheck + slugAll[i].slug
            
        if slug not in slugCheck:
            user_Post = Post(author=author, title=title, content=content, slug=slug, image=image)
            user_Post.save()
            messages.success(request,"Blog is posted successfully")
        else:
            messages.warning(request,"Use Different Slug")

    return render(request,'blog/postBlog.html')