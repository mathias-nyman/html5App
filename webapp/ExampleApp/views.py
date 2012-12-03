from django_pimentech.network import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from ExampleApp.models import ExampleObject


service = JSONRPCService()

# Serve base html on index request
def index(request):
    return render_to_response('ExampleApp.html')


# Returns all object , in the form of a dictionary:
# { name : value }
def getExampleObjects(request):
    print 'getExampleObjects(): enter...'
    ret = {}

    try:
        allObjects = ExampleObject.objects.filter()
    except Exception as e:
        print 'getExampleObjects(): inproper exit...'
        return ret
    for obj in allObjects:
        ret[obj.name] = obj.value

    print 'getExampleObjects: returning: ', ret
    return ret
service.add_method('getExampleObjects', getExampleObjects)

