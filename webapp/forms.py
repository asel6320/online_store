from decimal import Decimal
from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets
from django.core.exceptions import ValidationError
from webapp.models import Product

class ProductForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        if title and description and title == description:
            raise ValidationError("The title and description cannot be the same.")
        return cleaned_data

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'remainder', 'image_url']
        error_messages = {
            "title": {
                "required": "This field is required.",
            },
            "price": {
                "invalid": "Input correct price.",
            }
        }
        widgets = {
            'description': widgets.Textarea(attrs={'cols': 20, "rows": 5}),
        }
        validators = {
            'price': [MinValueValidator(Decimal('0.01'))],
            'remainder': [MinValueValidator(1)],
        }


class SearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)