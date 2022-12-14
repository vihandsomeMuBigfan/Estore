from django.shortcuts import render
from store.models import *


# Create your views here.
def trang_chu(request):
    # Slider
    sliders = Slider.objects.all()

    # Brand
    brands = Brand.objects.all()

    # Thiết bị gia đình
    subcategories_tbgd = SubCategory.objects.filter(category=1).values_list('id')
    
    list_subcategory_id_tbgd = [subcategory_id[0] for subcategory_id in subcategories_tbgd]

    products_tbgd = Product.objects.filter(subcategory__in=list_subcategory_id_tbgd).order_by('-public_day')

    dem = 0
    if request.COOKIES.get('so_lan_truy_cap') != None:
        dem = int(request.COOKIES.get('so_lan_truy_cap')) + 1





    response = render(request, 'store/index.html', {
        'sliders': sliders,
        'brands': brands,
        'products_tbgd': products_tbgd,
    })

    response.set_cookie('so_lan_truy_cap', dem)

    return response

def trang_chu_2(request):
    # Slider
    sliders = Slider.objects.all()

    # Brand
    brands = Brand.objects.all()

    # Thiết bị gia đình
    subcategories_tbgd = SubCategory.objects.filter(category=1).values_list('id')
    list_subcategory_id_tbgd = [subcategory_id[0] for subcategory_id in subcategories_tbgd]
    products_tbgd = Product.objects.filter(subcategory__in=list_subcategory_id_tbgd).order_by('-public_day')

    dem = 0
    if request.COOKIES.get('so_lan_truy_cap') != None:
        dem = int(request.COOKIES.get('so_lan_truy_cap')) + 1





    response = render(request, 'store/index.html', {
        'sliders': sliders,
        'brands': brands,
        'products_tbgd': products_tbgd,
    })

    response.set_cookie('so_lan_truy_cap', dem)

    return response

def san_pham(request, pk):
    danh_muc = SubCategory.objects.all()
    # list1 = danh_muc.values_list()
    # for i in list1:
        
    brand = Brand.objects.order_by('name')
    if pk == 0:
        all_product = Product.objects.all()

    else:
        all_product = Product.objects.filter(subcategory=pk)
        
    return render(request, 'store/product_list.html', {
        'all_products': all_product,
        'danh_muc': danh_muc,
        'brands': brand,
    })

def detail_sp(request):
    return render(request, 'store/product_detail.html')