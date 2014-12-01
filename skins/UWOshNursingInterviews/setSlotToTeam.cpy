## Controller Python Script "setSlotToTeam"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.PythonScripts.standard import html_quote
#from Products.CMFPlone.utils import getToolByName

request = context.REQUEST
RESPONSE =  request.RESPONSE

#print "request is", request
#print "response is", RESPONSE

memberNameNotFound = '__no_member_to_assign__'
memberName = request.get('memberToAssign', memberNameNotFound)
#print "memberToAssign is", memberName
if memberName <> memberNameNotFound:
    state.setError ('memberToAssign', 'You do not have a member name to assign to a time slot.')

slotNotFound = '__no_slot_to_assign__'
desiredSlot = request.get('slotSelection', slotNotFound)
#print "desiredSlot is", desiredSlot
if desiredSlot <> slotNotFound:
    state.setError ('memberToAssign', 'You did not select a time slot.')

day, slot = desiredSlot.split(' @ ')

#pm = getToolByName(context, 'portal_membership')
pm = context.portal_membership
memberObj = pm.getAuthenticatedMember()
email = memberObj.getProperty('email', '')
fullname = memberObj.getProperty('fullname', '')
#raise ValueError, 'email of %s is %s' % (memberName, email)

signupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet', 'Title':day})
if len(signupSheetBrains) == 0:
  raise ValueError, 'No such signup sheet found for day %s' % day
if len(signupSheetBrains) > 1:
  raise ValueError, 'Too many signup sheets found (%s) for day %s' % (len(signupSheetBrains), day)
signupSheetBrain = signupSheetBrains[0]
signupSheet = signupSheetBrain.getObject()

noSuchSlot = '__no_such_slot__'
if getattr(signupSheet, slot, noSuchSlot) == noSuchSlot:
    state.setError ('desiredSlot', "There is no time slot named '%s' on %s." % (slot, day))

portal_status_message = ''

# clear out any previously chosen time slot for this user
allSignupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet'})
#raise ValueError, "allSignupSheetBrains = %s" % allSignupSheetBrains
for brain in allSignupSheetBrains:
  sheet = brain.getObject()
  schema = sheet.Schema().viewableFields(sheet)
  for field in schema:
    name = field.getName()
    if name.find("timeslot") <> -1:
      value = getattr(sheet, name).strip()
      if value.find(';;;') == -1:
        valueMemberName = value
        valueEmail = ''
        valueFullName = ''
      else:
        valueMemberName, valueEmail, valueFullName = value.split(';;;')
      #out.append("attribute '%s' of sheet '%s' value is '%s'" % (name, sheet.Title(), value))
      if memberName == valueMemberName:
        mutator = field.getMutator(sheet)
        mutator('')
        portal_status_message = portal_status_message + "Cleared your previously chosen time slot: %s at %s.  " % (sheet.Title(), field.widget.label)
        #out.append ("Found!")
        #return "\n".join(out)

# now set the newly chosen time slot
for field in signupSheet.Schema().viewableFields (signupSheet):
    fieldName = field.getName()
    fieldLabel = field.widget.label
    if fieldLabel == slot:
        mutator = field.getMutator(signupSheet)
        desiredSlotLabel = field.widget.label
        value = getattr(sheet, name).strip()
        if value <> '':
            raise ValueError, "The slot you chose is not empty!  Use your browser's back button, reload the page to get the slots currently available, and choose another slot."
        else:
            mutator ("%s;;;%s;;;%s" % (memberName, email, fullname))

# send confirmation email
message = """
You have made a Nursing health requirements appointment for

%s

%s
""" % (desiredSlot, context.portal_url())

mTo = email
#mFrom = context.email_from_address
mFrom = 'robl@uwosh.edu'
mSubj = 'Your Nursing health requirements appointment'
context.MailHost.send(message, mTo, mFrom, mSubj)

# output status message and redirect browser
portal_status_message = portal_status_message + "Assigned user '%s' to slot '%s' on %s ok.  An email confirmation message has been sent to you.  You may log out of this site or exit from your browser now." % (memberName, desiredSlotLabel, day)
state.setKwargs ({'portal_status_message':portal_status_message})
redirect_to = context.portal_url.getPortalObject().absolute_url()
state.setNextAction ('redirect_to:string:' + redirect_to)

#return printed



# (Optional) set the default next action (this can be overridden
# in the script's actions tab in the ZMI).
#state.setNextAction('redirect_to:string:http://www.plone.org')

# Always make sure to return the ControllerState object
return state
