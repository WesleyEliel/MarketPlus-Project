from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from Blog.models import *
from Blog.forms import *
from django.views.generic.list import ListView
from taggit.models import Tag

import calendar

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/posts/list.html'

def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None 

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.get_page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.get_page(paginator.num_pages)
    
    tags = Tag.objects.all()[:12]
    context = locals()
    template = 'blog/posts/list.html'
    return render(request, template, context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                publish__year=year,publish__month=month,
                                publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    #Similars post
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    #Comment and Share forms 
    new_comment = None
    if request.method == 'POST':
        send=False
        # A comment was posted or a E-mail was send
        if request.POST['comment_or_share'] == 'CF':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
            share_form = EmailPostForm()
        elif request.POST['comment_or_share'] == 'SF':
            form = EmailPostForm(request.POST)
            if form.is_valid():
                # Form fields passed validation
                cd = form.cleaned_data
                post_url = request.build_absolute_uri(post.get_absolute_url())
                subject = "{} ({}) recommends you reading {}".format(cd['name'], cd['email'], post.title)
                message = "Read {} at {}\n\n{}\'s comments:{}".format(post.title, post_url, cd['name'], cd['comments'])
                send_mail(subject, message, 'admin@myblog.com',[cd['to']])
                sent = True
            comment_form = CommentForm()
            share_form = EmailPostForm()
        else:
            pass
        
    else:
        comment_form = CommentForm()
        share_form = EmailPostForm()

    context = locals()
    template = 'blog/posts/details.html',
    return render(request, template, context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search=search_vector,rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
        
    return render(request,'blog/posts/search.html',{'form': form, 'query': query, 'results': results})

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(
            post.get_absolute_url())
            subject = '{} ({}) recommends you reading {}'.format(cd['name'], cd['email'], post.title)
            message = 'Read {} at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    
    context = locals()
    template = 'blog/post/share.html'
    return render(request, template, context)