from django.shortcuts import render, redirect

from .form import StudentForm
from .models import *


def index(request):
    group = Group.objects.all()
    context = {
        'group': group
    }
    if request.method == "POST":
        Group.objects.create(name=request.POST.get("group"), teacher=request.POST.get("teacher"))
        return redirect("index")
    return render(request, 'index.html', context)


def DeleteGroup(request, pk):
    st = Group.objects.get(id=pk)
    st.delete()
    return redirect("/")




def StudentView(request):
    context = {
        "student": Student.objects.all(),
        "group": Group.objects.all()
    }
    if request.method == "POST":
        r = request.POST
        name = r.get("name")
        age = r.get("age")
        group = r.get("group")
        Student.objects.create(group_id=group, name=name, age=age)
        return redirect("student")
    return render(request, 'student.html', context)



def changeStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')

    contex = {
        'form': form,
        'student': Student.objects.get(id=pk),
        'group': Group.objects.all()
    }
    return render(request, 'change_student.html', contex)




def DeleteStudent(request, pk):
    st = Student.objects.get(id=pk)
    st.delete()
    return redirect("student")



