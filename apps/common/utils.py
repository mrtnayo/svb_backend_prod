# -*- coding: utf-8 -*-
import random
import string

from django.utils.text import slugify
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
)

from apps.common.errors import ERRORS_MAP


STATUS_MAP = {
    200: HTTP_200_OK,
    201: HTTP_201_CREATED,
    204: HTTP_204_NO_CONTENT,
    400: HTTP_400_BAD_REQUEST,
    401: HTTP_401_UNAUTHORIZED,
    404: HTTP_404_NOT_FOUND,
    500: HTTP_500_INTERNAL_SERVER_ERROR
}


class DefaultPagination(PageNumberPagination):
    """
    Customizando paginador por defecto.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


def send_response(msg=None, data=None, status=200):
    response = {
        'success': True,
        'msg': msg,
        'data': data
    }
    return Response(response, status=STATUS_MAP.get(status))


def send_error(code=None, msg=None, data=None):
    response = {
        'code': code,
        'error': ERRORS_MAP[code]['message'],
        'message': msg,
        'description': ERRORS_MAP[code]['description'],
        'errors': data
    }
    return Response(response, status=ERRORS_MAP[code]['status'])


def random_string_generator(size=10,
                            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
