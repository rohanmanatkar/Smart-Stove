from django.shortcuts import render
from stove.models import State
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')


def getState(request):
    result =  State.get_state()
    #print("from result", result["temp"])
   
    
    if (result['temp'] > 30 and result['proximity1'] > 15):
        display_msg= "Stove seems to be ON and nothing is cooking!"
    elif (result['temp'] > 30 and result['proximity1'] < 15):
        display_msg = "Food on stove. Must be burning!"
    else:
        display_msg = "Everything is OK"
        
    context = {
    'temp' : result['temp'],
    'proximity1' : result['proximity1'],
    'proximity2' : result['proximity2'],
    'display_msg' : display_msg,
        }

    #request.session['temp'] = result.temp 
    #request.session['proximity1'] = result.proximity1
    #request.session['proximity2'] = result.proximity2
    return render(request,'dashboard.html', context=context)
    #return JsonResponse(State.get_state())

def mobileApp(request):
    return JsonResponse(State.get_state())


def saveState(request, temp, p1, p2):
    # temp = float(request.POST.get('temp'))
    # p1 = float(request.POST.get('p1'))
    # p2 = float(request.POST.get('p2'))
    created = State.saveState(float(temp), float(p1), float(p2))
    return JsonResponse({"success": created})
