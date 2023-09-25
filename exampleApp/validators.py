import re


def validate_data(data):
    if len(data.get('company')) < 3:
        raise ValueError('company must have more than 3 characters')

    if len(data.get('title')) < 3:
        raise ValueError('title must have more than 3 characters')

    if len(data.get('location')) < 3:
        raise ValueError('location must have more than 3 characters')


def validate_register(data):
    email_regex = r'^\w+([.-]?\w+)*@(gmail|hotmail|outlook)\.com$'
    phone_regex = r'^(\\+34|0034|34)?[ -]*(6|7)[ -]*([0-9][ -]*){8}$'
    if not re.match(email_regex, data.get('email')):
        raise ValueError('email malformed')

    if len(data.get('name')) < 3:
        raise ValueError('name must have more than 3 characters')

    if len(data.get('last_name')) < 3:
        raise ValueError('lastName must have more than 3 characters')

    if not re.match(phone_regex, data.get('phone')):
        raise ValueError('phone malformed')
