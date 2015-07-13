from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from main.models import Morir

# Create your views here.

def first_view(request):
    deaths = Morir.objects.all()

    deaths_list = []

    for death in deaths:
    #     numbers = Morir.objects.all().order_by('number_of_deaths')
    #     for number in numbers:
        the_year = death.year
        the_number = death.number_of_deaths
        the_cause = death.cause_of_death
        the_sex = death.sex

        text_block = """

            <strong>{0}</strong> ::: {1} ::: <strong>{2}</strong> ::: {3}</br>

            """.format(the_cause, the_year, the_number, the_sex)

        deaths_list.append(text_block)

    return HttpResponse(deaths_list)


    # text_string = ''

    # deaths_list = []
    # for death in deaths:
    #     numbers = Morir.objects.order_by('number_of_deaths').reverse()
    #     for number in numbers:
    #         text_string += "%s</br>" % number.number_of_deaths

    # return HttpResponse(text_string)

    # for year in years:
    #     if year == 2001










# def first_view(request):
#     city_list = []
#     for state in State.objects.all():
#         cities = state.city_set.filter(name__startswith="A")
#         for city in cities:
#             the_state = state
#             the_city_name = city.name
#             the_zip_code = city.zip_code

#             text_block = """

#             {0} - <strong>{1}</strong> - {2}<br>

#             """.format(the_state, the_city_name, the_zip_code)
#             city_list.append(text_block)

#     return HttpResponse(city_list)