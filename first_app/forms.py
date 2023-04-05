from django import forms
from .models import Book


# django form using model then use ModelForm
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         # fields = "__all__"   # all field will converted into form field
#         exclude = ('is_active',)    # used to remove field
#         fields = ("name", "author", "qty")


# django form without using model then use Forms

# class BookForm(forms.Form):
   
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(
#                      help_text = "Enter 6 digit roll number"
#                      )
#     password = forms.CharField(widget = forms.PasswordInput())


# class BookForm(forms.Form):
#     Book_Name = forms.CharField(max_length=200)
#     Book_Author = forms.CharField(max_length=100)
#     Book_Quantity = forms.IntegerField()


class FeedbackForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Contact_Details = forms.IntegerField()
    Feedback = forms.CharField(max_length=250)


