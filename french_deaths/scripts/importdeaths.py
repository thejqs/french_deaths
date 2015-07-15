#!/usr/bin/env python

import csv
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "french_deaths.settings")

sys.path.append("..")

from django.db.models import Q

from main.models import Morir, MorirCause

# deaths = Morir.objects.all()

# for death in deaths:
#     print death.number_of_deaths

french_deaths_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "french_deaths.csv")

# print "%s french_deaths.csv" % os.path.dirname(os.path.abspath(__file__))

# print "{0}/french_deaths.csv".format(os.path.dirname(os.path.abspath(__file__)))

csv_file = open(french_deaths_csv, 'r')

reader = csv.DictReader(csv_file)

# Morir.objects.all().delete()
# MorirCause.objects.all().delete()

for row in reader:
    new_cause, created = MorirCause.objects.get_or_create(cause=row["ICD10"])
    new_cause.save()

    new_death, created=Morir.objects.get_or_create(
        number_of_deaths=row["Value"].replace(':', '0').replace(' ', ''),
        year=row["TIME"],
        sex=row["SEX"]
    )
    new_death.cause = new_cause
    new_death.save()


csv_file.close()
