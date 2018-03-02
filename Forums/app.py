########################################
# flask demo
########################################

from flask import Flask
import stores
import dummy_data
from Forums.views import *

member_store = stores.MemberStore()
post_store = stores.PostStore()

if __name__  == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()


