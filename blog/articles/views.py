from django.shortcuts import render

def post_list(request):
    return render(request, 'articles/post_list.html', {})