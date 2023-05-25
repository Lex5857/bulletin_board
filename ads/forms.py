from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import Ads, Responses, Author


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['heading', 'text', 'author', 'category']

        def clean(self):
            cleaned_data = super().clean()
            text = cleaned_data.get("text")
            if text is not None and len(text) < 20:
                raise ValidationError({
                    "text": "Описание не может быть менее 20 символов."
                })

            return cleaned_data


class ResponsesForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['text', 'ads', 'author']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Описание не может быть менее 20 символов."
            })

        return cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_active']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nickname',
                  'email',
                  'surname',
                  'name',
                  'middle_name',
                  'birthday',
                  'gender',
                  'user'
                  ]
