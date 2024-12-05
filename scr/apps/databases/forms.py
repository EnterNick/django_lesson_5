from django import forms

from .models import Post, Comments


class CreatePostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'description', 'class': 'form__input'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title', 'class': 'form__input'}))
    template_name = 'databases/add_form.html'

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]

    def save(self, commit=True):
        self.instance.author = self.initial['request'].user
        return super().save(commit)


class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'content', 'class': 'form__input'}))
    template_name = 'databases/add_comment.html'

    class Meta:
        model = Comments
        fields = [
            'content',
        ]

    def save(self, commit=True):
        try:
            self.instance.author = self.initial['request'].user
            self.instance.post = self.initial['post']
        except ValueError:
            pass
        return super().save(commit)
