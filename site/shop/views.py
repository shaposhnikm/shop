from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string

from .models import Product
from .models import User
from .models import Category
from .forms import ProductForm
from .forms import OrderForm

from shop.models import BlogPost

def archive(request):   
    posts = BlogPost.objects.all()   
    t = loader.get_template("archive.html")   
    c = Context({"posts": posts })   
    return HttpResponse(t.render(c))



def index(request):
	queryset = Product.objects.all()
	top = Product.objects.filter(best=True)
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	context={
		'items': items,
		'best': top

	}
	return render_to_response('shop/index.html', context)


def alll(request):
	queryset = Product.objects.all()
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	context={
		'items': items,

	}
	return render_to_response('shop/alll.html', context)

def top(request):
	queryset = Product.objects.filter(best=True)
	template = 'shop/top.html'

	context={
		'best': queryset
	}
	return render(request, template, context)

def list1(request):
	queryset = Product.objects.filter(category_id=1)
	template = 'shop/list1.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'list1': queryset
	}
	return render(request, template, context)


def list2(request):
	queryset = Product.objects.filter(category_id=2)
	template = 'shop/list2.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'list2': queryset
	}
	return render(request, template, context)


def list3(request):
	queryset = Product.objects.filter(category_id=3)
	template = 'shop/list3.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'list3': queryset
	}
	return render(request, template, context)


def list4(request):
	queryset = Product.objects.filter(category_id=4)
	template = 'shop/list4.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'list4': queryset
	}
	return render(request, template, context)


def list5(request):
	queryset = Product.objects.filter(category_id=5)
	template = 'shop/list5.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'list5': queryset
	}
	return render(request, template, context)



def order(request):
	context={
	}
	return HttpResponse(render_to_string('shop/korzina.html',context))



def detail(request, product_id):
	item = get_object_or_404(Product, id=product_id)
	template = 'shop/detail.html'
	context={
		'items': item
	}
	
	return render(request,template,context)

def metal(request, items_metal_id):
	queryset=Product.objects.filter(metal_id=items_metal_id)
	template = 'shop/metal.html'
	paginator = Paginator(queryset, 9) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context={
		'items': queryset
	}
	
	return render(request,template,context)

def create(request):
	template = 'shop/create.html'
	form = OrderForm(request.POST or None)
	context= {'form': form}

	if request.method == 'POST':
		print(request.POST)
	
		if form.is_valid():
			item = form.save()
			item.save()
		
			return redirect('alll')

	else:
		context= {'form': form}

	return render(request,template,context)



def delete_item(request, item_id):
    template='shop/delete_item.html'
    item = get_object_or_404(Item, id = item_id)    
    if request.method=='POST' and request.POST['action'] == "Yes":
        item.delete()
        return redirect('index')
    elif request.method=='POST' and request.POST['action'] == "No":
        return redirect('detail', item_id=item.id)
    return render(request, template, {'object':item})


