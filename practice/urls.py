from django.urls import path
from . import views

urlpatterns = [
    # path('', views.say_hello, name='say_hello'),
    path('student/', views.students, name='students'),
    path('say_hello/', views.say_hello),
    path('add-student/', views.addStudents, name="add-stud"),
    path('update_view/<id>', views.update_view, name="upd-stud"),
    path('update_edit/<id>', views.update_edit, name="upd-edit"),
    path('delete/<id>', views.delete, name="delete"),

]
