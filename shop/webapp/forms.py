from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data['product']
        description = cleaned_data['description']
        if product == description:
            raise ValidationError("Text of description should not duplicate it's product text")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
