from django.core.management.base import BaseCommand
from api.models.stickers import LocatorVehicleStickers
from datetime import datetime
import os
import xlsxwriter


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    start_date = datetime(year=2022, month=1, day=1)
    end_date = datetime(year=2022, month=12, day=31)

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        the_folder = "/home/rolan/data1/Dropbox/Temp/fpip-sheets"
        the_file = os.path.join(the_folder, "LocStickers_2022.xlsx")
        workbook = xlsxwriter.Workbook(filename=the_file)
        worksheet = workbook.add_worksheet("FPIP Locator Stickers")

        loc_veh_stickers = LocatorVehicleStickers.objects.all()\
            .filter(created_date__range=(self.start_date, self.end_date))\
            .order_by('created_date', '-start_date', 'last_name')

        print("{}:Writing {} rows...".format(datetime.now().strftime("%H:%M:%S"), loc_veh_stickers.count()))
        write_loc_stickers(loc_veh_stickers, worksheet)
        workbook.close()
        print("{}:Done.".format(datetime.now().strftime("%H:%M:%S")))


def write_loc_stickers(loc_veh_stickers_set, worksheet):
    """

    :param loc_veh_stickers_set:
    :param worksheet:
    :return:
    """
    write_header(worksheet)
    for row_no, ls in enumerate(loc_veh_stickers_set):
        write_row(worksheet, row_no+1, ls)


def write_header(worksheet):
    """

    :param worksheet:
    :return:
    """
    worksheet.write("A1", "No.")
    worksheet.write("B1", "Sticker No.")
    worksheet.write("C1", "Vehicle PlateNo.")
    worksheet.write("D1", "Date Applied")
    worksheet.write("E1", "Valid Until")
    worksheet.write("F1", "Locator")
    worksheet.write("G1", "Applicant")
    worksheet.write("H1", "Driver Last Name")
    worksheet.write("I1", "Driver First Name")
    worksheet.write("J1", "Transaction Number")
    worksheet.write("K1", "Remarks")
    worksheet.write("L1", "Approved")


def write_row(worksheet, row_no:int, ls: LocatorVehicleStickers):
    """

    :param row_no:
    :param ls:
    :return:
    """
    # "Row No."
    worksheet.write(row_no, 0, row_no)
    # "Sticker No."
    worksheet.write(row_no, 1, ls.sticker_number)
    # "Vehicle PlateNo."
    worksheet.write(row_no, 2, ls.vehicle_plate_no)
    # "Date Applied"
    worksheet.write(row_no, 3, ls.created_date.strftime("%m-%d-%Y"))
    # "Valid Until"
    worksheet.write(row_no, 4, ls.valid_until.strftime("%m-%d-%Y"))
    # "Locator"
    worksheet.write(row_no, 5, ls.locator.name)
    # "Applicant"
    worksheet.write(row_no, 6, ls.created_by.first_name + ls.created_by.last_name)
    # "Driver Last Name"
    worksheet.write(row_no, 7, ls.last_name)
    # "Driver First Name"
    worksheet.write(row_no, 8, ls.first_name)
    # "Transaction Number"
    worksheet.write(row_no, 9, ls.transaction_reference_number)
    # "Remarks"
    worksheet.write(row_no, 10, ls.remarks)
    worksheet.write(row_no, 11, "Yes" if ls.approved else "No")
    if row_no % 100 == 0:
        print("row_no={}".format(row_no))
