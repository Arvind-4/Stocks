from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import StocksForm
from .information import (get_search_data,
						get_price_information,
						get_meta_data,
						list_of_crypto_data,
						get_stocks_fundementals)

# Create your views here.

def home_page_view(request, *args, **kwargs):
	form = StocksForm(request.POST or None)
	if form.is_valid():
		stock_name = request.POST['name']
		stock_name = stock_name.lower()
		if stock_name:
			return HttpResponseRedirect(stock_name)
	context = {
		'form': form,
	}
	return render(request, 'stocks/home_page.html', context=context)

def redirect_page_stocks(request, stock_name):
	data = get_search_data(stock_name)
	if len(data) == 0:
		return redirect('/error')
	else:
		context = {
			'data': data,
		}
		return render(request, 'stocks/ticker.html', context=context)

def redirect_price_view(request, stock_code):
	data = get_price_information(stock_code)
	meta_data = get_meta_data(stock_code)
	context = {
		'data': data,
		'meta_data': meta_data,
		'stock_code': stock_code,
	}
	return render(request, 'stocks/table.html', context=context)

def crypto_view(request):
	return render(request, 'stocks/cryto_view.html', context={})

def crypto_list_view(request):
	data = list_of_crypto_data()
	context = {
		'data': data,
	}
	return render(request, 'stocks/cryto_list_view.html', context=context)

def stocks_details(request):
	data = get_stocks_fundementals()
	data = data[::-1]
	context = {
		'data': data,
	}
	return render(request, 'stocks/stocks_details.html', context=context)

def error_view(request):
	return render(request, 'stocks/error.html', context={})

def about_view(request):
	return render(request, 'stocks/about.html', context={})