from django.shortcuts import render
from django.template.loader import get_template
import random
from django.http import HttpResponse, Http404
from mysite.models import Product
def about(request):
	template = get_template('about.html')
	quotes = ["時光腳步輕，年歲不饒人","智者順時而謀，愚者逆理而動","訓教不嚴師之惰，學問無成子之罪","言不能亂髮，筆不能妄動"]
	html = template.render({'quote':random.choice(quotes)})
	return HttpResponse(html)


def disp_detail(request,sku):
	
	try:
		p = Product.objects.get(sku=sku)
	except Product.DoesNotExist:
		raise Http404("Not find items")

	template = get_template('disp.html')
	html = template.render({'product':p})
	return HttpResponse(html)

def listing(request):
	products= Product.objects.all()
	template = get_template('list.html')
	html = template.render({'products':products})
	return HttpResponse(html)