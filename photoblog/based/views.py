from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FeedbackForm, ProductForm, ChatForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Feedback, Product, Chat
from django.contrib.auth.models import Group


is_staff = Group.objects.get_or_create(name='staff')
users_in_stuff = User.objects.filter(groups__name='staff')

# Create your views here.
def index(request):
    template = 'blog'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'page_obj': page_obj
    }
    return render(request, template, context)

def home(request):
    return render(request, "home.html")

def sign_up(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'registration.html', {'form':form})

def links(request):
    return render(request, "links.html")

def site(request):
    return render(request, "site.html")

def feedback(request):
    return render(request, "feedback.html")

def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {'products':products})

@login_required
def product_create(request):
    form = ProductForm(request.POST or None, files=request.FILES or None,)
    if form.is_valid():
        product = form.save(commit=False)
        product.author = request.user
        product.save()
        return redirect('blog')
    return render(request, 'product_creation.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    title = str(product.text)[:30]
    number_of_products = Product.objects.filter(author=product.author).count()
    form = ChatForm()
    chats = Chat.objects.filter(product=product)
    context = {
        'product': product,
        'title': title,
        'number_of_products': number_of_products,
        'form': form,
        'chats': chats
    }
    return render(request, 'product_detail', context)

def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.author != request.user and request.user not in users_in_stuff:
        return redirect('product', product_id_id=product_id)
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
        instance=product
    )
    if form.is_valid():
        form.save()
        return redirect('product', product_id=product_id)
    context = {
        'product': product,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'product_creation.html', context)

def product(request, product_id):
    product = Product.objects.get(id = product_id)
    product_chats = Chat.objects.filter(product=product.id)

    if request.user in users_in_stuff:
        permission_check = True
    else:
        permission_check = False

    if request.method == 'POST':
        chat = Chat.objects.create(
            author = request.user,
            product = product,
            text = request.POST.get('body')
        )
        return redirect('product',product_id=product.id)
    context = {
        'product':product,
        'product_chats':product_chats,
        'permission_check': permission_check
        }
    return render(request, 'product_detail.html', context)

def meeedia(request):
    return render(request, "media.html")

def log_in(request):
    form = UserCreationForm()
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password doesn`t exist')

    context = {'page':page, 'form': form}
    return render(request, 'login.html',context)

def LogoutUser(request):
    logout(request)
    return redirect('home')

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html", {'posts':posts})

@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None,)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('blog')
    return render(request, 'post_creation.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    title = str(post.text)[:30]
    number_of_posts = Post.objects.filter(author=post.author).count()
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'title': title,
        'number_of_posts': number_of_posts,
        'form': form,
        'comments': comments
    }
    return render(request, 'post_detail', context)

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and request.user not in users_in_stuff:
        return redirect('post', post_id=post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if form.is_valid():
        form.save()
        return redirect('post', post_id=post_id)
    context = {
        'post': post,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'post_creation.html', context)

def post(request, post_id):
    post = Post.objects.get(id = post_id)
    post_comments = Comment.objects.filter(post=post.id)

    if request.user in users_in_stuff:
        permission_check = True
    else:
        permission_check = False

    if request.method == 'POST':
        comment = Comment.objects.create(
            author = request.user,
            post = post,
            text = request.POST.get('body')
        )
        return redirect('post',post_id=post.id)
    context = {
        'post':post,
        'post_comments':post_comments,
        'permission_check': permission_check
        }
    return render(request, 'post_detail.html', context)

def create_feedback(request):
    if request.method == post:
        feedback = Feedback.objects.create(name=request.POST.Name, email=request.POST.Email, text=request.POST.Message)
        return redirect('thanks')
    return render(request, "thanks.html")

def thanks(request, pk):
    feedback = Feedback.objects.get(id=pk)
    context = { 'feedback' : feedback }
    return render(request, 'thanks.html', context)

def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('thanks', pk=feedback.id)
    context = {'form':form}
    return render(request,'feedback.html', context)