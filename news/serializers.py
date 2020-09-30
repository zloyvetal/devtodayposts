# сделать два, один на коменты один на посты.
# todo https://www.django-rest-framework.org/tutorial/1-serialization/
from rest_framework import serializers
from .models import Posts, Comments


# 59:50 serializer

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
