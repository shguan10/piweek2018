from django.contrib.admin import AdminSite
from django.contrib.admin import site
from snowflake import models


class SnowflakeSite(AdminSite):
    site_title = "Snowflake"
    site_header = "Snowflake"
    index_title = "Snowflake"

    def __init__(self, *args, **kwargs):
        super(SnowflakeSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

site = SnowflakeSite()
site.register(models.Fridge, models.FridgeAdmin)
site.register(models.Item, models.ItemAdmin)
