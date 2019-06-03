from django.shortcuts import render
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can now login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def home(request):
    # print(Comment.objects.all())
    # context = {
    #     'posts': Post.objects.all()
    # }

    return render(request, "users/home.html")

