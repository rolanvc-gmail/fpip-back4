__author__ = 'rolanvc'

from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)
    gen_contractor = models.CharField(max_length=255)
    sub_con_1 = models.CharField(max_length=255,default=None, null=True)
    sub_con_2 = models.CharField(max_length=255, default=None, null=True)
    sub_con_3 = models.CharField(max_length=255, default=None, null=True)
    type_of_work = models.ForeignKey('TypeOfWork', default=None, on_delete=models.PROTECT)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    extension_start = models.DateField(null=True)
    extension_end = models.DateField(null=True)
    # construction_bond = models.CharField(max_length=255)
    target_date_of_payment = models.DateField(null=True)
    actual_date_of_payment = models.DateField(null=True)
    # pr_number = models.CharField(max_length=255)
    # remarks = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='prj_cb', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='prj_lm', on_delete=models.PROTECT)

    # Approve defaults to False, first, until approved by superadmin.
    # Active defaults to True, until deleted.
    # Therefore default query for this should be: approved=true, active=true.
    # For admins and superadmins, it doesn't matter.
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.project_name

    class Meta:
        app_label = 'api'


##############################
#
# The rest of the models are for support.  They provide a way for other models' fields to
# have foreign keys.
#
##############################


class GeneralContractor(models.Model):
    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class CompanyName(models.Model):
    gen_contractor = models.ForeignKey('GeneralContractor', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'api'








