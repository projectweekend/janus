This is a simple utility class for making JSON Web Tokens (JWT) for user objects and reading JWTs back into user objects. Compatible user objects must have the following interface:
* A property named `token_data` that returns a dictionary of data to encode into the JWT.
* A class method named `from_token_data` that accepts a single dictionary (the decoded JWT) and returns a user object instance.

Here's a class that implements the required interface:
```python
class User:

    def __init__(self, id, email):
        self.id = id
        self.email = email

    @property
    def token_data(self):
        return self.__dict__

    @classmethod
    def from_token_data(cls, token_data):
        # Do whatever you want to create the user here. In this example we
        # assume token_data contains all the key word arguments for the
        # class constructor.
        return cls(**token_data)
```

## Usage
```python
from janus import Janus
from whatever import User


j = Janus(jwt_secret='supersecret', user_class=User)

# Get a user instance for a JWT
user = j.read_token(token='some jwt string')

# Make a JWT for a user
jwt = j.make_token(user=user)
```



## Run tests with HTML coverage report
```bash
docker-compose run janus pytest --cov=janus --cov-report=html
```
