from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='title')
    link = models.URLField(max_length=100, verbose_name='url_link')
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvoutes = models.PositiveSmallIntegerField(editable=False, default=0)
    author_name = models.CharField(max_length=100, verbose_name='author_name')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comments(models.Model):
    author_name = models.CharField(max_length=100, verbose_name='author_name')
    content = models.TextField(max_length=1000, verbose_name='content')
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
