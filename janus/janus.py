import jwt


class Janus:

    def __init__(self, jwt_secret, jwt_algorithm=None, user_class=None):
        self.jwt_secret = jwt_secret
        self.jwt_algorithm = 'HS256' if jwt_algorithm is None else jwt_algorithm
        self.user_class = user_class

    def make_token(self, user):
        return jwt.encode(user.token_data, self.jwt_secret).decode()

    def read_token(self, token):
        token_data = jwt.decode(token, self.jwt_secret)
        if self.user_class is None:
            return token_data
        return self.user_class.from_token_data(token_data)
