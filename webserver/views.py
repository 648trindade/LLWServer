from django.shortcuts import render
from django.http import HttpResponse
import os, json

# Create your views here.

def getVersions():
    jsons = os.listdir('static/json/')
    jsons.remove('template.json')
    versions = [float(name.replace('.json','').replace('_','.')) for name in jsons]
    sorted(versions)
    return versions

def version(request):
    if request.method == 'GET':
        curVersion = float(request.GET['version'])
        lastVersion = getVersions()[-1]
        dic = { "atualizacoes": lastVersion > curVersion }
        if dic["atualizacoes"]:
            dic["newVersion"] = str(lastVersion)
        return HttpResponse(json.dumps(dic, indent=4, sort_keys=True))

def update(request):
    curVersion = float(request.GET['version'])
    versions = filter(lambda v: v > curVersion, getVersions())
    dic = []
    for version in versions:
        filename = 'static/json/' + str(version).replace('.','_') + '.json'
        with open(filename) as jfile:
            data = json.load(jfile)
            dic += data
    
    return HttpResponse(json.dumps(dic, indent=4, sort_keys=True))

