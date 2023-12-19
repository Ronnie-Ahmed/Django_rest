from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics



# Create your views here.

class StudentModelView(APIView):
    def get(self,request,*args,**kwargs):
        student=Student.objects.all()
        serializers=StudentSerializers(student,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

class StudentDetailsModelView(APIView):
    def get_object(self,pk):
        try:
            student=Student.objects.get(pk=pk)
            return student
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk,*args,**kwargs):
        student=self.get_object(pk)
        serializers=StudentSerializers(student).data
        return Response(serializers.data)
    
    def get(self,request,pk,*args,**kwargs):
        student=self.get_object(pk)
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def put(self,request,pk,*args,**kwargs):
        student=self.get_object(pk)
        serializers=StudentSerializers(student,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
        
class StudentGenericsModelView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
        
class StudentDetailsGenericsModelView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)