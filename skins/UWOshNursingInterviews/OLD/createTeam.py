from Products.PythonScripts.standard import url_quote, urlencode

portal=context.portal_url.getPortalObject()
pm=portal.portal_membership
myFolder=pm.getHomeFolder()

if not myFolder:
    kw = {
        'portal_status_message' : "You must be logged in to create a Homecoming team.",
        'came_from' : context.absolute_url() + "/createTeam",
        }
    context.REQUEST.RESPONSE.redirect(portal.absolute_url() + "/login_form?" + urlencode (kw))
else:
    new_id = myFolder.generateUniqueId('HomecomingTeam')
    newTeam = myFolder.invokeFactory('HomecomingTeam', new_id)
    newTeamURL = myFolder.absolute_url() + '/' + newTeam
    redirect_to = newTeamURL + '/edit'
    portal_status_message="A new team has been created.  You must give it a name and fill out the names and email addresses of its members. Please make sure you enter correct email addresses."

    ploneVersion = portal.portal_migration.getInstanceVersionTuple()
    #portal_status_message +=  " (Plone version is %s)" % str(ploneVersion)
    if ploneVersion[0] == 2 and ploneVersion[1] == 1:
      last_referer = newTeamURL + '/object_delete'
    else:    
      last_referer = newTeamURL + '/delete_confirmation'

    kw = {
        'portal_status_message' : portal_status_message, 
        'last_referer':last_referer,
        }
    context.REQUEST.RESPONSE.redirect(redirect_to + "?" + urlencode(kw))
