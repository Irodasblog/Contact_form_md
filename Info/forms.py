from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = '__all__'

        labels = {
            'first_name': 'Ism',
            'last_name': 'Familiya',
            'phone': 'Telefon raqam',
            'email': 'Email manzil',
            'message': 'Xabaringiz',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ismingiz'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Familiyangiz'
            }),

            'phone': forms.TextInput(attrs={
                'placeholder': '+998 90 123 45 67',
                'type': 'tel'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'example@gmail.com'
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Xabaringizni yozing...',
                'rows': 4
            }),
        }