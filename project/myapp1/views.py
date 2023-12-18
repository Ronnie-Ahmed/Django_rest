from django.shortcuts import render
from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class SnippestList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        snippet=Snippets.objects.all()
        serializers=SnippetSerializer(snippet,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializers=SnippetSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


class SnippetDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            snippet=Snippets.objects.get(pk=pk)
            return snippet
        except Snippets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        serializers=SnippetSerializer(snippet)
        return Response(serializers.data)
    
    def put(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        serializers=SnippetSerializer(snippet,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def delete(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_100_CONTINUE)
        

class SnippestModelGenerics(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    
    queryset=Snippets.objects.all()
    serializer_class = SnippetSerializer
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    
    
class SnippestModelDetailsGenerics(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    
    queryset=Snippets.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


# @api_view(['GET','POST'])
# def snippet_list(request):
    
#     if request.method=='GET':
#         snippets=Snippets.objects.all()
#         serializers=SnippetSerializer(snippets,many=True)
#         return Response(serializers.data)
    
#     elif request.method=='POST':
#         serializers=SnippetSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request, pk):
#         try:
#             snippet=Snippets.objects.get(pk=pk)
#         except Snippets.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#         if request.method=='GET':
#             serializers=SnippetSerializer(snippet)
#             return Response(serializers.data)
        
#         elif request.method=='PUT':
#             serializers=SnippetSerializer(snippet,data=request.data)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response(serializers.data,status=status.HTTP_200_OK)
#             return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#         elif request.method=='DELETE':
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
