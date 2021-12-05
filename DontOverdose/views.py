# import requests
# import requests

# NEED TO IMPORT MODELS INTO VIEW FUNCTIONS
from .models import Prescriber, Drugs, Triple, State

###### import models ########
# from travelSites.models import em


# this is for rendering the files
from django.shortcuts import render

# this view function needs to send the RESPONSE
from django.http import HttpResponse

# redeirect fucntion
from django.shortcuts import redirect

import webbrowser


# Create your views here.
def loadOurFindings(request):
    a_website = "https://docs.google.com/document/d/1kl4OnH6r4-B4LD2-QD5-_3CJ6BoskUCfCL-C9bLug_o/edit?usp=sharing"

    # Open url in a new page (“tab”) of the default browser, if possible
    webbrowser.open_new_tab(a_website)
    return render(request, "dontoverdose/index.html")


def loadOurImplementation(request):
    a_website = "https://docs.google.com/document/d/18c007R83f35F1Fvjnq23oXW14-cRxHXsqC50JU3YqR0/edit?usp=sharing"

    # Open url in a new page (“tab”) of the default browser, if possible
    yes = webbrowser.open_new_tab(a_website)
    return render(request, "dontoverdose/index.html")


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
    drug_list = Drugs.objects.all()

    context = {
        'drug_list': drug_list,
    }
    return render(request, "dontoverdose/searchDrug.html", context)


# SEARCHES FOR PRESCRIBERS #


def displayPrescriberPageView(request):
    sFirst = request.GET['first_name']
    sFirstCaptial = sFirst.capitalize()
    sLast = request.GET['last_name']
    sLastCaptial = sLast.capitalize()

    data = Prescriber.objects.filter(
        fname__contains=sFirstCaptial, lname__contains=sLastCaptial)
    if data.count() > 0:
        context = {
            "our_prescribers": data,
        }
        return render(request, 'dontoverdose/displayPrescriber.html', context)
    else:
        return render(request, "dontoverdose/badSearchPrescriber.html")


# SEARCHES FOR DRUGS #####################


def displayDrugPageView(request):
    name = request.GET['name']
    nameUpper = name.upper()
    # opioid_label = request.GET['is_opiate']
    # , isopioid=opioid_label)
    # need to make this so it can be lowercase or whatever!!!

    data = Drugs.objects.filter(drugname__contains=nameUpper)

    if data.count() > 0:
        context = {
            "our_drugs": data
        }
        return render(request, 'dontoverdose/displayDrug.html', context)
    else:
        return render(request, "dontoverdose/badSearchDrug.html")

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


def show_prescribed_drugs(request):
    iNPI = request.GET['NPI']

    data = Triple.objects.filter(npi=iNPI)
    data2 = Prescriber.objects.filter(npi = iNPI)
    context = {
        "our_drugs": data,
        "our_prescribers" : data2
    }
    return render(request, 'dontoverdose/displayPrescriberAndDrugs.html', context)


##### editing a specific prescriber #########


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

def deletePrescriber(request, NPI):
    data=Prescriber.objects.get(npi=NPI)
    prescriber_list = Prescriber.objects.filter(npi = NPI)
    context = {
        'prescriber_list': prescriber_list,
    }
    return render(request, "dontoverdose/deleteprescriber.html", context)

# delete a prescriber
def deletePrescriberforreal(request, NPI):
    data = Prescriber.objects.get(npi=NPI)
    # ARE YOU SURE FUNCTION
    # IF STATEMENT= if the NPI doesn't exist, redirects
    data.delete()

    return showAllPrescribersPageView(request)
