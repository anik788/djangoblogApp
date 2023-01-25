from django import forms
from blog.models import Post


# class PostCreateForm(forms.Form):
#     title = forms.CharField(max_length=500)
#     body = forms.CharField(widget=forms.Textarea, required=False)
#     status = forms.CharField(required=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('author',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('categories',)


# class PostUpdateForm(forms.Form):
#     title = forms.CharField(max_length=500, required=False)
#     body = forms.CharField(widget=forms.Textarea, required=False)
#     status = forms.CharField(required=False)
