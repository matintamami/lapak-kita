from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "scout_app/index.html")

def product_list(request):
    return render(request, "scout_app/product.html")

def product_detail(request):
    return render(request, "scout_app/product-detail.html")

def product_cart(request):
    return render(request, "scout_app/shoping-cart.html")

def mitra(request):
    return render(request, "scout_app/blog.html")

def mitra_detail(request):
    return render(request, "scout_app/blog-detail.html")

def about(request):
    return render(request, "scout_app/about.html")

def help(request):
    return render(request, "scout_app/contact.html")