import jwt


class Janus:

    def __init__(self, jwt_secret, jwt_algorithm=None):
        self.jwt_secret = jwt_secret
        self.jwt_algorithm = 'HS256' if jwt_algorithm is None else jwt_algorithm

    def make_token(self, user):
        return jwt.encode(user.to_token(), self.jwt_secret).decode()

    def read_token(self, token, user_cls=None):
        token_data = jwt.decode(token, self.jwt_secret)
        if user_cls is None:
            return token_data
        return user_cls.from_token(**token_data)
