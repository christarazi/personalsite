from django.shortcuts import render
from django.http import HttpResponse
from fortune.models import Fortune
import random
from django.template import RequestContext, loader
#from flickrapi import *

#from urllib.request import urlopen
from urllib2 import urlopen
from bs4 import BeautifulSoup
import random
# Create your views here.

keyword_list = ['cat', 'dog', 'animals', 'sports', 'people', 'cool', 'space']

def findAnImageFromFlickrWithKeyword(keyword):
  debug = False
  response = urlopen('http://api.flickr.com/services/feeds/photos_public.gne?tags=' + keyword + '&lang=en-us&format=rss_200').read( ).decode('utf-8')

  soup = BeautifulSoup(response, 'lxml')

  image_url_list = []

  for item in soup.find_all('item'):
    author_list = list(item.find_all('author'))
    media_list = list(item.find_all('media:content'))
    title_list = list(item.find_all('media:title'))
    if len(author_list) == len(media_list):
      for i in range(len(author_list)):
        #image_url_list.append((media_list[i]['url'], author_list[i]['flickr:profile'], title_list[i].string))
        image_url_list.append((media_list[i]['url']))
  return random.choice(image_url_list)

'''
apiKey = u'3063b7003db59b5d27c7f0bbeb9aca6b'
apiSecret = u'73e11cd05f8959cf'

flickr = FlickrAPI(apiKey, apiSecret)

def getFlickrImage():
	pictures = flickr.photos.getRecent(per_page=100)

	for i in pictures:
		l = i.getchildren()
		randPic = random.randint(0,99)
		photo = l[randPic]
		farmID = str(photo.get('farm'))
		ID = str(photo.get('id'))
		serverID = str(photo.get('server'))
		secretID = str(photo.get('secret'))

		fullPathImage = str("https://farm" + str(farmID) + ".staticflickr.com/" + str(serverID) + "/" + str(ID) + "_" + str(secretID) + ".jpg")

	return fullPathImage
'''

def home(request):
	template = loader.get_template('fortune/home.html')
	context = RequestContext(request, {})

	return HttpResponse(template.render(context))

def index(request):
	rn = random.randint(0,14334)
	results = Fortune.objects.filter(id=rn)
	#aphorism = results[0].aphorism
	template = loader.get_template('fortune/index.html')
	context = RequestContext(request, {'aphorism': results[0].aphorism, 'fullPathImage': findAnImageFromFlickrWithKeyword(random.choice(keyword_list)),})
	# template loads the html page and looks for the braces.
	# context then fills the braces with the information provided by the dictionary,
	# ex. {'aphorism': ...}
	   
	return HttpResponse(template.render(context))

def idAphorism(request, fortuneID):
    # if user types a large value, set it to 42
    if int(fortuneID) > 14334:
    	fortuneID = 42
    results = Fortune.objects.filter(id=fortuneID)
    template = loader.get_template('fortune/index.html')
    context = RequestContext(request, {'aphorism': results[0].aphorism, 'fullPathImage': findAnImageFromFlickrWithKeyword(random.choice(keyword_list)),})

    return HttpResponse(template.render(context))

def short(request):
    #Fortune.objects.filer(size__lt=140)
    '''
	while True:
		rn = random.randint(0,14334)
		results = Fortune.objects.filter(id=rn)
		if(len(results[0].aphorism) < 140):
			break
    '''
    results = Fortune.objects.filter(size__lt=140)
    template = loader.get_template('fortune/index.html')
    context = RequestContext(request, {'aphorism': results[0].aphorism, 'fullPathImage':findAnImageFromFlickrWithKeyword(random.choice(keyword_list)), 'size': results[0].size},)

    return HttpResponse(template.render(context))

def startrek(request):
	rn = random.randint(14132,14334)			# this is the range of startrek aphorisms. 
	results = Fortune.objects.filter(id=rn)
	template = loader.get_template('fortune/index.html')
	context = RequestContext(request, {'aphorism': results[0].aphorism, 'fullPathImage': findAnImageFromFlickrWithKeyword(random.choice(keyword_list)), 'size': results[0].size},)

	return HttpResponse(template.render(context))
