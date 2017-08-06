from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

import requests
import json
import hashlib
import datetime

def index(request):
    private_key = 'XXX'
    public_key = 'XXX'
    ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    tshash = hashlib.md5("%s%s%s" % (ts, private_key, public_key)).hexdigest()
    about = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009378?ts='+ts+'&apikey='+public_key+'&hash='+tshash)
    comic = requests.get('https://gateway.marvel.com:443/v1/public/stories/77852?ts='+ts+'&apikey='+public_key+'&hash='+tshash)
    character = requests.get('https://gateway.marvel.com:443/v1/public/stories/77852/characters?ts='+ts+'&apikey='+public_key+'&hash='+tshash)
    return render(request, 'index.html', { 'about': about.json(), 'comics': comic.json(), 'characters': character.json() })

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})
