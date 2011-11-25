# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Character, Item

def main_view(request, template="char.html"):
    char_name = request.GET.get("char", None)
    if not char_name: char_name = "test"
    char = Character.objects.get(name="test")

    items = Item.objects.distance(char.loc)
    return render_to_response(template, {"char": char, "items": items}, context_instance=RequestContext(request))