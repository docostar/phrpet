from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Dr. xyz',
            'id': 'name'
        })
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'info.example@.com',
            'id': 'email'
        })
    )
    message = forms.CharField(
        required=True, 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Opinion...',
            'id': 'message'
        })
    )

