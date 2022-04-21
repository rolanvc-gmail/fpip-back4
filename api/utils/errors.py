__author__ = 'rolanvc'

SUCCESS = 0
ERR_NO_USER_FOUND = 1
ERR_USER_NOT_ACTIVE = 2
ERR_WRONG_PASSWORD = 3
ERR_MULTIPLE_USERS = 4
ERR_NOT_AUTHORIZED = 5
ERR_NOT_AJAX = 6
ERR_USER_LOCKED = 7

MESSAGES = (
    'SUCCESS',
    'NO USER FOUND',
    'USER HAS BEEN DELETED',
    'WRONG PASSWORD',
    'MULTIPLE USERS ERROR',
    'NOT AUTHORIZED',
    'NOT AJAX',
    ' USER ACCOUNT HAS BEEN LOCKED. Please Contact your Central Authorizer.'
)

def getError(err):
    return (err, MESSAGES[err])

def getErrorMsg(err):
    return MESSAGES[err]
