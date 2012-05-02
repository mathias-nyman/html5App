from django_pimentech.network import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from ExampleApp.models import ExampleObject

import json
import os


service = JSONRPCService()

# Serve base html on index request
def index(request):
    return render_to_response('ExampleApp.html')


# Returns all tags, in the form of a dictionary: { tagId : (description, isfound) }
def getExampleObjects(request):
    print 'getExampleObjects(): enter...'
    ret = {}

    try:
        allObjects = ExampleObject.objects.filter()
    except Exception as e:
        print 'getExampleObjects(): inproper exit...'
        return ret
    for obj in allObjects:
        ret[obj.name] = (ojb.pic)

    print 'getExampleObjects: returning: ', ret
    return ret
service.add_method('getExampleObjects', getExampleObjects)


#@param obj: must contain obj.name and obj.pic strings
def saveExampleObject(request, obj):
    print 'saveExampleObject(): enter...'

    # Don't allow duplicates
    matchingObj = ExampleObject.objects.filter(name=obj.name)
    if matchingObj != 0:
        print 'saveExampleObject(): updating existing objects picture'
        newObj = matchingObj[0] #NOTE: this is safe, since name is treated as unique
    else:
        print 'saveExampleObject(): creating new object'
        newObj = ExampleObject()

    newObj.name = obj.name
    newObj.pic = obj.pic
    newObj.save()
    return True
service.add_method('saveExampleObject', saveExampleObject)


def removeExampleObject(request, objName):
    try:
        ExampleObject.objects.get(name=objName).delete()
    except ExampleObject.DoesNotExist:
        return False
    return True
service.add_method('removeExampleObject', removeExampleObject)


def getAllPics(request):
    pics = []
    print 'getAllPics(): enter...'
    picsPath = settings.STATIC + '/images/' #TODO: add variable to settings.py
    for dirname, dirnames, filenames in os.walk(picsPath):
        for subdirname in dirnames:
            pics.append('images/' + subdirname)
        for filename in filenames:
            pics.append('images/' + filename)

    print 'getAllPics(): returning:\n%s' % (pics)
    return pics
service.add_method('getAllPics', getAllPics)

