from django import forms

class postBlog(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    title = forms.CharField(max_length=100)
    data = forms.CharField(max_length=300)
    # pub_date = forms.DateTimeField('date published')