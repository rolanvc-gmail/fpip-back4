__author__ = 'rolanvc'
##
# Permission revisions.
##
USER_ROLE_HAS_ADD = 0
USER_ROLE_HAS_EDIT = 1
USER_ROLE_HAS_DEL = 2


def getAccessRequestMenu(user):

    role = user.user_role
    if role.name == 'Security':
        return None
    menu =  {
        "text":"Access Request(7-Day)",
        "subs":[]
    }
    menu["subs"].append({"text":"Single Application", "state":'main.access_request' })

    menu["subs"].append({"text":"Batch Application", "state":'main.batch_access_request'})

    # if user.access_construction:
    #     menu["subs"].append({"text":"Construction", "state":'main.construction', "disabled":False})
    #
    # if user.access_service_provider:
    #     menu["subs"].append({"text":"Service Provider", "state":'main.service_provider', "disabled":False})
    #
    # if user.access_repair_maintenance:
    #     menu["subs"].append({"text":"Repair and Maintenance", "state":'main.repair_maintenance', "disabled":False})



    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getParkPassIdMenu(user):
    role = user.user_role
    if role.name == 'Security':
        return None
    menu = {
        "text": "Park Pass ID",
        "subs": []
    }


    menu["subs"].append({"text": "Single Application", "state": 'main.parkpassid'})
    menu["subs"].append({"text": "Batch Application", "state": 'main.batchparkpassid'})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getVehicleStickerMenu(user):
    role = user.user_role
    if role.name == 'Security':
        return None

    menu =  {
        "text":"Vehicle Sticker",
        "subs":[]
    }

    menu["subs"].append({"text":"Single Application ",  "state":'main.single-sticker', "disabled":False})
    menu["subs"].append({"text":"Batch Application",  "state":'main.batch-sticker', "disabled":False})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getCentralAuthorizerMenu(user):
    role = user.user_role
    if role.name == 'Security':
        return None

    menu = {
        "text":"Authorizer",
        "subs":[]
    }
    role = user.user_role

    if role.manage_user:
        menu["subs"].append({"text":"Park Access Endorser", "state":'main.users'})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getAdminMenu(user):
    menu = {
        "text":"Admin",
        "subs":[]
    }
    role = user.user_role

    if role.request_locator:
        menu["subs"].append({"text":"Locators", "state":'main.locator'})

    if role.request_project:
        menu["subs"].append({"text":"SubContractors", "state":'main.subcon'})
        menu["subs"].append({"text":"GenContranctors", "state":'main.gencon'})
        menu["subs"].append({"text":"Projects", "state":'main.project'})


    if role.request_banned_employee:
        menu["subs"].append({"text":"Banned Employees", "state":'main.bannedEmployees'})

    if role.request_flagged_purpose:
        menu["subs"].append({"text":"Flagged Purposes", "state":'main.flaggedPurposes'})


    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getSuperAdminMenu(user):
    menu = {
        "text":"For Approval",
        "subs":[]
    }
    role = user.user_role

    if role.approve_locator:
        menu["subs"].append({"text":"Locators", "state":'main.locator-sa'})

    if role.approve_project:
        menu["subs"].append({"text":"Projects", "state":'main.project-sa'})

    if role.approve_vehicle_type:
        menu["subs"].append({"text":"Vehicle Types", "state":'main.vehicle_type-sa'})

    if role.approve_vehicle_usage:
        menu["subs"].append({"text":"Vehicle Usages", "state":'main.vehicle_usage-sa'})

    if role.approve_id_fee:
        menu["subs"].append({"text":"ID Fees", "state":'main.id_fee-sa'})

    if role.approve_locator_sticker_fee:
        menu["subs"].append({"text":"Locator Sticker Fees", "state":'main.locator_sticker_fee-sa'})

    if role.approve_csprm_sticker_fee:
        menu["subs"].append({"text":"Const/SP/RM Pass Fees", "state":'main.csprm_pass_fee-sa'})

    if role.approve_type_of_work:
        menu["subs"].append({"text":"Types of Work", "state":'main.types_of_work'})

    if role.approve_plate_no_format:
        menu["subs"].append({"text":"Plate Number Formats", "state":'main.plate_no_formats-sa'})

    if role.approve_banned_employee:
        menu["subs"].append({"text":"Banned Employees", "state":'main.bannedEmployees-sa'})

    if role.approve_flagged_purpose:
        menu["subs"].append({"text":"Flagged Purpose ", "state":'main.flaggedPurpose-sa'})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu


def getReportMenu(user):
    menu = {
        "text":"Reports",
        "subs":[]
    }
    role = user.user_role
    canViewReports = role.view_reports

    if canViewReports:
        menu["subs"].append({"text":"Guest Access Report", "state":'main.rep_gv'})
        menu["subs"].append({"text":"Applicant Access Report", "state":'main.rep_app'})
        menu["subs"].append({"text":"Temporary Pass Access Report", "state":'main.rep_temp_pass'})
        menu["subs"].append({"separator":True})
        menu["subs"].append({"text":"Park Pass ID", "state":'main.rep_ppid'})
        menu["subs"].append({"separator":True})
        menu["subs"].append({"text":"Locator Sticker", "state":'main.rep_s_locator'})
        menu["subs"].append({"text":"Contractor Sticker", "state":'main.rep_s_contractor'})
        menu["subs"].append({"text":"Service Provider Sticker", "state":'main.rep_s_service_service'})
        menu["subs"].append({"text":"Environmental Service Provider Sticker", "state":'main.rep_s_service_esp'})
        menu["subs"].append({"text":"Shuttle Service Provider Sticker", "state":'main.rep_s_service_shuttle'})
        menu["subs"].append({"text":"Vendor Sticker", "state":'main.rep_s_vendor'})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu



def getTestsMenu(user):
    menu = {
        "text":"Tests",
        "subs":[]
    }

    role = user.user_role

    if role.approve_locator:
        menu["subs"].append({"text":"Guest Visitor", "state":'main.testGuestVisitor',"disabled":True,})
        menu["subs"].append({"text":"Applicant", "state":'main.testApplicant', "disabled":True})
        menu["subs"].append({"text":"Construction/SP/R&M", "state":'main.testCSPRM',"disable":True})
        menu["subs"].append({"text":"Sticker/Passes - Locator", "state":'main.testSPLocator',"disabled":True})
        menu["subs"].append({"text":"Sticker/Passes - CSPRM", "state":'main.testSPCSPRM',"disabled":True})

    if len(menu["subs"]) == 0:
        return None
    else:
        return menu

    return menu



