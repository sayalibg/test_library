"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views
from user import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.home, name="home_page"),
    path('showbook/', views.show_books, name="book_page"),
    path('updatebook/<int:id>', views.update_book, name="update_page"),
    path('deletebook/<int:pk>', views.delete_book, name="delete_page"),
    path('softdeletebook/<int:pk>', views.soft_delete_book, name="soft_delete_page"),
    path('inactivebook/', views.inactive_book, name="inactive_book_page"),
    path('restorebook/<int:pk>', views.restore_book, name="restore_book_page"),
    # path('book_form/', views.book_form, name="book_form"),



# Users Url

    path('register/', user_views.register_users, name="register"),
    path('login/', user_views.login_user, name="login_user"),
    path('logout/', user_views.logout_user, name="logout_user"),
    path('index/', user_views.index, name="index"),
    path('login-cbv/', user_views.LoginPageView.as_view(), name="LoginPageView"),
    path('logout-cbv/', user_views.LogoutView.as_view(), name='LogoutView'),   # no need to define class in views.py



# classbased views url
    # path('cbv/', views.NewView.as_view(), name="cbv"),
    path('cbv-book/', views.BookCreate.as_view(), name="cbv-book"),
    path('retrieve/', views.BookRetrieve.as_view(), name = 'BookRetrieve')  ,
    path('retrieve/<int:pk>', views.BookDetail.as_view(), name = 'BookDetail'),  
    path('update/<int:pk>', views.BookUpdate.as_view(), name = 'BookUpdate'), 
    path('delete/<int:pk>/', views.BookDelete.as_view(), name = 'BookDelete') ,
    path('feedback/', views.FeedbackFormView.as_view(), name = 'Feedback') ,
    path('template/', views.TemplateView.as_view(), name = 'template') 





]
