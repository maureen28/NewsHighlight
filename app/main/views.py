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
    if search_everything:
        return redirect(url_for('search', article_title = search_everything))
    else:
        return render_template('index.html', title = title, sources = sources, ent = entertainment_sources, sports = sports_sources, tech = technology_sources,health = health_sources )
 
@main.route('/sources/<id>')
def articles(id): 
    '''
    View root page function that returns the article page and its data
    '''
   article = get_article(id)
   title = f'{article.title}'

    return render_template('article.html', title = title, article = article )


@main.route('/search/<article_title>')
def search(article_title):
    '''
    View function to display the search results
    '''
    limit = 40
    article_name_list = article_title.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_title}'
    return render_template('search.html',title = title ,articles = searched_articles)
