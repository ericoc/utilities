#!/usr/bin/env python3.13
from django.core.management.base import BaseCommand
from ...models import GasUsage

class Command(BaseCommand):
    """
    Calculate weekday vs. weekend natural gas usage.
    """
    help = "Calculate weekday vs. weekend natural gas usage."

    def handle(self, *args, **options):

        num_weekday = 0
        num_weekend = 0
        usage_weekday = 0
        usage_weekend = 0
