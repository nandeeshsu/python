from functools import wraps

def get_token_auth_header():
    """Obtains the access token from the Authorization Header
    """

    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization Header is expected"
        }, 401)
    
    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must start with Bearer"
        }, 401)
    
    elif len(parts) == 1:
        raise AuthError({
            "code": "invalid_header",
            "description": "Token not found"
        }, 401)
    
    elif len(parts) > 2:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorizatin header must be Bearer token"
        }, 401)
    
    token = parts[1]
    return token

def requires_auth(f):
    """Determines if the access token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        rsa_key = {
            "test": "test"
        }
        if rsa_key:
            return f(*args, **kwargs)
        return decorated
    
class AuthError(object):
    def __init__(self, code, description):
        self.description = description
        self.code = code