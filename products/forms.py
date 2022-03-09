from django import forms
from django.http import Http404
from products.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     slogan = forms.TextInput()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'category_name',
            'price',
            'slogan',
            'image',
            'media',
        ]

    def clean_slogan(self):
        data = self.cleaned_data.get('slogan')
        if len(data) < 2:
            raise forms.ValidationError("This field must be more than 2 characters long.")
        return data

    def download_order_media(request, *args, **kwargs):
        qs = Product.objects.all()
        product_obj = qs.first()
        if not product_obj.media: raise Http404

        
