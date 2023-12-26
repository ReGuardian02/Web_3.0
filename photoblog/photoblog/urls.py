from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from based import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('links/', views.links, name='links'),
    path('site/', views.site, name='site'),
    path('feedback/', views.feedback, name='feedback'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.log_in, name='login'), 
    path('logout/', views.LogoutUser, name='logout'),
    path('post_create/', views.post_create, name='post_create'),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path("posts/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('meeedia/', views.meeedia, name='meeedia'),
    path('thanks/<int:pk>/', views.thanks, name='thanks'),
    path('create_feedback/', views.create_feedback, name='create_feedback'),
    path('shop/', views.shop, name='product_shop'),
    path('product_create/', views.product_create, name='product_create'),
    path("product/<int:product_id>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:product_id>/edit/", views.product_edit, name="product_edit"),
    path('products/<int:product_id>/', views.product, name='product'),
    path('product/<int:product_id>/', views.product, name='product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
