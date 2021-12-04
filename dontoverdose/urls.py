# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
from .views import addPrescriberPageView, deletePrescriber, displayDrugPageView, displayPrescriberPageView,  indexPageView, searchPresriberPageView, showAllDrugsPageView, showAllPrescribersPageView, showSinglePrescriberPageView, storePrescriberPageView, updatePrescriber, show_prescribed_drugs
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
    path("searchPrescriber/", searchPresriberPageView, name="searchPrescriber"),
    path("searchDrug/", searchDrugPageView, name="searchDrug"),
    path("allDrugs/", showAllDrugsPageView, name="allDrugs"),
    path("allPrescribers/", showAllPrescribersPageView, name="allPrescribers"),
    path("addPrescriber/", addPrescriberPageView, name="addPrescriber"),
    path("storePrescriber/", storePrescriberPageView, name="storePrescriber"),
    path("showPrescriber/<int:NPI>/",
         showSinglePrescriberPageView, name='singlePrescriber'),
    path("updatePrescriber/", updatePrescriber, name="updatePrescriber"),
    path("deletePrescriber/<int:NPI>/", deletePrescriber, name="deletePrescriber"),
    path("show_prescribed_drugs/", show_prescribed_drugs, name="show_prescribed_drugs"),
    path("contact/", contactPageView, name="contact")

    # path(
    #     "aboutData/<str:trip_name>/<int:trip_length>",
    #     aboutPageDataView,
    #     name="aboutData",
    # ),
    # # this path goes to the view that will display DATABASE data!
    # path("students/", displayStudentView, name="student"),
    # # this path goes to the view that will display DATABASE data PART 2!
    # path("searchemp/", searchEmpPageView, name="searchEmp"),
    # # path("About/", aboutPageView, name="about"),]
]
