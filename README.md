An anagrammatic, turn-key CouchDB eventual replacement for the base free dynamic
dns use case.

[More info about CouchApps here.](http://couchapp.org) [including installation]

## Deploying this app

Make some databases:

    curl -X PUT http://name:password@localhost:5984/candyminds
    curl -X PUT http://name:password@localhost:5984/candyminds/current_ip_address -d @initial.json
    
    curl -X PUT https://name:password@youraccount.iriscouch.com/candyminds
    curl -X PUT https://name:password@youraccount.iriscouch.com/candyminds/current_ip_address -d @initial.json
    
Put some application logic in the local one:

    couchapp push . http://name:password@localhost:5984/candyminds

Edit the `poller.py` `CAPITALIZED_VARIABLES`, or do something equivalent to it in
some other language. You can run a process like `poller.py` from within
couchdb by adding the following lines to your `local.ini`:

`[os_daemons]`

`candyminds_poller = /usr/bin/python /opt/poller.py`

[This works great in Debian and not really in OS X, will run in foreground on
either.]

Once you see that your local database has been updated, set up continuous
replication (in futon -> replicator -> local candyminds to iriscouch
candyminds).

Then visit your new easy-to-remember-url at

`http://youraccount.iriscouch.com/candyminds/_design/cm/_show/current/current_ip_address`

You can create an easier-to-remember url by using `vhosts` and one of iriscouch's
handy alternate urls, ie in `youraccount.iriscouch.com/_utils` in configuration,
create a record like this:

`vhosts  youraccount.iriscou.ch/casa  /candyminds/_design/cm/_show/current/current_ip_address`

and access your server at `youraccount.iriscou.ch/casa`
