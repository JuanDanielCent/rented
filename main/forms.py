from django import forms
from .models import Property, Property_lease

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'parking', 'department']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a desription'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a department'})
        }


class LeaseForm(forms.ModelForm):
    class Meta:
        model = Property_lease
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'parking', 'department']
        fields = ['title', 'description', 'price', 'bedrooms', 'bathrooms', 'parking', 'department']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a desription'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'parking': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a department'})
        }


class CategoriaForm(forms.Form):
    CATEGORIA_CHOICES = [
        ('venta', 'Venta'),
        ('alquiler', 'Alquiler'),
    ]
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, widget=forms.RadioSelect)