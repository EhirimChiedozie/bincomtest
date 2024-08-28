from django.db import models
import datetime
# Create your models here.

class AgentName(models.Model):
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()


class AnnouncedLgaResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=40)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)


class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)


class AnnouncedStateResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)


class AnnouncedWardResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)


class Lga(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)


class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)


class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField(null=True)
    lga_id = models.IntegerField(null=True)
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.CharField(max_length=100, null=True)
    user_ip_address = models.CharField(max_length=50, null=True)


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)


class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=50)