from django import forms
from.models import Product,Category


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['image','name','category','price','description']


        widgets={
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'discription':forms.Textarea(attrs={'class':'form-control'})
            #'is_published':forms.Select(attrs={'class':'form-control'}),
        }




class ByProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='By-Product Name')

 