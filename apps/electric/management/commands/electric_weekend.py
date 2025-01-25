#!/usr/bin/env python3.13
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timesince import timesince
from django.utils.timezone import localtime
from ...models import ElectricUsage

class Command(BaseCommand):
    """
    Calculate weekday vs. weekend electric usage.
    """
    help = "Calculate weekday vs. weekend electric usage."

    def handle(self, *args, **options):

        now = localtime()
        num_weekday = 0
        num_weekend = 0
        usage_weekday = 0
        usage_weekend = 0

        # Get all electric usage from the database.
        usage = ElectricUsage.objects

        ## Format of minimum and maximum hour of electric usage.
        dt_fmt = "%c"

        # Minimum ("From") date.
        min_hour = usage.first().hour
        min_hour_local = localtime(min_hour)
        min_hour_ago = timesince(min_hour_local)
        min_hour_fmt = min_hour_local.strftime(dt_fmt)
        self.stdout.write(self.style.SUCCESS(
            f"From:\t\t{min_hour_fmt} ({min_hour_local}) [{min_hour_ago} ago]"
        ))

        # Maximum ("To") date.
        max_hour = usage.last().hour
        max_hour_local = localtime(max_hour)
        max_hour_ago = timesince(max_hour_local)
        max_hour_fmt = max_hour_local.strftime(dt_fmt)
        self.stdout.write(self.style.SUCCESS(
            f"To:\t\t{max_hour_fmt} ({max_hour_local}) [{max_hour_ago} ago]"
        ))

        ## Iterate all electric usage data, calculating weekend vs. weekday kWh.
        for row in usage.all():

            # Weekend.
            hour_local = localtime(row.hour)
            hour_dow = hour_local.strftime("%A")
            if hour_dow in ("Saturday", "Sunday"):
                num_weekend += 1
                usage_weekend += row.kwh

            # Weekday.
            else:
                num_weekday += 1
                usage_weekday += row.kwh


        ## Show usage separately for weekdays and weekends.

        # Weekdays.
        num_weekday_ago = timesince(now - timedelta(hours=num_weekday), now)
        average_weekday = usage_weekday / num_weekday
        self.stdout.write(self.style.SUCCESS(
            f"Weekdays:\t{'{0:,.4f}'.format(usage_weekday)} total kWh /"
            f" {'{0:,}'.format(num_weekday)} total hours ="
            f" average {'{0:,.4f}'.format(average_weekday)} kWh"
            f" over {num_weekday_ago}."
        ))

        # Weekends.
        num_weekend_ago = timesince(now - timedelta(hours=num_weekend), now)
        average_weekend = usage_weekend / num_weekend
        self.stdout.write(self.style.SUCCESS(
            f"Weekends:\t{'{0:,.4f}'.format(usage_weekend)} total kWh /"
            f" {'{0:,}'.format(num_weekend)} total hours ="
            f" average {'{0:,.4f}'.format(average_weekend)} kWh"
            f" over {num_weekend_ago}."
        ))

        # Show total usage, number of hours, and average usage per hour.
        total_hours = usage.count()
        total_ago = timesince(now - timedelta(hours=total_hours), now)
        total_usage = usage_weekday + usage_weekend
        average_kwh = total_usage / total_hours
        self.stdout.write(self.style.SUCCESS(
            f"Total:\t\t{'{0:,.4f}'.format(total_usage)} kWh /"
            f" {'{0:,}'.format(total_hours)} hours ="
            f" average {'{0:,.4f}'.format(average_kwh)} kWh"
            f" over {total_ago}."
        ))
