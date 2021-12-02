from django.db import models

# Create your models here.


########################################## pd_drugs ###################################################
# good!
# still need to add to TRIPLE
class Drugs(models.Model):
    drugid = models.IntegerField()
    drugname = models.CharField(max_length=30, primary_key=True)
    isopioid = models.CharField(max_length=5)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "pd_drugs"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.drugname + " \nIs an Opioid?: " + self.isopioid


########################################## pd_StateData ###################################################
# good on both this and prescriber
# still need to add to TRIPLE

class State(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2, primary_key=True)
    population = models.IntegerField()
    deaths = models.IntegerField()
    populationpc = models.DecimalField(max_digits=11, decimal_places=9)

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "pd_statedata"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.state + " has a population of " + self.population + " and has " + self.deaths + " deaths."


########################################## pd_Prescriber_info ###################################################
# good on this and the state
class Prescriber (models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey(
        'State', null=True, blank=True, on_delete=models.SET_NULL)
    credentials = models.CharField(max_length=7)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField()

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "pd_prescriber_info"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.fname + " " + self.lname


########################################## THIS IS THE triple ###################################################
# --> still need to make new table
# this shows the type of drug and how much of each drug was adminsiterd
# not shown on any other table

class Triple (models.Model):
    # don't need to make id, becuase python will do it= autogenerates!
    npi = models.ForeignKey(
        'Prescriber', null=True, blank=True, on_delete=models.SET_NULL)
    drugname = models.ForeignKey(
        'Drugs', null=True, blank=True, on_delete=models.SET_NULL)
    qtyprescribed = models.IntegerField()

    # This links THIS model to the database table (:
    # python will automatically do this, but this just makes SURE and will override what python automatically does

    class Meta:
        db_table = "pd_triple"

    # ACCESS DATA--> if try to look at a single record, we are going to return the description
    # the description= the description field from the table
    # This is what is going to be displayed to the ADMIN!!
    def __str__(self):
        return self.npi + " " + self.drugname + " " + self.qtyprescribed
