#!/usr/bin/env python3.13
from django.core.management.base import BaseCommand
from ...models import WaterUsage

class Command(BaseCommand):
    """
    Calculate weekday vs. weekend water usage.
    """
    help = "Calculate weekday vs. weekend water usage."

    def handle(self, *args, **options):

        num_weekday = 0
        num_weekend = 0
        usage_weekday = 0
        usage_weekend = 0

        # Get all water usage from the database.
        usage = WaterUsage.objects

        ## Show/format the minimum and maximum dates of water usage.
        dt_fmt = "%A, %B %d, %Y"

        # Minimum ("From") date.
        min_date = usage.first()
        self.stdout.write(self.style.SUCCESS(
            f'From:\t\t{min_date.date.strftime(dt_fmt)} ({min_date.date})'
        ))

        # Maximum ("To") date.
        max_date = usage.last()
        self.stdout.write(self.style.SUCCESS(
            f'To:\t\t{max_date.date.strftime(dt_fmt)} ({max_date.date})'
        ))

        ## Iterate all water usage data, calculating weekend vs. weekday usage.
        for day in usage.all():

            # Weekend.
            if day.date.strftime('%A') in ('Saturday', 'Sunday'):
                num_weekend += 1
                usage_weekend += day.gallons

            # Weekday.
            else:
                num_weekday += 1
                usage_weekday += day.gallons


        ## Show usage separately for weekdays and weekends.

        # Weekdays.
        average_weekday = usage_weekday / num_weekday
        self.stdout.write(self.style.SUCCESS(
            f"Weekdays:\t{'{0:,.4f}'.format(usage_weekday)} gallons /"
            f" {num_weekday} week days ="
            f" average {'{0:,.4f}'.format(average_weekday)} gallons."
        ))

        # Weekends.
        average_weekend = usage_weekend / num_weekend
        self.stdout.write(self.style.SUCCESS(
            f"Weekends:\t{'{0:,.4f}'.format(usage_weekend)} gallons /"
            f" {num_weekend} weekend days ="
            f" average {'{0:,.4f}'.format(average_weekend)} gallons."
        ))

        # Show total usage, number of days, and average usage per day.
        total_days = usage.count()
        total_usage = usage_weekday + usage_weekend
        average_gallons = total_usage / total_days
        self.stdout.write(self.style.SUCCESS(
            f"Total:\t\t{'{0:,.4f}'.format(total_usage)} gallons /"
            f" {total_days} days ="
            f" average {'{0:,.4f}'.format(average_gallons)} gallons."
        ))
