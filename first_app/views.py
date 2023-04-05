from django.shortcuts import render,HttpResponse, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    
    if request.method == "POST":
        # print(request.POST.get("cars"))  # for single dropdown value
        # print(request.POST.getlist("car"))  # for multiple dropdown value
        bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        author = request.POST.get("book_author")
        price = request.POST.get("book_price")
        quantity = request.POST.get("book_quantity")
        is_pub = request.POST.get("book_published")
        # print(is_pub)
        # print(name, author, price, quantity, is_pub)
        if is_pub == "yes":
            is_pub = True
        else:
            is_pub = False
        print(bid)
      
        if not bid:

            Book.objects.create(name=name, author=author, price=price, qty=quantity, is_published = is_pub)   # book object created
        else:
            book_obj1 = Book.objects.get(id = bid)
            book_obj1.name = name
            book_obj1.author = author
            book_obj1.price = price
            book_obj1.qty = quantity
            book_obj1.is_published = is_pub
            book_obj1.save()
        # print(request.POST)

        # <QueryDict: {'csrfmiddlewaretoken': ['cLssuwcYjmyaQuqjHQNkS9KdvnFUw7KuaVQsHZsg2OG6k72YNZWtvlIBb4MakU8M'], 'book_name': ['abc'], 'book_author': ['abc'], 'book_price': ['4545'], 'book_quantity': ['5'], 'book_published': ['on'], 'create_book': ['Create Book']}>
        # return HttpResponse("Sucess")
        return redirect("home_page")
       
    elif request.method == "GET":
        # print(request.GET)   #  <QueryDict: {'name': ['abc']}> query params
        return render(request, "home.html")
        # return render(request, "home.html", context={"per_name" : "SHIVA"})


def show_books(request):
    return render(request, "show_book.html", {"all_books" : Book.objects.filter(is_active = True), "active": True})

def update_book(request, id): 
    book_obj = Book.objects.get(id=id)
    return render(request, "home.html", context={"single_book": book_obj})        

def delete_book(request, pk):    # hard delete--- directly deleted from database
    Book.objects.get(id = pk).delete()
    return redirect("book_page")


def soft_delete_book(request, pk):    # soft delete--- make active status false
    bk_obj = Book.objects.get(id = pk)
    bk_obj.is_active = False
    bk_obj.save()
    return redirect("book_page")

def inactive_book(request):
    return render(request, "show_book.html", {"all_books" : Book.objects.filter(is_active = False), "inactive": True} )

def restore_book(request, pk):
    restr_bk = Book.objects.get(id = pk)
    restr_bk.is_active = True
    restr_bk.save()
    return redirect("book_page")


# from  first_app.forms  import BookForm

# def book_form(request):
#     return render(request, "book_form.html", {"form" : BookForm()})


# simpleisbetterthancomplex

# Django Class Based Generic Views

# from django.views import View  

# class NewView(View):
#     def get(self, request):
#         return HttpResponse('get response')

#     def post(self, request):
#         return HttpResponse('post response')

#     def put(self, request):   # update
#         return HttpResponse('put response')

#     def patch(self, request):   # partial update
#         return HttpResponse('patch response')

#     def delete(self, request):
#         return HttpResponse('delete response')

# CRUD -----------------------------------------

from django.views.generic.edit import CreateView  
  
class BookCreate(CreateView):  
    model = Book 
    fields = '__all__'  
    success_url = '/cbv-book/' # reverse_lazy('Bookcreate') 

# There are two kinds of retrieve view - ListView and DetailView. We will use the ListView which refers to a view to display
#  multiple instances of a table in database. We only need to specify the model name which apply ListView, 
#  Class based ListView will automatically do the job for us. 
# To retrieve the data, we need to create the 'app_name/modelname_list.html' file.


# ----------------------------------- LIST VIEW -----------------------------------------

from django.views.generic.list import ListView

class BookRetrieve(ListView):
    model = Book
    context_object_name = 'all_books'
    # queryset = Book.objects.filter(is_active = 0) # by default queryset is object.all() --- to change we use queryset


# ------------------------------------- DETAIL VIEW ------------------------------------
from django.views.generic.detail import DetailView  
  
class BookDetail(DetailView):  
    model = Book  

# ------------------------------- UpdateView ----------------------------------------------
# UpdateView allows to update the particular instance of the table from
#  the database with some more details. This view is used to alter the entries in the database

from django.views.generic.edit import UpdateView  
class BookUpdate(UpdateView):  
    model = Book  
    fields = '__all__'
    success_url = '/cbv-book/'


# --------------------------- DELETE VIEW ------------------------------------------
from django.views.generic.edit import DeleteView  
class BookDelete(DeleteView):
    model = Book
    success_url = '/cbv-book/'



# --------------------------------- FORM VIEW -------------------------------------------
from django.views.generic.edit import FormView
from first_app.forms import FeedbackForm

class FeedbackFormView(FormView):
    template_name = 'first_app/feedback.html'
    form_class = FeedbackForm
    success_url = '/cbv-book/'


# _----------------------------- TEMPLATE VIEW ------------------------

from django.views.generic import TemplateView
from django.core.exceptions import ImproperlyConfigured

# ----- this is giving error----------

# class Template(TemplateView):
#     template_name = 'F:\B8\B8_Django\library\first_app\templates\first_app\home.html'
#     extra_context = {"Name" : "Sayali"}

#     def get_template_names(self):
#         if self.template_name is None:
#             raise ImproperlyConfigured("TemplateResponseMixin requires either a definition of ")
#         else:
#             return [self.template_name]
