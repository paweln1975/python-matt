from django.contrib.sessions.models import Session
from ninja.security import APIKeyHeader


class SessionAuth(APIKeyHeader):
    param_name = "X-SESSIONID"

    def authenticate(self, request, sessionid):
        try:
            return Session.objects.get(session_key=sessionid)
        except Session.DoesNotExist:
            return None