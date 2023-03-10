import logging

from django.http import HttpResponse
from django.http import JsonResponse

from .models import Fruit

logger = logging.getLogger()
logger.info('loading views')


# Create your views here.
def index(request):
    """
    Return the main page
    """
    logger.info('getting all the fruits')
    all_fruits = Fruit.objects.all()
    all_fruits_str = 'This is the Django app. Found these fruits in the database: ' + ' '.join(
        [x.type for x in all_fruits])
    logger.info('returning all the fruits')
    return HttpResponse(all_fruits_str)


# Create your views here.
def health(request):
    """
    Return the health
    """

    heath = {'running': True}
    return JsonResponse(status=200, data=heath)
