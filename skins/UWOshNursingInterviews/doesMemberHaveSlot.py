## Script (Python) "doesMemberHaveSlot"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
#from Products.CMFPlone.utils import getToolByName

#pm = getToolByName(context, 'portal_membership')
pm = context.portal_membership
if pm.isAnonymousUser():
  raise ValueError, 'You are not logged in; no current member defined'
u = str(pm.getAuthenticatedMember()).strip()
if not u:
  raise ValueError, "No currently defined authenticated member"
#raise ValueError, "Current member is %s" % u
signupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet'})
if len(signupSheetBrains) == 0:
  raise ValueError, 'No signup sheets found'
out = []
for signupSheetBrain in signupSheetBrains:
  signupSheet = signupSheetBrain.getObject()
  day = signupSheet.Title()
  schema = signupSheet.Schema().viewableFields(signupSheet)
  for field in schema:
    name = field.getName()
    if name.find("timeslot") <> -1:
      value = getattr(signupSheet, name).strip()
      if value.find(';;;') == -1:
        valueMemberName = value
        valueEmail = ''
        valueFullName = ''
      else:
        valueMemberName, valueEmail, valueFullName = value.split(';;;')
      #out.append("attribute '%s' of sheet '%s' value is '%s'" % (name, signupSheet.Title(), value))
      if u == valueMemberName:
        #out.append ("Found!")
        #return "\n".join(out)
        return context.getSlotLabel(day, name)
#out.append("Nothing found")
#return "\n".join(out)
return False
