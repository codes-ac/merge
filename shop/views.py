from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
import json

# from math import ceil


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # if n%4==0:
    #     nslides = n//4
    # else:
    #     nslides=n//4+1

    # nslides = n//4+ceil((n/4)-(n//4))    #ceil : least integer function
    # params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products}

    # allprods = [[products, range(1, nslides), nslides],
    #             [products, range(1, nslides), nslides]]

    allprods = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}  # set comprehension
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        if n % 4 == 0:
            nslides = n // 4
        else:
            nslides = n // 4 + 1
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('Item_Json', '')
        name = request.POST.get('Fname', '') + " " + request.POST.get('Lname', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        address = request.POST.get('Address1', '') + " " + request.POST.get('Address2', '')
        city = request.POST.get('City', '')
        state = request.POST.get('State', '')
        zip_code = request.POST.get('Zip_Code', '')
        amount = request.POST.get('amount', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city,
                      state=state, zip_code=zip_code, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed!")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')



def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', ' ')
        email = request.POST.get('email', ' ')
        try:
            order = Order.objects.filter(order_id= orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id= orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "items_json": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "No Item"}')

        except Exception as e:
            return HttpResponse('{"status":"Error"}')


    return render(request, 'shop/tracker.html')
