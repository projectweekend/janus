from janus import Janus


class SampleUser:

    def __init__(self, id, email):
        self.id = id
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def token_data(self):
        return {
            'id': self.id,
            'email': self.email
        }

    @classmethod
    def from_token_data(cls, token_data):
        return cls(**token_data)


sample_user = SampleUser('1234', 'test@email.com')


def test_janus_no_user_factory():
    j = Janus(jwt_secret='whatever')
    token = j.make_token(user=sample_user)
    user_dict = j.read_token(token=token)
    assert user_dict['id'] == sample_user.id
    assert user_dict['email'] == sample_user.email


def test_janus_with_user_factory():
    j = Janus(jwt_secret='whatever', user_class=SampleUser)
    token = j.make_token(user=sample_user)
    output_user = j.read_token(token=token)
    assert sample_user == output_user
