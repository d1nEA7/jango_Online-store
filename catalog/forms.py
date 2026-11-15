from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control",})



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name_category", "description_category"]
        description_category = forms.CharField(widget=forms.Textarea)

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'description_product', 'category', 'image_product', 'price_product']


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "").lower()
        description = cleaned_data.get("description", "").lower()

        forbidden_words = [
            "казино",
            "биржа",
            "криптовалюта",
            "крипта",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in name or word in description:
                raise ValidationError(f"Слово '{word}' запрещено к использованию")

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной или равной 0")
        return price


