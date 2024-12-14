#!/usr/bin/env python3.13
from django.core.management.base import BaseCommand
from ...models import ElectricUsage

class Command(BaseCommand):
    """
    Calculate weekday vs. weekend electric usage.
    """
    help = "Calculate weekday vs. weekend electric usage."

    def handle(self, *args, **options):

        num_weekday = 0
        num_weekend = 0
        usage_weekday = 0
        usage_weekend = 0

        # Get all electric usage from the database.
        usage = ElectricUsage.objects

        ## Show/format the minimum and maximum date hour of electric usage.
        dt_fmt = "%c"

        # Minimum ("From") date.
        min_date = usage.first()
        self.stdout.write(self.style.SUCCESS(
            f'From:\t\t{min_date.hour.strftime(dt_fmt)} ({min_date.hour})'
        ))

        # Maximum ("To") date.
        max_date = usage.last()
        self.stdout.write(self.style.SUCCESS(
            f'To:\t\t{max_date.hour.strftime(dt_fmt)} ({max_date.hour})'
        ))

        ## Iterate all electric usage data, calculating weekend vs. weekday usage.
        for day in usage.all():

            # Weekend.
            if day.hour.strftime('%A') in ('Saturday', 'Sunday'):
                num_weekend += 1
                usage_weekend += day.kwh

            # Weekday.
            else:
                num_weekday += 1
                usage_weekday += day.kwh


        ## Show usage separately for weekdays and weekends.

        # Weekdays.
        average_weekday = usage_weekday / num_weekday
        self.stdout.write(self.style.SUCCESS(
            f"Weekdays:\t{'{0:,.4f}'.format(usage_weekday)} total kWh /"
            f" {'{0:,}'.format(num_weekday)} total hours ="
            f" average {'{0:,.4f}'.format(average_weekday)} kWh."
        ))

        # Weekends.
        average_weekend = usage_weekend / num_weekend
        self.stdout.write(self.style.SUCCESS(
            f"Weekends:\t{'{0:,.4f}'.format(usage_weekend)} total kWh /"
            f" {'{0:,}'.format(num_weekend)} total hours ="
            f" average {'{0:,.4f}'.format(average_weekend)} kWh."
        ))

        # Show total usage, number of hours, and average usage per hour.
        total_hours = usage.count()
        total_usage = usage_weekday + usage_weekend
        average_kwh = total_usage / total_hours
        self.stdout.write(self.style.SUCCESS(
            f"Total:\t\t{'{0:,.4f}'.format(total_usage)} kWh /"
            f" {'{0:,}'.format(total_hours)} hours ="
            f" average {'{0:,.4f}'.format(average_kwh)} kWh."
        ))
