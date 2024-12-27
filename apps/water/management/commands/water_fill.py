from csv import DictReader
from datetime import date
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from ...models import WaterUsage


class Command(BaseCommand):
    """
    Import water usage data to the database,
    from comma-separated values ("CSV") file.
    """
    help = "Import water usage data."

    def handle(self, *args, **options):

        num_created = 0
        try:
            # Open comma-separated values ("CSV") file of water usage data.
            with open(file=settings.WATER_FILENAME, mode="r") as csv_fh:

                # Iterate each row of the CSV file.
                for csv_row in DictReader(csv_fh):

                    # Ensure the row is measuring gallons (not CCFs, etc.)
                    assert csv_row[" Units"] == " Gallons", "Invalid unit!"

                    # Parse the date column within each CSV row.
                    date_parts = csv_row[" Time Interval"].strip().split('/')
                    date_iso = \
                        f"{date_parts[2]}-{date_parts[0]}-{date_parts[1]}"

                    # Create dictionary mapping date to water usage in gallons.
                    usage = {
                        "day": date.fromisoformat(date_iso),
                        "gallons": float(csv_row[" Consumption"].strip())
                    }

                    # Update or create the water usage object in the database.
                    obj, created = WaterUsage.objects.update_or_create(
                        **usage,
                        defaults=usage
                    )

                    # Show any newly created water usage database objects.
                    if created:
                        num_created += 1
                        self.stdout.write(self.style.SUCCESS(
                            f"Created:\t{obj.day.strftime('%A, %B %d, %Y')}"
                            f" ({obj.day}) [{obj.gallons} gallons]"
                        ))

            # List total count of newly created water usage database objects.
            if num_created > 0:
                self.stdout.write(self.style.SUCCESS(
                    f"Total:\t\t{num_created}"
                ))
            self.stdout.write(self.style.SUCCESS("Done."))

        except Exception as exc:
            raise CommandError(exc)
