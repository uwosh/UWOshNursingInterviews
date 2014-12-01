## Script (Python) "hasManagePortalPermission"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
return context.portal_membership.checkPermission('Manage portal', context)
