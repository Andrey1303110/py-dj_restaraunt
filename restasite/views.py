from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from restasite.forms import ContactForm
from restasite.models import MenuItem


def index(request):
    menu_main = MenuItem.objects.filter(type__exact='main').order_by('price')
    menu_drink = MenuItem.objects.filter(type__exact='drink').order_by('price')
    menu_other = MenuItem.objects.filter(type__exact='other').order_by('price')
    menu_all = MenuItem.objects.order_by('price')
    context = {'menu_main': menu_main, 'menu_drink': menu_drink, 'menu_other': menu_other, 'menu_all': menu_all}
    return render(
        request,
        'index.html',
        context=context
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contacts.html',
        context=context
    )


def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {
        'name': name,
        'email': email,
        'message': message
    }
    subject = 'Сообщение от пользователя'
    from_email = 'mysite@gmail.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['andrey1303110@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
