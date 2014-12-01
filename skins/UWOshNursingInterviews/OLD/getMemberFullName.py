## Script (Python) "getMemberFullName"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=username
##title=
##
from Products.CMFPlone.utils import getToolByName
pm = getToolByName(context, 'portal_membership')
#raise ValueError, "member is '%s'" % username
#raise ValueError, pm.getMemberInfo()
raise ValueError, pm.getMemberInfo(username)
raise ValueError, pm.getMemberById(username)
return pm.getMemberById(username)
