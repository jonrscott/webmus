from datetime import datetime, date

from .models import Gig


def monthyear_to_str(month, year):
    d = datetime(year, month, 1)
    return d.strftime("%B %Y")


def get_gigs_by_month():
    result = []
    currentmonthyear = None
    currentmonthgigs = []
    for gig in Gig.objects.filter(start_date__gte=date.today()).order_by(
        'start_date', 'start_time'):
        gigmonthyear = monthyear_to_str(gig.start_date.month, gig.start_date.year)
        if gigmonthyear != currentmonthyear:
            if currentmonthgigs:
                result.append((currentmonthyear, currentmonthgigs))
                currentmonthgigs = []
            currentmonthyear = gigmonthyear
        currentmonthgigs.append(gig)
    if currentmonthgigs:
        result.append((currentmonthyear, currentmonthgigs))
    return result
