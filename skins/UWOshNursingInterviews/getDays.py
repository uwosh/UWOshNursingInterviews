## Script (Python) "getDays"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
signupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet'})
if len(signupSheetBrains) == 0:
  raise ValueError, "No signup sheets were found"
days = []
for signupSheetBrain in signupSheetBrains:
    signupSheet = signupSheetBrain.getObject()
    title = signupSheet.Title()
    days.append( title )
return days
