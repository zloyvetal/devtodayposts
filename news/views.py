from rest_framework.response import Response

from .serializers import PostsSerializer, CommentsSerializer
from rest_framework import generics
from .models import Posts, Comments
from rest_framework.views import APIView


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostsSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()


class CommentsCreateView(generics.CreateAPIView):
    serializer_class = CommentsSerializer


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class CommentsDetalView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class UpvoteUpdateView(APIView):

    def get(self, request, pk):
        post = Posts.objects.get(pk=pk)
        post.amount_of_upvoutes += 1
        post.save()
        return Response("U successful add +1 votes")


class UpvoteResetAllView(APIView):

    def get(self, request):
        Posts.objects.all().update(amount_of_upvoutes=0)
        return Response("U successful reset all votes")
