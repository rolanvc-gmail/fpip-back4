from django.db import models

#####################################
#
# Locator
#
#####################################
class LocatorVehicleStickers(models.Model):
    start_date= models.DateField(null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT)
    vehicle_plate_no = models.CharField(max_length=20, db_index=True)
    purpose = models.CharField(max_length=255)
    brand = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30)
    model = models.CharField(max_length=15, blank=True)
    or_number = models.CharField(max_length=15, db_index=True)
    or_date = models.DateField()
    cr_number = models.CharField(max_length=15, db_index=True)
    cr_date = models.DateField()
    vehicle_owner_name = models.CharField(max_length=30)
    address_of_vehicle_owner = models.CharField(max_length=255)
    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)

    transaction_reference_number = models.CharField(max_length=30, null=True)
    sticker_number = models.CharField(max_length=30, null=True)
    detail_reference_number = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', models.PROTECT)

    # Used for acceptance / denial
    approved = models.BooleanField(default=False)
    cost = models.FloatField(null=True)
    flagged = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, null=True)
    id_pass_sticker = models.CharField(max_length=15, null=True)
    validity_months = models.IntegerField(null=True)
    valid_until = models.DateField(null=True)


#####################################
#
# Contractor
#
#####################################
class ContractorVehicleStickers(models.Model):
    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)
    gen_contractor = models.ForeignKey('GeneralContractor', models.PROTECT)
    subcon = models.ForeignKey('CompanyName', models.PROTECT)
    project = models.ForeignKey('Project', models.PROTECT)
    contractor_id = models.CharField(max_length=30)
    id_valid_until = models.DateField()

    start_date= models.DateField(null=True)
    purpose = models.CharField(max_length=255)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT)
    vehicle_plate_no = models.CharField(max_length=20, db_index=True)
    brand = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=15)
    model = models.CharField(max_length=15, blank=True)

    or_number = models.CharField(max_length=15, db_index=True)
    or_date = models.DateField()
    cr_number = models.CharField(max_length=15, db_index=True)
    cr_date = models.DateField()
    vehicle_owner_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    transaction_reference_number = models.CharField(max_length=30, null=True)
    sticker_number = models.CharField(max_length=30, null=True)
    detail_reference_number = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT)

    # Used for acceptance / denial
    approved = models.BooleanField(default=False)
    cost = models.FloatField(null=True)
    flagged = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, null=True)
    id_pass_sticker = models.CharField(max_length=15, null=True)
    validity_months = models.IntegerField(null=True)
    valid_until = models.DateField(null=True)


#####################################
#
# Service Provider
#
#####################################
class ServiceVehicleStickers(models.Model):

    serviceprovidertype = models.CharField(max_length=30)

    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)
    companyname= models.CharField(max_length=250)

    spid_valid_until= models.DateField(null=True)
    esp_certificate= models.CharField(max_length=30)
    contractvalid_until= models.DateField(null=True)
    driveridnumber= models.CharField(max_length=30)

    start_date= models.DateField(null=True)
    end_date= models.DateField(null=True)
    purpose = models.CharField(max_length=255)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT)
    vehicle_plate_no = models.CharField(max_length=20, db_index=True)
    brand = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=15)
    model = models.CharField(max_length=15, blank=True)
    or_number = models.CharField(max_length=15, db_index=True)
    or_date = models.DateField()
    cr_number = models.CharField(max_length=15, db_index=True)
    cr_date = models.DateField()
    vehicle_owner_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    transaction_reference_number = models.CharField(max_length=30, null=True)
    sticker_number = models.CharField(max_length=30, null=True)
    detail_reference_number = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT)

    # Used for acceptance / denial
    approved = models.BooleanField(default=False)
    cost = models.FloatField(null=True)
    flagged = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, null=True)
    id_pass_sticker = models.CharField(max_length=15, null=True)
    validity_months = models.IntegerField(null=True)
    valid_until = models.DateField(null=True)


#####################################
#
#  Vendor
#
#####################################
class VendorVehicleStickers(models.Model):

    locator = models.ForeignKey('Locator', on_delete=models.PROTECT)
    companyname= models.CharField(max_length=250)
    start_date= models.DateField(null=True)
    end_date= models.DateField(null=True)
    purpose = models.CharField(max_length=255)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT)
    vehicle_plate_no = models.CharField(max_length=20, db_index=True)
    brand = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=15)
    model = models.CharField(max_length=15, blank=True)
    or_number = models.CharField(max_length=15, db_index=True)
    or_date = models.DateField()
    cr_number = models.CharField(max_length=15, db_index=True)
    cr_date = models.DateField()
    vehicle_owner_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    transaction_reference_number = models.CharField(max_length=30, null=True)
    sticker_number = models.CharField(max_length=30, null=True)
    detail_reference_number = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT)

    # Used for acceptance / denial
    approved = models.BooleanField(default=False)
    cost = models.FloatField(null=True)
    flagged = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, null=True)
    id_pass_sticker = models.CharField(max_length=15, null=True)
    validity_months = models.IntegerField(null=True)
    valid_until = models.DateField(null=True)

