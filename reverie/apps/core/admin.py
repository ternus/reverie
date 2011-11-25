__author__ = 'ternus'
from django.contrib.gis import admin
from models import Character, Item, AbstractItem
from django.contrib.gis.maps.google import GoogleMap
from django.conf import settings
from django.contrib.gis.geos import Point


class RModelAdmin(admin.OSMGeoAdmin):
    pnt = Point(x=-71.093, y=42.359, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords
    map_width = 800
    map_height = 800
    default_zoom = 17

admin.site.register(Character, RModelAdmin)
admin.site.register(Item, RModelAdmin)
admin.site.register(AbstractItem, RModelAdmin)



  