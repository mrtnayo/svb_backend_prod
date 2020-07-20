from django.utils.translation import gettext_lazy as _


ERRORS_MAP = {
    5000: {
        'message': 'Server error.',
        'status': 500,
        'description': _('Error producido por el servidor.')
    },
    4000: {
        'message': 'Validation error.',
        'status': 400,
        'description': _('Error producido por request erróneo.')
    },
    4010: {
        'message': 'Authentication error.',
        'status': 401,
        'description': _('Error producido por credenciales fallidas.')
    },
    4040: {
        'message': 'Not found error.',
        'status': 404,
        'description': _('Error producido por no encontrarse el recurso solicitado.')
    }
}
