from django import forms
from blogapp.models import Post, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': "textinputclass"}),
            'text': forms.Textarea(attrs={'class': 'edittextarea'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'author style'}),
            'text': forms.Textarea(attrs={'class': 'comments style'})
        }
