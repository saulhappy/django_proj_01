import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type
from django import forms
from django.http import Http404, HttpResponse
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
        qs = Product.objects.filter(media__isnull=False)
        product_obj = qs.first()

        if not product_obj.media: raise Http404
        
        media_path = product_obj.media.path
        media_path = pathlib.Path(media_path)
        ext = media_path.suffix
        pk = product_obj.pk
        file_name = f"media_{pk}{ext}"

        if not media_path.exists(): raise Http404

        with open(media_path, 'rb') as f:
            wrapper = FileWrapper(f)
            content_type = 'application/force-download'
            guessed_media_type = guess_type(media_path)[0]
            if guessed_media_type:
                content_type = guessed_media_type
            response =  HttpResponse(wrapper, content_type=content_type)

        return HttpResponse


        
