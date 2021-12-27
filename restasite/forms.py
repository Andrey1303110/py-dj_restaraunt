from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form-control valid'}
        )
    )
    email = forms.EmailField(
        min_length=8,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш Email', 'class': 'form-control valid'}
        )
    )
    message = forms.CharField(
        min_length=20,
        max_length=350,
        widget=forms.Textarea(
            attrs={'placeholder': 'Введите сообщение', 'cols': 30, 'rows': 9, 'class': 'form-control w-100'}
        )
    )
