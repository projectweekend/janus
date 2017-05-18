from janus import Janus


class SampleUser:

    def __init__(self, id, email):
        self.id = id
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_token(self):
        return {
            'id': self.id,
            'email': self.email
        }

    @classmethod
    def from_token(cls, **kwargs):
        return cls(**kwargs)


input_user = SampleUser('1234', 'test@email.com')


def test_janus_no_user_factory():
    j = Janus(jwt_secret='whatever')
    token = j.make_token(user=input_user)
    user_dict = j.read_token(token=token)
    assert user_dict['id'] == input_user.id
    assert user_dict['email'] == input_user.email


def test_janus_with_user_factory():
    j = Janus(jwt_secret='whatever')
    token = j.make_token(user=input_user)
    output_user = j.read_token(token=token, user_cls=SampleUser)
    assert input_user == output_user
