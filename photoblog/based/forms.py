from django import forms
from .models import Post, Comment, Feedback, Product, Chat
from django.forms import ModelForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) < 10:
            raise forms.ValidationError(
                f"Длинна поста должна быть не менее 10 символов!"
            )

        return data


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'text', 'image', 'tags')


    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) < 10:
            raise forms.ValidationError(
                f"Длинна описани должна быть не менее 10 символов!"
            )

        return data

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ["text"]

    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) < 3:
            raise forms.ValidationError(
                "Длинна сообщения должна быть не менее 3 символов!"
            )
        return data

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]

    def clean_text(self):
        data = self.cleaned_data["text"]

        if len(data) < 5:
            raise forms.ValidationError(
                "Длинна комментария должна быть не менее 5 символов!"
            )
        return data

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'