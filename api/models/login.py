__author__ = 'rolanvc'

from django.db import models
from .config import Locator


class UserRole(models.Model):
    name = models.CharField(max_length=32)

    # Privileges of Superadmins
    approve_locator = models.BooleanField(default=False, null=False)
    approve_project = models.BooleanField(default=False, null=False)
    approve_vehicle_type = models.BooleanField(default=False, null=False)
    approve_vehicle_usage = models.BooleanField(default=False, null=False)
    approve_id_fee = models.BooleanField(default=False, null=False)
    approve_locator_sticker_fee = models.BooleanField(default=False, null=False)
    approve_csprm_sticker_fee = models.BooleanField(default=False, null=False)
    approve_type_of_work = models.BooleanField(default=False, null=False)
    approve_plate_no_format = models.BooleanField(default=False, null=False)
    approve_banned_employee= models.BooleanField(default=False, null=False)
    approve_flagged_purpose = models.BooleanField(default=False, null=False)

    # Privileges of Admins
    request_locator = models.BooleanField(default=False, null=False)
    request_project = models.BooleanField(default=False, null=False)
    request_vehicle_type = models.BooleanField(default=False, null=False)
    request_vehicle_usage = models.BooleanField(default=False, null=False)
    request_id_fee = models.BooleanField(default=False, null=False)
    request_locator_sticker_fee = models.BooleanField(default=False, null=False)
    request_csprm_sticker_fee = models.BooleanField(default=False, null=False)
    request_type_of_work = models.BooleanField(default=False, null=False)
    request_plate_no_format = models.BooleanField(default=False, null=False)
    request_banned_employee = models.BooleanField(default=False, null=False)
    request_flagged_purpose = models.BooleanField(default=False, null=False)

    # Privileges of Central_Authorizers
    manage_user = models.BooleanField(default=False, null=False)
    view_reports = models.BooleanField(default=False, null=False)

    def __unicode__(self):
        return self.name


class User(models.Model):
    user_role = models.ForeignKey(UserRole, on_delete=models.PROTECT)
    locator = models.ForeignKey(Locator, null=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=256)
    uuid = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', related_name='c_u', on_delete=models.PROTECT)
    last_modified_date = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey('User', related_name='m_u', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True, null=False)
    times_wrong_passwd = models.IntegerField(default=0, null=False)
    last_login = models.DateTimeField(null=True)

    # Privileges of ordinary user

    # revised permissions
    access_guest = models.BooleanField(default=False, null=False)
    access_applicant= models.BooleanField(default=False, null=False)
    access_temp = models.BooleanField(default=False, null=False)

    pass_construction = models.BooleanField(default=False, null=False)
    pass_service= models.BooleanField(default=False, null=False)
    pass_repair = models.BooleanField(default=False, null=False)

    sticker_locator = models.BooleanField(default=False, null=False)
    sticker_contractor= models.BooleanField(default=False, null=False)
    sticker_service = models.BooleanField(default=False, null=False)
    sticker_vendor = models.BooleanField(default=False, null=False)

    def __unicode__(self):
        nm = self.last_name + ', ' + self.first_name
        if self.middle_name is not None:
            nm += self.middle_name
        return nm

    class Meta:
        app_label = 'api'


