from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.db.models import Sum

from collections import OrderedDict

import re

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from main.models import Morir, MorirCause
from main.forms import CauseSearchForm

# Create your views here.


# class CauseSearchView(FormView):
#     model = Morir
#     template_name = 'cause_search.html'
#     form_class = CauseSearchForm
#     context_object_name = "death"

#     def get_cause_data():
#         context = super(CauseDetailView, self).get_cause_data(**kwargs)
#         context['causes'] = MorirCause.objects.all()
#         return context

#     def form_valid(self, form):
#         request_context = RequestContext(self.request)
#         context = {}
#         cause = form.cleaned_data['cause']
#         year = form.cleaned_data['year']
#         context['form'] = form
#         context['cause_list'] = MorirCause.objects.filter(cause__startswith=cause, morir__year__startswith=year)
#         return render_to_response('cause_search.html', context, context_instance=request_context)


class CauseListView(ListView):
    model = MorirCause
    template_name = "cause_list.html"
    context_object_name = "cause_list"


class CauseDetailView(DetailView):
    """extends this view to add cause to the Morir details"""
    model = Morir
    template_name = "cause_detail.html"
    context_object_name = "cause"

    def get_cause_data():
        context = super(CauseDetailView, self).get_cause_data(**kwargs)
        context['causes'] = MorirCause.objects.all()
        return context


def cause_search(request):
    context = {}
    request_context = RequestContext(request)
    # print request.method
    if request.method == 'POST':
        form = CauseSearchForm(request.POST)
        context['form'] = form
        if form.is_valid():
            cause = form.cleaned_data['cause']
            sex = form.cleaned_data['sex']
            year = form.cleaned_data['year']
            context['cause_list'] = Morir.objects.filter(cause__cause=cause, year=year, sex=sex)
            print context['cause_list'], cause

            context['valid'] = "Well done. Valid choice. But everyone's still dead."
            
            return render_to_response("cause_search.html", context, context_instance=request_context)

        else:
            context['valid'] = form.errors

    else:
        form = CauseSearchForm()
        context['form'] = form

    return render_to_response("cause_search.html", context, context_instance=request_context)


def template_view(request):

    context = {}
    deaths_dict = {}

    death_types = MorirCause.objects.all().order_by('cause')
    # all_deaths = Morir.objects.all().order_by('year').reverse()

    for death_type in death_types:
        all_deaths = death_type.morir_set.all()

        all_deaths_total = death_type.morir_set.all().aggregate(Sum('number_of_deaths'))
        all_deaths_total_f = death_type.morir_set.filter(sex="Females").aggregate(Sum('number_of_deaths'))
        all_deaths_total_m = death_type.morir_set.filter(sex="Males").aggregate(Sum('number_of_deaths'))
        # print type(all_deaths_total_m['number_of_deaths__sum'])

        if (all_deaths_total_m['number_of_deaths__sum']) is None:
            (all_deaths_total_m['number_of_deaths__sum']) = 0

        if (all_deaths_total_f['number_of_deaths__sum']) is None:
            (all_deaths_total_f['number_of_deaths__sum']) = 0


        deaths_dict[death_type.cause] = {"all_deaths": all_deaths, 
                                                                "death_total": all_deaths_total['number_of_deaths__sum'],
                                                                "all_females": all_deaths_total_f['number_of_deaths__sum'],
                                                                "all_males": all_deaths_total_m['number_of_deaths__sum']
                                                                }

    context['death_types'] = deaths_dict
    return render(request, 'template_view.html', context)


def all_deaths_view(request):

    context = {}
    deaths_dict = OrderedDict()

    death_types = MorirCause.objects.all().order_by('cause')
    # all_deaths = Morir.objects.all().order_by('year').reverse()

    for death_type in death_types:
        all_deaths = death_type.morir_set.all()

        all_deaths_total = death_type.morir_set.all().aggregate(Sum('number_of_deaths'))
        all_deaths_total_f = death_type.morir_set.filter(sex="Females").aggregate(Sum('number_of_deaths'))
        all_deaths_total_m = death_type.morir_set.filter(sex="Males").aggregate(Sum('number_of_deaths'))
        # print type(all_deaths_total_m['number_of_deaths__sum'])

        if (all_deaths_total_m['number_of_deaths__sum']) is None:
            (all_deaths_total_m['number_of_deaths__sum']) = 0

        if (all_deaths_total_f['number_of_deaths__sum']) is None:
            (all_deaths_total_f['number_of_deaths__sum']) = 0


        deaths_dict[death_type.cause] = {"all_deaths": all_deaths, 
                                                                "death_total": all_deaths_total['number_of_deaths__sum'],
                                                                "all_females": all_deaths_total_f['number_of_deaths__sum'],
                                                                "all_males": all_deaths_total_m['number_of_deaths__sum']
                                                                }

    context['death_types'] = deaths_dict




        # import pdb; pdb.set_trace()
        # total_numbers = Morir.total_numbers()
        # death_type.cause = {death_type.cause: all_deaths}
        # deaths_dict.update(death_type.cause)


        # for death in all_deaths:
        #     if death_type.id == death.cause_id:
        #         deathcause = [death.year, death.number_of_deaths, death.sex]
    # print death_type, deathcause

    return render(request, 'all_deaths.html', context)




        # if death.sex == 'Males':
        #     death_types.cause = {all_deaths.cause: [death.year, death.number_of_deaths, death.sex]}
        # deaths_dict.update(death.cause)
        # if death.sex == 'Females':
        #     death_types.cause = {all_deaths.cause: [death.year, death.number_of_deaths, death.sex]}
        # deaths_dict.append(death.cause)


    context['all_deaths'] = death_types

    # deaths = Morir.objects.all()

    # deaths_dict = {}

    # for death in deaths:
    #     if death.sex == "Males":
    #         death.cause_of_death = {death.cause_of_death: [death.year, death.number_of_deaths, death.sex]}
    #     if death.sex == "Females":
    #         death.cause_of_death = {death.cause_of_death: [death.year, death.number_of_deaths, death.sex]}
    #     deaths_dict.update(death.cause_of_death)

    # context['deaths'] = deaths_dict

    return render(request, 'template_view.html', context)




def first_view(request):
    deaths = Morir.objects.all()

    deaths_list = []

    for death in deaths:
    #     numbers = Morir.objects.all().order_by('number_of_deaths')
    #     for number in numbers:
        the_year = death.year
        the_number = death.number_of_deaths
        the_cause = death.cause
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