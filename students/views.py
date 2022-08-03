from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):
    student = Student.objects.all()
    
    return render(request, 'index.html', {'student': student})

def view_one(request, id):
    student = Student.objects.filter(id=id).first()

    return render(request, 'one.html', {'student' :student})

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return redirect('/')
    else:
        form = StudentForm()
        return render(request, 'new.html', {'form': form})

def edit(request,id):
    if request.method == 'POST':
        post = Student.objects.get(id=id)
        form = StudentForm(request.POST,instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited")
            return redirect('/')
    else:
        post = Student.objects.get(id=id)
        form = StudentForm(instance=post)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    post = Student.objects.get(id=id)
    post.delete()
    return redirect("/")
