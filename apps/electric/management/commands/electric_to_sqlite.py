#!/usr/bin/env python3
from sys import exit
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.management.base import BaseCommand
from django.utils.translation import ngettext

from ...models import ElectricUsage as model


class Command(BaseCommand):
    """
    Export usage data from PostgreSQL to SQLite.
    """
    help = "Convert latest electric gas usage for Datasette."

    def handle(self, *args, **options):

        # Find latest in SQLite.
        latest = None
        try:
            latest = model.objects.using("sqlite"). \
                order_by("-hour").first().hour
            self.stdout.write(
                self.style.SUCCESS(
                    f"Latest SQLite: {latest.strftime(settings.TIME_FMT)}"
                )
            )

        # Warn if nothing was found in SQLite.
        except (model.DoesNotExist, AttributeError):
            self.stdout.write(
                self.style.WARNING("Nothing in SQLite!\n")
            )

        # Gather and count from PostgreSQL, based on latest in SQLite.
        usage = model.objects
        if latest:
            usage = usage.filter(pk__gt=latest)
        usage = usage.order_by("hour")
        num_found = usage.count()

        # Exit if nothing was found to export.
        if num_found == 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{num_found} {model._meta.verbose_name_plural} found for"
                    f" export to {settings.DATABASES['sqlite']['NAME']}."
                )
            )
            exit(0)

        # List count found, and where they are being exported to.
        self.stdout.write(
            self.style.NOTICE(
                f"Exporting {intcomma(num_found)} {ngettext(
                    singular="record",
                    plural="records",
                    number=num_found
                )} to {settings.DATABASES['sqlite']['NAME']}.\n"
            )
        )

        # Iterate each record found in PostgreSQL, for export to SQLite.
        created = 0
        skipped = 0
        for (count, row_obj) in enumerate(usage.all(), start=1):

            # Create a dictionary from PostgreSQL object.
            row_dict = vars(row_obj)
            hour = row_dict.pop("hour")
            del row_dict["_state"]

            # Create record in SQLite, using the PostgreSQL dictionary.
            (obj, ctd) = model.objects.using("sqlite").update_or_create(
                hour=hour,
                defaults=row_dict,
                create_defaults=row_dict
            )

            # List and count whether each was created in SQLite, or skipped.
            if ctd:
                msg = self.style.SUCCESS(f"Created: {obj}\n")
                created += 1
            else:
                msg = self.style.NOTICE(f"Skipping: {obj}\n")
                skipped += 1
            self.stdout.write(msg)

        # Show final created/skipped, and total.
        self.stdout.write(
            self.style.SUCCESS(
                f"\n{intcomma(created)} created.\n"
                f"{intcomma(skipped)} skipped.\n"
                f"{intcomma(created+skipped)} total.\nDone!"
            )
        )
