from django.core.management.base import BaseCommand, CommandError
from api.models.stickers import LocatorVehicleStickers

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        loc_veh_stickers = LocatorVehicleStickers.objects.all().order_by('-start_date', 'last_name')[:10]
        for lvs in loc_veh_stickers:
            print("{}--{}, {}".format(lvs.start_date, lvs.last_name, lvs.first_name))