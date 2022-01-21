from django import forms

from products.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     slogan = forms.TextInput()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'slogan'
        ]

    def clean_slogan(self):
        data = self.cleaned_data.get('slogan')
        if len(data) < 2:
            raise forms.ValidationError("This field must be more than 2 characters long.")
        return data