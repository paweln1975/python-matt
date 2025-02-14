from django.contrib.auth import authenticate, login
from ninja import Router, Schema

router = Router()

class LoginRequest(Schema):
    username: str
    password: str

class LoginResponse(Schema):
    sessionid: str

class UnauthorizedResponse(Schema):
    status_code: int = 401
    reason: str = 'Unauthorized'
    details: str


@router.post('/login', response={
    200: LoginResponse,
    401: UnauthorizedResponse},
 summary='Authenticate using Username and Password to get SessionID')
def session_login(request, data: LoginRequest):
    username = data.username
    password = data.password
    if user := authenticate(request, username=username, password=password):
        login(request, user)
        return 200, {'sessionid': request.session.session_key}
    else:
        return 401, {'details': 'Invalid username or password'}