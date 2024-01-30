from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view

from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView
from django.views.decorators.http import require_POST


@api_view(['POST'])
@require_POST
def post_comment(request, post_id):
    """
    calling the function allows you to add a new comment to a blog post
    :param request: required parameter
    :param post_id: ID of the post to which the comment was added
    :return: page containing a message about adding a post
    """
    post = get_object_or_404(Post, id=post_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'myapi/post/comment.html',
                  {'post': post, 'form': form, 'comment': comment})


@api_view(['GET'])
def post_detail(request, id):
    """
    displays a page with a post, comments added to it, and a form for adding a comment
    :param request: required parameter
    :param id: the ID of the post to display
    :return: html page with post, comments and form
    """
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'myapi/post/detail.html',
                  {'post': post, 'comments': comments, 'form': form})


@api_view(['GET'])
class PostListView(ListView):
    """
    displays a list of all existing blog posts
    """
    current_time = timezone.now()
    queryset = Post.objects.filter(publish__lte=current_time)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'myapi/post/list.html'
