# import requests
# import requests

# NEED TO IMPORT MODELS INTO VIEW FUNCTIONS
from .models import Prescriber, Drugs, Triple

###### import models ########
# from travelSites.models import em


# this is for rendering the files
from django.shortcuts import render

# this view function needs to send the RESPONSE
from django.http import HttpResponse

# redeirect fucntion
from django.shortcuts import redirect


# Create your views here.
def indexPageView(request):
    return render(request, "dontoverdose/index.html")


def aboutPageView(request):
    # OLD WAY return HttpResponse("I am the about page!")
    return render(request, "dontoverdose/about.html")


def contactPageView(request):
    return render(request, "dontoverdose/contact.html")


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
    # iNPI = request.GET['NPI']
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    # sGender = request.GET['prescriber_gender']
    # sCredentials = request.GET['prescriber_credentials']
    # sLocation = request.GET['location']
    # sSpecialty = request.GET['prescriber_specialty']
    # sIsOpioid = request.GET['opioid_dude?']
    # iTotal = request.GET['total']

    # ,        npi__iexact=iNPI, , gender__iexact=sGender, credentials__iexact=sCredentials, state__iexact=sLocation, specialty__iexact=sSpecialty, isopioidprescriber__iexact=sIsOpioid, totalprescriptions__iexact=iTotal)
    data = Prescriber.objects.filter(fname__iexact=sFirst, lname__iexact=sLast)
    data2 = Triple.objects.values_list('npi', 'drugname', 'qtyprescribed')

    if data.count() > 0:
        context = {
            "our_prescribers": data,
            "our_drugs": data2
        }
        return render(request, 'dontoverdose/displayPrescriber.html', context)
    else:
        return HttpResponse("Not found")


# SEARCHES FOR DRUGS #####################


def displayDrugPageView(request):
    name = request.GET['name']
    # opioid_label = request.GET['is_opiate']
    # , isopioid=opioid_label)
    # need to make this so it can be lowercase or whatever!!!

    data = Drugs.objects.filter(drugname__iexact=name)

    if data.count() > 0:
        context = {
            "our_drugs": data
        }
        return render(request, 'dontoverdose/displayDrug.html', context)
    else:
        return HttpResponse("Not found")

# this will pull up the ADD PRESCRIBER page


def addPrescriberPageView(request):
    return render(request, "dontoverdose/addPrescriber.html")

#### this is going to actually save the prescriber to the database when submitted!!!#####


def storePrescriberPageView(request):
    # check that there is data, if not then tell the user!
    # if new_prescriber.npi is None:
    # HttpResponse("You need data ")

    # Check to see if the form method is a get or post
    if request.method == 'POST':

        # Create a new employee object from the model (like a new record)
        new_prescriber = Prescriber()

        # Store the data from the form to the new object's attributes (like columns)
        new_prescriber.npi = request.POST.get('NPI')

        new_prescriber.fname = request.POST.get('first_name')
        new_prescriber.lname = request.POST.get('last_name')
        new_prescriber.gender = request.POST.get('prescriber_gender')
        new_prescriber.state = request.POST.get('location')
        new_prescriber.credentials = request.POST.get('prescriber_credentials')
        new_prescriber.specialty = request.POST.get('prescriber_specialty')
        new_prescriber.isopioidprescriber = request.POST.get('opioid_dealer')
        new_prescriber.totalprescriptions = request.POST.get('total')

        # Save the employee record
        new_prescriber.save()

    # Make a list of all of the employee records and store it to the variable
    data = Prescriber.objects.all()

    # Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_prescribers": data
    }
    # r = requests.post('')
    return render(request, 'dontoverdose/displayPrescriber.html', context)


###### trying to edit and delete ########
def showSinglePrescriberPageView(request, NPI):
    data = Prescriber.objects.get(npi=NPI)

    context = {
        "prescriber": data
    }
    return render(request, 'dontoverdose/updatePrescriber.html', context)

##### editing a specific prescriber ########


def updatePrescriber(request):
    if request.method == 'POST':
        iNPI = request.POST['NPI']

        # Find the employee record
        prescriber = Prescriber.objects.get(npi=iNPI)

        # Modify the employee last name with a new value from the form
        prescriber.npi = iNPI
        prescriber.fname = request.POST['first_name']
        prescriber.lname = request.POST['last_name']
        prescriber.gender = request.POST['prescriber_gender']
        prescriber.state = request.POST['location']
        prescriber.credentials = request.POST['prescriber_credentials']
        prescriber.specialty = request.POST['prescriber_specialty']
        prescriber.isopioidprescriber = request.POST['opioid_dealer']
        prescriber.totalprescriptions = request.POST['total']

        # Save the changes
        prescriber.save()

    return showAllPrescribersPageView(request)


# delete a prescriber
def deletePrescriber(request, NPI):
    data = Prescriber.objects.get(npi=NPI)
    # ARE YOU SURE FUCNTION
    # IF STATEMENT= if the NPI doesn't exist, redirects
    data.delete()

    return showAllPrescribersPageView(request)
