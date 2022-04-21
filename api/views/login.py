from django.views.decorators.csrf import csrf_exempt
from api.models import User
from api.utils import errors
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
import json
from api.utils.notifications import user_locked_email, user_locked_notify, unlock_user_notify
from api.utils import permissions
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

def getMenuObject(user):
    '''
    Returns a json object describing the menu.
    Inputs: permission, a BitArray object
    '''

    data = []
    p = permissions.getAccessRequestMenu(user)
    if p : data.append(p)
    p = permissions.getParkPassIdMenu(user)
    if p : data.append(p)
    p = permissions.getVehicleStickerMenu(user)
    if p : data.append(p)
    p = permissions.getCentralAuthorizerMenu(user)
    if p : data.append(p)
    p = permissions.getAdminMenu(user)
    if p : data.append(p)
    p = permissions.getSuperAdminMenu(user)
    if p : data.append(p)
    p = permissions.getReportMenu(user)
    if p : data.append(p)
    # p = permissions.getTestsMenu(user)
    # if p : data.append(p)
    return data

@csrf_exempt
def vwLogin(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = str(data.get('email'))
            password = data.get('password')
            (error, result) = login(email, password)

            response = {'status':error}
            if error == errors.SUCCESS:
                user = result
                response['uuid'] = str(user.uuid)
                response['menu'] = getMenuObject(user)
                response['locatorId'] = user.locator_id
                response['locatorName'] = user.locator.name
                response['userRole'] = user.user_role.name
                response['isActive'] = user.is_active
                response['access_guest'] = user.access_guest
                response['access_applicant'] = user.access_applicant
                response['access_temp'] = user.access_temp
                response['pass_construction'] = user.pass_construction
                response['pass_service'] = user.pass_service
                response['pass_repair'] = user.pass_repair
                response['sticker_locator'] = user.sticker_locator
                response['sticker_contractor'] = user.sticker_contractor
                response['sticker_service'] = user.sticker_service
                response['sticker_vendor'] = user.sticker_vendor
            else:
                response['result'] = result

            return HttpResponse(json.dumps(response), status=200)

        except Exception as e:
            print("Exception: " + str(e))
            return HttpResponseBadRequest(str(e))

    else:
        return HttpResponseNotAllowed()


def login(email, password):
    """

    :param email:
    :param password:
    :return:
    """
    try:
        user = User.objects.get(email=email)
        # if more than 3 wrong attempts, consider locked. We don't care even if password is correct
        if user.times_wrong_passwd >= 3:
            return errors.getError(errors.ERR_USER_LOCKED)
        ok = pwd_context.verify(password, user.password)

        if ok:
            user.last_login = datetime.now()
            user.times_wrong_passwd = 0 # no matter how many times he's tried before, we reset
            if user.is_active:
                # We have a email-password match.  Return the user.
                return errors.SUCCESS, user
            else:
                return errors.getError(errors.ERR_USER_NOT_ACTIVE)

        else:
            # Password is wrong.
            user.times_wrong_passwd += 1
            user.save()
            if user.times_wrong_passwd >= 3:
                #Do actions for locking account
                uname = user.first_name +' '+ user.last_name
                user_locked_email(username=uname, user_email=user.email)
                creator = User.objects.get(id = user.created_by_id )
                creator_name = creator.first_name + ' ' + creator.last_name
                user_locked_notify(creator_name=creator_name, creator_email = creator.email, username= uname, useremail = user.email)
            return errors.getError(errors.ERR_WRONG_PASSWORD)

    except User.DoesNotExist:
        # User does not exist.
        return errors.getError(errors.ERR_NO_USER_FOUND)
    except User.MultipleObjectsReturned:
        return errors.getError(errors.ERR_MULTIPLE_USERS)
