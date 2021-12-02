# NEED TO IMPORT MODELS INTO VIEW FUNCTIONS
from .models import Prescriber, Drugs

###### import models ########
# from travelSites.models import em


# this is for rendering the files
from django.shortcuts import render

# this view function needs to send the RESPONSE
from django.http import HttpResponse

# HERE, I need to import the HTML page that I want and then i can return it LATER
# import index.html from travelPages


# Create your views here.
def indexPageView(request):
    return render(request, "dontoverdose/index.html")


def aboutPageView(request):
    # OLD WAY return HttpResponse("I am the about page!")
    return render(request, "dontoverdose/about.html")


def showAllDrugsPageView(request):
    drug_list = Drugs.objects.all()
    context = {
        'drug_list': drug_list,
    }
    return render(request, "dontoverdose/allDrugs.html", context)


def showAllPrescribersPageView(request):
    prescriber_list = Prescriber.objects.all()
    context = {
        'prescriber_list': prescriber_list,
    }
    return render(request, "dontoverdose/allPrescribers.html", context)


# DISPLAY search forms


def searchPresriberPageView(request):
    return render(request, "dontoverdose/searchPrescriber.html")


def searchDrugPageView(request):
    return render(request, "dontoverdose/searchDrug.html")


# SEARCHES FOR PRESCRIBERS #


def displayPrescriberPageView(request):
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    sGender = request.GET['prescriber_gender']
    sCredentials = request.GET['prescriber_credentials']
    sLocation = request.GET['location']
    sSpecialty = request.GET['last_name']

    data = Prescriber.objects.filter(
        fname=sFirst, lname=sLast, gender=sGender, credentials=sCredentials, state=sLocation, specialty=sSpecialty)

    if data.count() > 0:
        context = {
            "our_prescribers": data
        }
        return render(request, 'dontoverdose/displayPrescriber.html', context)
    else:
        return HttpResponse("Not found")

# SEARCHES FOR DRUGS #####################


def displayDrugPageView(request):
    name = request.GET['name']
    opioid_label = request.GET['is_opiate']
    data = Drugs.objects.filter(drugname=name, isopioid=opioid_label)

    if data.count() > 0:
        context = {
            "our_drugs": data
        }
        return render(request, 'dontoverdose/displayDrug.html', context)
    else:
        return HttpResponse("Not found")


# def empPageView(request):
#     data = Employee.objects.all()

#     context = {
#         "our_emps": data
#     }
#     return render(request, 'homepages/displayEmps.html', context)


# def aboutPageDataView(request, trip_name, trip_length):
#     # new way to render
#     context = {
#         "trip_name": trip_name,
#         "trip_length": trip_length + 2,
#         "places_to_visit": [
#             "Arenal Volcano",
#             "Manual Antonio National Park",
#             "Monteverde Cloud Forest",
#         ],
#     }

#     return render(request, "travelPages/aboutData.html", context)


# def displayStudentView(request):
#     data = Student.objects.all()
#     lookup = Grade_Level.objects.all()

#     # dictionary data
#     context = {"our_students": data, "grades": lookup}

#     return render(request, "travelPages/displayStudents.html", context)


# def searchEmpPageView(request):
#     sFirst = request.GET["first_name"]
#     sLast = request.GET["last_name"]
#     # data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)
#     # filter method LIMITS records, whereas the ALL gets all the records

#     # using query tool --> this is HUGE for intex!!
#     # need to se id!!
#     # sQuery= the first statement returns ALL
#     # if --> this filters
#     # after data= Student.obejcts.raw (sQuery)
#     # if data.count() > 0:
#     #     context = {"our_emps": data}
#     #     return render(request, "homepages/displayEmps.html", context)
#     # else:
#     #     return HttpResponse("Not found")
