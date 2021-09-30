import string
import random


def get_default_share_code(size=8, chars=string.ascii_uppercase + string.digits):
    '''
    Returns the share code.
    '''
    return ''.join(random.choice(chars) for _ in range(size))
