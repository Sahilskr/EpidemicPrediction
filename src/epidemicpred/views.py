from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import City
from django.db.models import Q
import os
from .twitter import *
from django.http import JsonResponse

# Create your views here.
def home(request,*args, **kwargs):
    return render(request,"index.html",{})

def about(request,*args, **kwargs):
    return render(request,"about.html",{})

def contact(request,*args, **kwargs):
    return render(request,"contact.html",{})

def helpline(request,*args, **kwargs):
    return render(request,"helpline.html",{})

def sentiment(request,*args, **kwargs):
    return render(request,"index2.html",{})


class SearchResultsView(ListView):
    model = City
    template_name = 'tp.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
        Q(name__icontains=query) | Q(state__icontains=query)
    )
        return object_list

class TweetView(ListView):
    template_name="index2.html"
    def strtobool(v):
        return v.lower() in ["yes", "true", "t", "1"]
    api = TwitterClient('@Sirajology')
    def tweets():
        retweets_only = request.args.get('retweets_only')
        api.set_retweet_checking(strtobool(retweets_only.lower()))
        with_sentiment = request.args.get('with_sentiment')
        api.set_with_sentiment(strtobool(with_sentiment.lower()))
        query = request.args.get('query')
        api.set_query(query)

        tweets = api.get_tweets()
        return JsonResponse({'data': tweets, 'count': len(tweets)})
