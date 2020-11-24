from django.db import models


class Color(models.Model):
    """ Responsible by define Color table fields """
    name = models.CharField(max_length=100, unique=True)
    hex_code = models.CharField(max_length=7, unique=True)

    class Meta:
        """ Define Color table name """
        db_table = "Colors"

    def _str_(self):
        """ get _str_"""
        return self.name
