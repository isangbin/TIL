from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '댓글 ',
        widget = forms.TextInput(
            attrs = {
                'class' : 'comment-content',
                'row': 1,
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)