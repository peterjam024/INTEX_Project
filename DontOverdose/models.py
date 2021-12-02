from django.db import models

# Create your models here.


########################################## pd_drugs ###################################################
class Drugs(models.Model):
    drugid = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=30)
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
class State(models.Model):
    state = models.CharField(max_length=14, primary_key=True)
    stateabbrev = models.CharField(max_length=2)
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
# THIS HAS NO DATABASE YET, do not use --> still need to make new table
class Prescriber (models.Model):
    npi = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
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

# class Triple (models.Model):
#     # don't need to make id, becuase python will do it= autogenerates!
#     npi = models.BigIntegerField()
#     drugname = models.CharField(max_length=40)
#     qtyprescribed = models.IntegerField()

#     # This links THIS model to the database table (:
#     # python will automatically do this, but this just makes SURE and will override what python automatically does

#     class Meta:
#         db_table = "pd_prescriber_updated"

#     # ACCESS DATA--> if try to look at a single record, we are going to return the description
#     # the description= the description field from the table
#     # This is what is going to be displayed to the ADMIN!!
#     def __str__(self):
#         return self.NPI + " " + self.DrugName + " " + self.QtyPrescribed
