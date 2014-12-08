Service-Now  send an insident to service now from command line
===========
#USAGE ssh or windows bash

./snowsendinsident.py "$sysparm_action" "$category" "$impact" "$urgency" "$caller_id" "$cmdb_ci" "$short_description"

# example usage

./snowsendinsident.py 'insert' 'software' 1 1 'Abel Tuter' 'Email' 'new incident from eashwar'


