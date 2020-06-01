from django.shortcuts import redirect,render


def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)
