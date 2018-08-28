from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
#from .pre_processing import Pre_processing as pp
from .main2 import Classification as da
from .tweeturl import tweet
from urllib.parse import urlparse
import re

def is_absolute(url):
    return bool(urlparse(url).netloc)

def index(request):
	context = {
	}
	# da.cross_validation()
	# da.get_relevance('')
	return render(request,'Home.html', context)


def search_post(request):
	ctx ={}
	ctx.update(csrf(request))
	if request.POST:
		reg = r"http.*"
   
		if is_absolute(request.POST['q']):
			print('INI HASILNYA')
			isi = tweet.get_tweet(request.POST['q'])
			ctx['isi'] = re.sub(reg, '', isi)
		else:
			ctx['isi'] = request.POST['q']
		print(ctx['isi'])
		hasil = da.classify(ctx['isi'])
		ctx['hsl'] = hasil
		r = da.get_relevance(ctx['isi'])
		ctx['titl'] = []
		ctx['url'] = []
		ctx['sim'] = []
		ctx['content'] = r
		
	return render(request, 'Hasil.html', ctx)

	