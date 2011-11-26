from datetime import datetime
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from const import Skills, LogTypes
from couchdbkit.ext.django.schema import *

DEFAULT_LOCATION=Point(42.359140, -71.093548) # 77 Mass Ave

class Character(models.Model):
    name = models.CharField(max_length=256)
    essence = models.IntegerField()
    loc = models.PointField(default=DEFAULT_LOCATION)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.essence)

    def write_log(self, type, **kwargs):
        l = CharLog(char_id=self.id, char_name=self.name, type=type)
        for k in kwargs:
            l.__setattr__(k, kwargs[k])
        l.save()

    def read_log(self, type=None):
        pass
    
    def heartbeat(self, loc):
        self.loc = loc
        self.save()
        self.write_log(LogTypes.HEARTBEAT, lat=loc.get_x(), long=loc.get_y())

    def get_location(self):
        l = CharLog.view("core/cur_loc", reduce=True, group=True, group_level=1).all()
        if not l: return None
        return l[0]['value']['lat'], l[0]['value']['long']


class CharLog(Document):
    char_id = IntegerProperty(required=True)
    char_name = StringProperty()
    type = StringProperty(required=True)
    lat = FloatProperty()
    long = FloatProperty()
    date = DateTimeProperty(default=datetime.utcnow)

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