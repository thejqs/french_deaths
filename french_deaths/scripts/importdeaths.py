#!/usr/bin/env python

import csv
import os
import sys
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "french_deaths.settings")
sys.path.append("..")

from django.db.models import Q
from main.models import Morir, MorirCause


french_deaths_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "french_deaths.csv")

# print "%s french_deaths.csv" % os.path.dirname(os.path.abspath(__file__))
# print "{0}/french_deaths.csv".format(os.path.dirname(os.path.abspath(__file__)))

with open(french_deaths_csv, 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    Morir.objects.all().delete()
    MorirCause.objects.all().delete()

    for row in reader:
        cause = re.sub(r'\(.*?\)', '', row['ICD10'])
        cause = cause.replace('excluding S00-T98', '')
        new_cause, created = MorirCause.objects.get_or_create(cause=cause)
        new_cause.save()

        new_death = Morir.objects.create(
            number_of_deaths=row['Value'].replace(':', '0').replace(' ', ''),
            year=row["TIME"],
            sex=row["SEX"]
        )
        new_death.cause = new_cause
        new_death.save()
