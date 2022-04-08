__author__ = 'rolanvc'

from django.db import models

################
##
## Counters
##
###############
class Counters(models.Model):
    name = models.CharField(max_length=32)
    counter = models.IntegerField(default=0)
    last_modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'api'



################
##
## Vehicle Types
##
###############


class VehicleType(models.Model):
    type_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='vt_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='vt_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.type_name

    class Meta:
        app_label = 'api'




################
##
## Vehicle Usage
##
###############


class VehicleUsage(models.Model):
    usage_name = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='vu_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='vu_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.usage_name

    class Meta:
        app_label = 'api'



################
##
## Types Of Work
##
###############


class TypeOfWork(models.Model):
    type_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='tow_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='tow_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.type_name
    class Meta:
        app_label = 'api'



################
##
## Plate Number Formats
##
###############


class PlateNumberFormat(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT)
    format_string = models.CharField(max_length=50)
    friendly_format = models.CharField(max_length=30, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='pnf_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='pnf_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'



################
##
## Banned Employees
##
###############

class BannedEmployee(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='be_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='be_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'



################
##
## FlaggedPurpose
##
###############

class FlaggedPurpose(models.Model):
    title = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='fp_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='fp_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'




################
##
## Locators
##
################


class Locator(models.Model):
    name = models.CharField(max_length=255)
    # no = models.IntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='loc_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='loc_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'api'






