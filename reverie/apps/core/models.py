from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

DEFAULT_LOCATION=Point(42.359140, -71.093548)

class Character(models.Model):
    name = models.CharField(max_length=256)
    exp = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    loc = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.exp)
    
class Item(models.Model):
    """ Represents an *instance* of an item.  We'll want to have more than one of any given item."""
    owner = models.ForeignKey('Character', null=True, blank=True)
    base = models.ForeignKey('AbstractItem')
    loc = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        if self.owner:
            return "%s (owned by %s)" % (self.base.name, self.owner)
        else:
            return "%s (at %s)" % (self.base.name, self.loc)

class AbstractItem(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return "<%s>" % self.name