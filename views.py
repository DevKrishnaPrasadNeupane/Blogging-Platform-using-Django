from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_list(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request, 'gallery/index.html',context)

def product_details(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request,'gallery/product_details.html',context)


def delete(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":  # Only delete if the form is submitted
        product.delete()
        return redirect('product_list')  # Redirect after deleting

    # Render the confirmation page
    context = {'product': product}
    return render(request, 'gallery/delete.html', context)


def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'gallery/edit.html', {'form': form})