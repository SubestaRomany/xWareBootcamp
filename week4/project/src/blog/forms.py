from django import forms
from .models import Post
class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']