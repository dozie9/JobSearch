from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(required = True)

    class Meta:
        model = Post
        fields = ('post',)
