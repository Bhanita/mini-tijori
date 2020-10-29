from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse,JsonResponse
from company.models import Person, Company
from .forms import InvestorForm



def get_investor(request,sid):
    try:
        investor = Person.objects.get(id=sid)
        data= {}
        data["id"]=investor.id
        data["name"]=investor.name
        data["amount"]=investor.amount
        data["company"]=investor.company.name
        return JsonResponse(data, status=200)
    except Exception:
        return JsonResponse({"Error":"Investor not found"}, status=404)


def get_all_investors(request):
    all_investors = [] 
    for investor in Person.objects.all():
        data= {}
        data["id"]=investor.id
        data["name"]=investor.name
        data["amount"]=investor.amount
        data["company"]=investor.company.name
        all_investors.append(data)
    return JsonResponse(all_investors,safe=False, status=200)


def get_all_by_id(request,sid):
    all_investors = []
    for investor in Person.objects.all():
        if investor.id == sid:
            data= {}
            data["id"]=investor.id
            data["name"]=investor.name
            data["amount"]=investor.amount
            data["company"]=investor.company.name
            return JsonResponse(data, status=200)

@csrf_exempt
def create_investor(request):
    form = InvestorForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        #print(form.errors)
        return JsonResponse({"Error":"Investor not created"}, status=404)

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
