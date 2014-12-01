## Script (Python) "getSlotsForDay"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=day
##title=
##
if not day:
    raise ValueError, "No day was specified"
signupSheetBrains = context.queryCatalog({'portal_type':'NursingSignupSheet', 'Title':day})
if len(signupSheetBrains) == 0:
  raise ValueError, "No signup sheets were found"
if len(signupSheetBrains) > 1:
  raise ValueError, "Too many signup sheets (%s) were found for day %s" % (len(signupSheetBrains), day)
allSlots = []
for signupSheetBrain in signupSheetBrains:
    signupSheet = signupSheetBrain.getObject()
    title = signupSheet.Title()
    schema = signupSheet.Schema().viewableFields(signupSheet)
    for field in schema:
      name = field.getName()
      if name.find("timeslot") <> -1:
        #allSlots.append("%s: %s" % (title, name))
        allSlots.append( {'day':day, 'slot':name} )
return allSlots
