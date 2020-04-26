from flask import render_template, request, redirect, url_for
from . import main
from ..models import Articles, Sources
from ..requests import get_sources,get_article,search_everything

# Views
@main.route('/')
def index(): 
    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	health_sources = get_sources('health')
 
	title = "News Highlight"
