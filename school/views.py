from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student, Teacher, Department, Subject
from django import forms


# Create your views here.
def index(request):
    # Get count of students and teachers for the dashboard
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    subject_count = Subject.objects.count()
    
    # Mock data for the dashboard
    context = {
        'student_count': student_count,
        'teacher_count': teacher_count,
        'subject_count': subject_count,
        'upcoming_exams': 15,
        'results_published': 8,
        'total_expenses': 10000,
        'due_fees': 1500,
        'students': Student.objects.all()[:2],  # Get first two students for the cards
        'notices': [
            {
                'date': '16 May, 2017',
                'time_ago': '5 min ago',
                'author': 'Jennyfer Lopez',
                'author_color': 'blue',
                'message': 'Great School management system dummy text of the printing and typesetting industry.'
            },
            {
                'date': '16 May, 2017',
                'time_ago': '10 min ago',
                'author': 'Kazi Fahim',
                'author_color': 'orange',
                'message': 'Great School management system dummy text of the printing and typesetting industrysm simply.'
            },
            {
                'date': '16 May, 2017',
                'time_ago': '20 min ago',
                'author': 'Gizzar Awala',
                'author_color': 'gray',
                'message': 'Great School management system dummy text of the printing and typesetting industry.'
            }
        ],
        'expenses': [
            {
                'id': 3055,
                'type': 'Salary',
                'amount': 300.00,
                'status': 'Due',
                'email': 'kazifehim93@gmail.com',
                'date': '20/06/2017'
            },
            {
                'id': 3056,
                'type': 'Exam Fee',
                'amount': 500.00,
                'status': 'Paid',
                'email': 'kazifehim93@gmail.com',
                'date': '20/06/2017'
            },
            {
                'id': 3057,
                'type': 'Library Fee',
                'amount': 900.00,
                'status': 'Paid',
                'email': 'kazifehim93@gmail.com',
                'date': '20/06/2017'
            },
            {
                'id': 3058,
                'type': 'Class Test Fee',
                'amount': 300.00,
                'status': 'Due',
                'email': 'kazifehim93@gmail.com',
                'date': '20/06/2017'
            },
            {
                'id': 3059,
                'type': 'Exam Fee',
                'amount': 500.00,
                'status': 'Paid',
                'email': 'kazifehim93@gmail.com',
                'date': '20/06/2017'
            }
        ]
    }
    
    return render(request, 'school/student_dashboard.html', context)

# Student form for create and edit operations
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'gender', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Student list view
def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'page_title': 'Student List'
    }
    return render(request, 'school/student_list.html', context)

# Student detail view
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
        'page_title': f'Student: {student.name}'
    }
    return render(request, 'school/student_detail.html', context)

# Student edit view
def student_edit(request, pk=None):
    # If pk is provided, we're editing an existing student
    if pk:
        student = get_object_or_404(Student, pk=pk)
        page_title = f'Edit Student: {student.name}'
    else:
        # Otherwise, we're creating a new student
        student = None
        page_title = 'Add New Student'
    
    # Handle form submission
    if request.method == 'POST':
        if student:
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        if student:
            form = StudentForm(instance=student)
        else:
            form = StudentForm()
    
    context = {
        'form': form,
        'student': student,
        'page_title': page_title
    }
    
    return render(request, 'school/student_form.html', context)

# Student create view (uses the same form as edit)
def student_create(request):
    return student_edit(request)

# Student delete view
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
        
    context = {
        'student': student,
        'page_title': f'Delete Student: {student.name}'
    }
    
    return render(request, 'school/student_confirm_delete.html', context)

# Teacher form for create and edit operations
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'gender', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Teacher list view
def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'page_title': 'Teacher List'
    }
    return render(request, 'school/teacher_list.html', context)

# Teacher detail view
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    context = {
        'teacher': teacher,
        'page_title': f'Teacher: {teacher.name}'
    }
    return render(request, 'school/teacher_detail.html', context)

# Teacher edit view
def teacher_edit(request, pk=None):
    # If pk is provided, we're editing an existing teacher
    if pk:
        teacher = get_object_or_404(Teacher, pk=pk)
        page_title = f'Edit Teacher: {teacher.name}'
    else:
        # Otherwise, we're creating a new teacher
        teacher = None
        page_title = 'Add New Teacher'
    
    # Handle form submission
    if request.method == 'POST':
        if teacher:
            form = TeacherForm(request.POST, instance=teacher)
        else:
            form = TeacherForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        if teacher:
            form = TeacherForm(instance=teacher)
        else:
            form = TeacherForm()
    
    context = {
        'form': form,
        'teacher': teacher,
        'page_title': page_title
    }
    
    return render(request, 'school/teacher_form.html', context)

# Teacher create view (uses the same form as edit)
def teacher_create(request):
    return teacher_edit(request)

# Teacher delete view
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
        
    context = {
        'teacher': teacher,
        'page_title': f'Delete Teacher: {teacher.name}'
    }
    
    return render(request, 'school/teacher_confirm_delete.html', context)

# Subject form for create and edit operations
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

# Subject list view
def subject_list(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
        'page_title': 'Subject List'
    }
    return render(request, 'school/subject_list.html', context)

# Subject detail view
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        'subject': subject,
        'page_title': f'Subject: {subject.name}'
    }
    return render(request, 'school/subject_detail.html', context)

# Subject edit view
def subject_edit(request, pk=None):
    # If pk is provided, we're editing an existing subject
    if pk:
        subject = get_object_or_404(Subject, pk=pk)
        page_title = f'Edit Subject: {subject.name}'
    else:
        # Otherwise, we're creating a new subject
        subject = None
        page_title = 'Add New Subject'
    
    # Handle form submission
    if request.method == 'POST':
        if subject:
            form = SubjectForm(request.POST, instance=subject)
        else:
            form = SubjectForm(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        if subject:
            form = SubjectForm(instance=subject)
        else:
            form = SubjectForm()
    
    context = {
        'form': form,
        'subject': subject,
        'page_title': page_title
    }
    
    return render(request, 'school/subject_form.html', context)

# Subject create view (uses the same form as edit)
def subject_create(request):
    return subject_edit(request)

# Subject delete view
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
        
    context = {
        'subject': subject,
        'page_title': f'Delete Subject: {subject.name}'
    }
    
    return render(request, 'school/subject_confirm_delete.html', context)

