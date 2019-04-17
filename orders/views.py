from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import AddOrder, AddEmail, AddItem
from .models import Order, Email, Item

# Create your views here.

def ordersindex(request):
    order_lst = Order.objects.select_related('email').select_related('item').order_by('-order_time')
    order_dckt = {'order':order_lst}

    form = AddOrder()
    order_dckt['form'] = form

    EForm = AddEmail()
    order_dckt['EForm'] = EForm

    IForm = AddItem()
    order_dckt['IForm'] = IForm

    if request.method == 'POST':
        form = AddOrder(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj = form.save()

            email = Email.objects.filter(id=request.POST['email'])
            email_subject = email.values('email_subject')[0]['email_subject']
            email_address = email.values('email_address')[0]['email_address']
            item = Item.objects.filter(id=request.POST['item'])
            item_model = item.values('item_model')[0]['item_model']
            item_type = item.values('item_type')[0]['item_type']

            message = "Dzień dobry,\n\nChciałbym zamówić " + request.POST['item_quantity'] + "x " + item_type + " " + item_model + " na naszą Centralę w Zamościu.\nDziękuję i pozdrawiam,\n\n--\nDawid Kuchciński\nDział Wsparcia Technicznego\nTel. 52 372 54 17\nTel. 52 372 54 67\nHurtownia Motoryzacyjna Gordon\nZamość ul. Poznańska 62, 89-200 Szubin\nwww.gordon.com.pl"
            send_mail(email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email_address],
            fail_silently=False)

            return redirect('/zamowienia')

        else:
            form = AddEmail(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj = form.save()
                return redirect('/zamowienia')
            
            else:
                form = AddItem(request.POST)

                if form.is_valid():
                    obj = form.save(commit=False)
                    obj = form.save()
                    return redirect('/zamowienia')

    return render(request, 'orders/orders.html', context = order_dckt)