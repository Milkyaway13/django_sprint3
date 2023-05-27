from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        pub_date__lte=make_aware(datetime.now()),
        is_published=True,
        category__is_published=True
    ).order_by('-created_at')[:5]
    context = {'posts': posts}
    return render(request, template_name, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'category', 'author', 'location'
            ).filter(
                id=post_id,
                pub_date__lt=make_aware(datetime.now()),
                is_published=True,
                category__is_published=True),
        )
    template_name = 'blog/detail.html'
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    template_name = 'blog/category.html'
    posts = Post.objects.select_related(
        'category', 'author', 'location'
    ).filter(
        category__slug=category_slug,
        pub_date__lt=make_aware(datetime.now()),
        is_published=True,
        category__is_published=True)
    context = {'category': category,
               'post_list': posts}
    return render(request, template_name, context)
