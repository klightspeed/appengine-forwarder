#!/usr/bin/env python

import webapp2

from google.appengine.ext import ndb

class DomainRedirection(ndb.Model):
  domainname = ndb.StringProperty(required=True)
  redirect = ndb.StringProperty(required=True)
  keeppath = ndb.BooleanProperty(required=True)

class Redirector(webapp2.RequestHandler):
  def get(self):
    domain = self.request.host
    urlpath = self.request.path
    domainredirect = DomainRedirection.query(DomainRedirection.domainname = domain).get()

    if domainredirect is not None:
      if domainredirect.keeppath:
        self.redirect(domainredirect.redirect + urlpath)
      else:
        self.redirect(domainredirect.redirect)
    else:
      self.abort(404)

app = webapp2.WSGIApplication([
    (r'/.*', Redirector)
  ])
