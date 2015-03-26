"""
API functions relating to admin users.
"""

import api

from api.common import check, validate, safe_fail
from api.common import WebException, InternalException
from api.annotations import log_action

def give_admin_role(name=None, uid=None):
    db = api.common.get_conn()

    user = api.user.get_user(name=name, uid=uid)
    db.users.update({"uid": user["uid"]}, {"$set": {"admin": True}})