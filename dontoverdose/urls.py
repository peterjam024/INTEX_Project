# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
<<<<<<< Updated upstream
from .views import addPrescriberPageView, deletePrescriber, displayDrugPageView, displayPrescriberPageView,  indexPageView, loadOurFindings, loadOurImplementation, searchPresriberPageView, showAllDrugsPageView, showAllPrescribersPageView, showSinglePrescriberPageView, sqlStatsView, storePrescriberPageView, topTenDrugsPageView, updatePrescriber, show_prescribed_drugs, deletePrescriberforreal
=======
from .views import addPrescriberPageView, deletePrescriber, displayDrugPageView, displayPrescriberPageView,  indexPageView, loadOurFindings, loadOurImplementation, mockupView, searchPresriberPageView, showAllDrugsPageView, showAllPrescribersPageView, showSinglePrescriberPageView, sqlStatsView, storePrescriberPageView, updatePrescriber, show_prescribed_drugs, deletePrescriberforreal
>>>>>>> Stashed changes
from .views import aboutPageView, contactPageView
from .views import searchDrugPageView
# we create the path with this syntax
urlpatterns = [
    # first part of path --> WHERE website.com/DIRECTION ... the page to render which is the VIEW function
    # ... give it a name
    path("", indexPageView, name="index"),
    # 2nd path
    path("home/", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("displayPrescriber/", displayPrescriberPageView, name="displayPrescriber"),
    path("displayDrug/", displayDrugPageView, name="displayDrug"),
    path("topTenDrugsPageView/", topTenDrugsPageView, name="topTenDrugsPageView"),
    path("searchPrescriber/", searchPresriberPageView, name="searchPrescriber"),
    path("searchDrug/", searchDrugPageView, name="searchDrug"),
    path("allDrugs/", showAllDrugsPageView, name="allDrugs"),
    path("allPrescribers/", showAllPrescribersPageView, name="allPrescribers"),
    path("addPrescriber/", addPrescriberPageView, name="addPrescriber"),
    path("storePrescriber/", storePrescriberPageView, name="storePrescriber"),
    path("showPrescriber/<int:NPI>/",
         showSinglePrescriberPageView, name='singlePrescriber'),
    path("updatePrescriber/", updatePrescriber, name="updatePrescriber"),
    path("deletePrescriber/<int:NPI>/",
         deletePrescriber, name="deletePrescriber"),
    path("deletePrescriberforreal/<int:NPI>/",
         deletePrescriberforreal, name="deletePrescriberforreal"),
    path("show_prescribed_drugs/", show_prescribed_drugs,
         name="show_prescribed_drugs"),
    path("contact/", contactPageView, name="contact"),
    path("pdf/", loadOurFindings, name='pdf'),
    path("implementation", loadOurImplementation, name="implementation"),
    path('sql/', sqlStatsView, name='sql'),
    path('mockup/', mockupView, name='mockup')

]
