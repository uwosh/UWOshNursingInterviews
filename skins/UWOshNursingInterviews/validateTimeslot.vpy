## Controller Validator "validateTimeslot"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=
##
n = context.REQUEST.get('slotSelection', None)
if not n:
 state.setError('n', 'Please choose a time slot.', new_status='failure')

if state.getErrors():
 state.set(portal_status_message='Please choose a time slot.')
return state
