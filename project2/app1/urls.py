from django.urls import path
from app1 import views

urlpatterns = [
    path('project/',views.StudentModelView.as_view()),
    path('project/<int:pk>/',views.StudentDetailsModelView.as_view()),
    path('generic/',views.StudentGenericsModelView.as_view()),
    path('generic/<int:pk>/',views.StudentDetailsGenericsModelView.as_view())
  
]
