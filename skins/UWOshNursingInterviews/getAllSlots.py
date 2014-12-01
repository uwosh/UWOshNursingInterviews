## Script (Python) "getAllSlots"
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
  return "No signup sheets were found"
allSlots = []
for signupSheetBrain in signupSheetBrains:
    signupSheet = signupSheetBrain.getObject()
    title = signupSheet.Title()
    schema = signupSheet.Schema().viewableFields(signupSheet)
    for field in schema:
      name = field.getName()
      if name.find("timeslot") <> -1:
        #allSlots.append("%s: %s" % (title, name))
        allSlots.append( {'day':title, 'slot':name} )
return allSlots
