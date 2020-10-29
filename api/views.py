from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse,JsonResponse
from company.models import Person, Company
from .forms import PersonForm



def get_person(request,sid):
    try:
        person = Person.objects.get(id=sid)
        data= {}
        data["id"]=person.id
        data["name"]=person.name
        data["amount"]=person.amount
        data["company"]=person.company.name
        return JsonResponse(data, status=200)
    except Exception:
        return JsonResponse({"Error":"Investor not found"}, status=404)


def get_details(request):
    all_details = [] 
    for person in Person.objects.all():
        data= {}
        data["id"]=person.id
        data["name"]=person.name
        data["amount"]=person.amount
        data["company"]=person.company.name
        all_details.append(data)
    return JsonResponse(all_details,safe=False, status=200)


def get_all_by_id(request,sid):
    for person in Person.objects.all():
        if person.id == sid:
            data= {}
            data["id"]=person.id
            data["name"]=person.name
            data["amount"]=person.amount
            data["company"]=person.company.name
            return JsonResponse(data, status=200)

@csrf_exempt
def create_person(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Success",status=200)
        
    else:
        #print(form.errors)
        return JsonResponse({"Error":"Person not created"}, status=404)

def get_all_companies(request):
    all_companies = []
    for company in Company.objects.all():
        data= {}
        data["id"]=company.id
        data["name"]=company.name
        data["location"]=company.location
        data["revenue"]=company.revenue
        all_companies.append(data)
    return JsonResponse(all_companies, safe=False, status=200)
