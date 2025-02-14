from django.contrib.auth import logout
from ninja import Router
from ninja.security import SessionAuth

router = Router()


@router.post('/logout', summary='Logout using SessionID', auth=SessionAuth)
def session_logout(request):
    logout(request)
    return {'details': 'User logout successful'}