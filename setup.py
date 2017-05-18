from setuptools import setup


setup(
    name='janus',
    version='0.0.1',
    author='Brian Hines',
    author_email='brian@projectweekend.net',
    description='A JWT auth companion',
    url='https://github.com/projectweekend/janus',
    packages=['janus'],
    py_modules=['janus'],
    install_requires=[
        'PyJWT==1.5.0',
    ],
)
