from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json, requests
from newsapi import NewsApiClient
# Create your views here.
newsapi = NewsApiClient(api_key = 'XXXXXXXXX')

def index(request):
    topheadlines = newsapi.get_top_headlines(country = 'in')
    articles = topheadlines['articles']
    return render(request, "MyNews/index.html", {
        "news": articles,
        "n1":articles[1],
        "n2":articles[2],
        "n3":articles[3]
    })

def categoric(request,category):
    topheadlines = newsapi.get_top_headlines(category = category, country = 'in')
    articles = topheadlines['articles']
    return render(request, "MyNews/index.html", {
        "news": articles
    })

def worldnews(request):
    topheadlines = newsapi.get_top_headlines()
    articles = topheadlines['articles']
    return render(request, "MyNews/index.html", {
        "news": articles
    })

def search(request):
    if request.method == "POST":
        query = request.POST['query']
        info = newsapi.get_everything(q = query)
        if info['totalResults'] == 0:
            topheadlines = newsapi.get_top_headlines(country = 'in')
            articles = topheadlines['articles']
            return render(request, "MyNews/index.html", {
                "news": articles
            })
        else:
            articles = info['articles']
            return render(request, "MyNews/index.html", {
                "news": articles
            })
    else:
        topheadlines = newsapi.get_top_headlines(country = 'in')
        articles = topheadlines['articles']
        return render(request, "MyNews/index.html", {
            "news": articles,
        })
