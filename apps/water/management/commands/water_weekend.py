#!/usr/bin/env python3.13
from django.core.management.base import BaseCommand
from django.utils.timesince import timesince
from django.utils.timezone import localtime, timedelta
from ...models import WaterUsage

class Command(BaseCommand):
    """
    Calculate weekday vs. weekend water usage.
    """
    help = "Calculate weekday vs. weekend water usage."

    def handle(self, *args, **options):

        now = localtime()
        num_weekday = 0
        num_weekend = 0
        usage_weekday = 0
        usage_weekend = 0

        # Get all water usage from the database.
        usage = WaterUsage.objects

        ## Show/format the minimum and maximum dates of water usage.
        dt_fmt = "%A, %B %d, %Y"

        # Minimum ("From") date.
        min_row = usage.first()
        min_day = min_row.day
        self.stdout.write(self.style.SUCCESS(
            f'From:\t\t{min_day.strftime(dt_fmt)} ({min_day})'
        ))

        # Maximum ("To") date.
        max_row = usage.last()
        max_day = max_row.day
        self.stdout.write(self.style.SUCCESS(
            f'To:\t\t{max_day.strftime(dt_fmt)} ({max_day})'
        ))

        ## Iterate all water usage data, calculating weekend vs. weekday usage.
        for row in usage.all():

            # Weekend.
            if row.day.strftime('%A') in ('Saturday', 'Sunday'):
                num_weekend += 1
                usage_weekend += row.gallons

            # Weekday.
            else:
                num_weekday += 1
                usage_weekday += row.gallons


        ## Show usage separately for weekdays and weekends.

        # Weekdays.
        num_weekday_ago = timesince(now - timedelta(days=num_weekday), now)
        average_weekday = usage_weekday / num_weekday
        self.stdout.write(self.style.SUCCESS(
            f"Weekdays:\t{'{0:,.4f}'.format(usage_weekday)} gallons /"
            f" {num_weekday} week days ="
            f" average {'{0:,.4f}'.format(average_weekday)} gallons"
            f" over {num_weekday_ago}."
        ))

        # Weekends.
        num_weekend_ago = timesince(now - timedelta(days=num_weekend), now)
        average_weekend = usage_weekend / num_weekend
        self.stdout.write(self.style.SUCCESS(
            f"Weekends:\t{'{0:,.4f}'.format(usage_weekend)} gallons /"
            f" {num_weekend} weekend days ="
            f" average {'{0:,.4f}'.format(average_weekend)} gallons"
            f" over {num_weekend_ago}."
        ))

        # Show total usage, number of days, and average usage per day.
        total_days = usage.count()
        total_ago = timesince(now - timedelta(days=total_days), now)
        total_usage = usage_weekday + usage_weekend
        average_gallons = total_usage / total_days
        self.stdout.write(self.style.SUCCESS(
            f"Total:\t\t{'{0:,.4f}'.format(total_usage)} gallons /"
            f" {total_days} days ="
            f" average {'{0:,.4f}'.format(average_gallons)} gallons"
            f" over {total_ago}."
        ))
