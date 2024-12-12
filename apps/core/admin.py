from django.contrib import admin
from django.contrib.auth.admin import Group


# Set admin header and title text.
admin.site.site_header = admin.site.site_title = "Utilities"
admin.site.index_title = "Usage"

# Disable original admin Group model.
admin.site.unregister(Group)
