from django.shortcuts import render
from .models import Student

# shows all students name
def index(request):
    all_students = Student.objects.all()
    return render(request, 'student/index.html', {'students': all_students})
