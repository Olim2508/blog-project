from typing import Text
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, resolve_url
from . models import Comment, Post
from django.urls import reverse
from .forms import PostForm

# DRF links
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from rest_framework.decorators import api_view
from rest_framework import status
from .todo import PostSerializer

def index(request):
    post = Post.objects.order_by('-date')
    print()
    context = {
        'post': post
    }
    return render(request, 'index.html', context)



def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

def comment(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            post.comment_set.create(user = request.user, text = request.POST.get('text'))

    return redirect(reverse('post_detail', kwargs = {'pk':pk}))

def create_post(request):

    if request.method == 'POST':
        post = PostForm(request.POST)
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')  
        post.author = request.user
        post.save()                         
        return redirect('index')
    else:
        post = PostForm()
        return render(request, 'create_post.html', {'post': post})


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        post.save()
        return redirect('post_detail', pk = post.id)
    else:
        return render(request, 'edit_post.html', {'post': post})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    else:
        return render(request, 'delete_post.html', {'post': post})


def delete_comment(request, pk):    
    comment = Comment.objects.get(pk = pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    else:
        return render(request, 'delete_comment.html', {'comment':comment})
    






# DRF class-based views

class PostListView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AuthorListView(APIView):
    def get(self, request):
        author = User.objects.all()
        serializer = PostSerializer(author, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = PostSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = PostSerializer(author, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)