from django import template
from django.contrib.auth.models import User
from mdldjango.models import *
from events.models import WorkshopAttendance, TestAttendance

register = template.Library()

def get_participant_score(key):
    try:
        ta = MdlUser.objects.get(mdluser_id = key)
    except:
        return 'error'
    
    return key

def check_workshop_enrole(rid, mdluser_id):
    try:
        wa = WorkshopAttendance.objects.get(workshop_id = rid, mdluser_id = mdluser_id)
        return True
    except:
        return False

def check_test_enrole(rid, mdluser_id):
    try:
        wa = TestAttendance.objects.get(test_id = rid, mdluser_id = mdluser_id)
        return True
    except:
        return False

register.filter('get_participant_score', get_participant_score)
register.filter('check_workshop_enrole', check_workshop_enrole)
register.filter('check_test_enrole', check_test_enrole)