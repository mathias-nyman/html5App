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


#TODO: keep example of proxied JSON request
"""
def getValpasEvent(request, valpasEvent):

    # This method will relay JSON requests from the client side, to the
    # actual Valpas application running elsewhere

    # Event descriptions:
    #
    # event: door
    #   if not found, returning: "Not Found"
    #   if found, returning: 
    #   [
    #       {
    #           "device": {
    #               "description": "",
    #               "_state": "<django.db.models.base.ModelState object at 0xbda3f0>",
    #               "name": "door",
    #               "map_x": 0,
    #               "map_y": 0,
    #               "device_type_id": 1,
    #               "id": 7,
    #               "device_id": "2"
    #           },
    #           "variable": "DoorOpen",
    #           "value": 1.0,
    #           "time": "2011-09-14 16:57:26"
    #       }
    #   ]
    #

    import httplib2
    print "getValpasEvent(): valpasEvent=%s" % valpasEvent

    # The Valpas server address
    PROXY_DOMAIN = "130.233.120.107"
    PROXY_FORMAT = u"https://%s/%s" % (PROXY_DOMAIN, u"%s")

    # Assemble the URL for events on the Valpas server
    url = 'valpas/api/event/' + valpasEvent
    url = PROXY_FORMAT % url
    print "getValpasEvent(): url=%s" % url

    # Configure connection not to validate ssl certificates
    valpasConnection = httplib2.Http(disable_ssl_certificate_validation=True)

    # Provide authentication for server
    valpasConnection.add_credentials('admin','ALHDemo112')

    # Start the request towards Valpas
    print "getValpasEvent(): starting polling %s ..." % valpasEvent
    resp, content = valpasConnection.request(url, 'GET')
    print "getValpasEvent(): stopped polling %s" % valpasEvent

    # Transform string representation to python data types
    if content == "Not Found":
        ret = []
    else:
        ret = json.loads(content)
    print "getValpasEvent(): ret=%s" % (ret)
    return ret
service.add_method('getValpasEvent', getValpasEvent)
"""

