## Script (Python) "getSlotLabel"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=day,slot
##title=
##
signupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet', 'Title':day})
if len(signupSheetBrains) == 0:
  raise ValueError, 'No such signup sheet found for day %s' % day
if len(signupSheetBrains) > 1:
  raise ValueError, 'Too many signup sheets found (%s) for day %s' % (len(signupSheetBrains), day)
signupSheetBrain = signupSheetBrains[0]
signupSheet = signupSheetBrain.getObject()
slotLabel = signupSheet.getField(slot).widget.label
return {'full' : day + ' @ ' + slotLabel, 'day':day, 'slot':slotLabel }
