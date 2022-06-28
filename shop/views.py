from django.shortcuts import redirect, render
from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from django.views import View


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:product_list")
        return render(request, 'shop/home.html')

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list3.html',
                  {'category':category,
                   'categories':categories,
                   'products':products})
    
def product_detail(request,id,slug):
    product = get_object_or_404(Product, id=id,slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    
    return render(request,'shop/product/detail.html',
                  {'product':product,
                   'cart_product_form':cart_product_form})
    

def about_us(request):

    return render(request, 'shop/about.html')


