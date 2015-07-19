from main.models import MorirCause, Morir


def causes_menu(request):
    causes_menu = MorirCause.objects.all()[:5]
    return {'causes_menu': causes_menu}


def causes_processor(request):
    return {'causes': MorirCause.objects.all()}