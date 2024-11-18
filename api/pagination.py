from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class CustomPageNumberPagination(PageNumberPagination):
    #default_page_size = 10; 
    default_page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
