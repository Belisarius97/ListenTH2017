from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
import urllib.parse
import urllib.request
try:
    import json
except ImportError:
    import simplejson as json

from .models import Song

def index(request):
    song_list = Song.objects.all()
    context = {'song_list': song_list}
    return render(request, 'listen/index.html', context)

def make_playlist(request):
    return HttpResponse("Yooooo!")

# Create your views here.
"""
def index(request):
    api_host = 'api.musixmatch.com'
    api_selector = '/ws/1.1/'
    method = 'track.lyrics.get'
    api_key = 'bfa3d54946f3a61d45327d53931c4bcf'

    params = {}
    params['format'] = 'json'
    params['callback'] = 'callback'
    params['apikey'] = api_key
    params['track_id'] = 122216636
    params = urllib.parse.urlencode(params)
    
    url = 'http://%s%s%s?%s' % (api_host, api_selector, method, params)

    f = urllib.request.urlopen(url)
    response = f.read()
    response = decode_json(response)
    res_checked = check_status(response)
    
    return HttpResponse("Hello world! Here's the data I found: \n%s" % res_checked['lyrics']['lyrics_body'])

def decode_json(raw_json):
    # Transform the json into a python dictionary or raise a ValueError
    try:
        response_dict = json.loads(raw_json)
    except ValueError:
        raise Http404("Error parsing json!")
    return response_dict

def check_status(response):
    # Checks the response in JSON format
    # Raise an error, or return the body of the message
    if not 'message' in response.keys():
        raise Http404("JSON does not have field 'message'!")
    msg = response['message']
    if not 'header' in msg.keys():
        raise Http404("JSON does not have field 'header'!")
    header = msg['header']
    if not 'status_code' in header.keys():
        raise Http404("JSON does not have field 'status_code'!")
    code = header['status_code']
    if code != 200:
        raise Http404("'status_code' is not 200! It is %s" % code)
    body = msg['body']
    return body
"""
