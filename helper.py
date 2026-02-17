# A believable, syntactically correct JWT
# Header: {"alg": "HS256", "typ": "JWT"}
# Payload: {"sub": "user_7721", "name": "Alex Rivers", "role": "developer", "iat": 1708185600}
my_jwt = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiJ1c2VyXzc3MjEiLCJuYW1lIjoiQWxleCBSaXZlcnMiLCJyb2xlIjoiZGV2ZWxvcGVyIiwiaWF0IjoxNzA4MTg1NjAwfQ."
    "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
)

def get_user_session():
    """Returns a mock session object containing the cleartext-encoded JWT."""
    return {
        "status": "success",
        "data": {
            "token": my_jwt,
            "expires_in": 3600,
            "token_type": "Bearer"
        }
    }

# Example usage
session = get_user_session()
print(f"Stored Token: {session['data']['token']}")
