from django.shortcuts import render


from .models import BlogPost


def index(request):
    form_list = BlogPost.objects.all()
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)

def userIndex(request):
    form_list = BlogPost.objects.filter(username= request.user)
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)
