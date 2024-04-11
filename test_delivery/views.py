from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.forms import formset_factory,modelformset_factory
from .forms import *
def add_store_item(request):
    item_formset=formset_factory(itemForms)
    if request.method=='POST':
        store_form=storeForms(request.POST)
        formset=item_formset(request.POST)
        if store_form.is_valid():
            store=store_form.save()
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data: 
                    item=form.save(commit=False)
                    item.store=store
                    item.save()
        return redirect(request,'manage_store')
    else:
        store_form=storeForms
        formset=item_formset()
        return render(request,'add_store_item.html',{'store_form':store_form,'item_formset':formset})
    
def add_CMD(request):
    if request.method=='GET':
        stores=Store.objects.all()
        items=Items.objects.all()
        return render(request,'cmd.html',{'stores':stores,'items':items})
    else:
        store_id = request.POST.get("store")
        cmd=CMD()
        cmd.store=Store.objects.get(pk=store_id)
        cmd.status=1
        cmd.save()
        for key in request.POST.keys():
            if key.startswith('counter_'):
                item_id=key.split('_')[1]
                cmd_line=CMD_line()
                item=Items.objects.get(pk=item_id)
                cmd_line.item=item
                cmd_line.quantity=int(request.POST.get(key)[0])
                cmd.total+=cmd_line.quantity*item.price
                cmd_line.cmd=cmd
                cmd_line.save()
        cmd.save()
        return redirect('menu')
    
def get_items(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id')

        if store_id == '-':
            # If no store is selected, return an empty list
            items = []
        else:
            # Retrieve items for the selected store
            items = Items.objects.filter(store_id=store_id).values('id','name')

        # Convert items queryset to a list of dictionaries
        items_list = list(items)

        return JsonResponse(items_list, safe=False)

def edit_store_item(request, store_id):
    store = Store.objects.get(pk=store_id)
    ItemFormSet = modelformset_factory(Items, form=itemForms, extra=0)
    
    if request.method == 'POST':
        store_form = storeForms(request.POST, instance=store)
        formset = ItemFormSet(request.POST, queryset=Items.objects.filter(store=store))
        
        if store_form.is_valid() and formset.is_valid():
            store = store_form.save()
            for form in formset:
                instance=form.save(commit=False)
                if  instance.store_id is None:
                    instance.store=store
                instance.save()
            return redirect('manage_stores')
    else:
        store_form = storeForms(instance=store)
        formset = ItemFormSet(queryset=Items.objects.filter(store=store))
    
    return render(request, 'edit_store_item.html', {'store_form': store_form, 'item_formset': formset})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_clients')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('manage_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})

def manage_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'manage_driver.html', {'drivers': drivers})

def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_drivers')
    else:
        form = DriverForm()
    return render(request, 'add_driver.html', {'form': form})

def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('manage_drivers')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'edit_driver.html', {'form': form})

def menu(request):
    return render(request, 'menu.html')

def manage_clients(request):
    clients = Client.objects.all()
    return render(request, 'manage_client.html', {'clients': clients})

def manage_stores(request):
    stores = Store.objects.all()
    return render(request, 'manage_store.html', {'stores': stores})


# Create your views here.
