from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from config import settings
from core.models import Shop
from core.tasks import create_shops


def index_view(request):
    shops_location = Shop.objects.values_list("location", "address")
    coordinates = []
    for index, location in enumerate(shops_location):
        coordinates.append({})
        coordinates[index]["latitude"], coordinates[index]["longitude"] = location[0].split(",")
    return render(
        request,
        template_name="core/index.html",
        context={
            "title": "Main page",
            "data": coordinates,
            "google_maps_api_key": settings.base.GOOGLE_MAPS_API_KEY,
            "addresses": list(shops_location),
        },
    )


def generate_shops(request, **kwargs):
    count = kwargs.get("count")
    create_shops.delay(count)
    message = "Shop created"
    return render(
        request,
        template_name="catalogue/generate_data.html",
        context={"title": "Generate part", "message": message},
    )


class PageNotFound(TemplateView):
    template_name = "core/404.html"
    extra_context = {"title": "Page not found"}


class Forbidden(TemplateView):
    template_name = "core/forbidden.html"
    extra_context = {"title": "Forbidden"}


# def add_to_cart(request, **kwargs):
#     print(kwargs)
#     CartItem.objects.create(part=kwargs.get('part_number'), quantity=kwargs.get('quantity')),
#                             # cart_id=kwargs.get('user_cart'))
# return HttpResponseRedirect(reverse("parts"))

# return render(request, template_name="students_create.html", context={"response": response})
#
