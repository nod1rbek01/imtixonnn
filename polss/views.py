from django.shortcuts import render
from .models import MyModel


def appp(request):
    posts = MyModel.objects.all()
    return render(request, "test.html", {"posts": posts})
