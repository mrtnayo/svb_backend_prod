from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.common.utils import STATUS_MAP
from apps.common.utils import send_error
from apps.rest_auth.serializers import UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    Endpoint de login, recibe username y password y devuelve el token
    de autenticación de acceso al API.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return send_error(code=4010, msg='Please provide both username and password.')
    user = authenticate(username=username, password=password)
    if not user:
        return send_error(code=4010, msg='Invalid credentials.')
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key
    })


@swagger_auto_schema(
    methods=['post'],
    request_body=UserSerializer
)
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registration(request):
    """
    Endpoint de registro, se ingresa username, password e email(opcional)
    y devuelve el usuario.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=STATUS_MAP[201])
    else:
        return send_error(code=4000, msg='Invalid request fields.', data=serializer.errors)


@swagger_auto_schema(
    methods=['get'],
    responses={204: None}
)
@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def logout(request):
    """
    Endpoint de logout, elimina el token del usuario.
    """
    request.user.auth_token.delete()
    return Response(status=STATUS_MAP[204])
