from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django import template

# Create your views here.

def home(request):
	posts = Post.objects.filter(site=1).order_by('-published_date')
	viewName = "home.html"
	currPageClassSelector = ["", "", ""]
	currPage = 0
	# This string will be used to append to tab element's class that is currently being viewed, so we can activate the css.
	currPageClassSelector[currPage] = "current-menu-item current_page_item menu-item-home"

	# We return a rendered home.html with our model "posts".
	return render(request, 'base.html', {"posts": posts, "currPageClassSelector": currPageClassSelector, "viewName": viewName})

def about(request):
	posts = Post.objects.filter(site=2).order_by('published_date')
	viewName = "about.html"
	currPageClassSelector = ["", "", ""]
	currPage = 1
	currPageClassSelector[currPage] = "current-menu-item current_page_item menu-item-home"

	# We return a rendered base.html with our model "posts".
	return render(request, 'base.html', {"posts": posts, "currPageClassSelector": currPageClassSelector, "viewName": viewName})

def contact(request):
	posts = Post.objects.filter(site=3).order_by('published_date')
	viewName = "contact.html"
	currPageClassSelector = ["", "", ""]
	currPage = 2
	currPageClassSelector[currPage] = "current-menu-item current_page_item menu-item-home"


	# We return a rendered base.html with our model "posts".
	return render(request, 'base.html', {"posts": posts, "currPageClassSelector": currPageClassSelector, "viewName": viewName})