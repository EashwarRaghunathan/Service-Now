#!/usr/bin/python

from SOAPpy import SOAPProxy
import sys

def createincident(params_dict):

        # instance to send to
        instance='autodesksb'

        # username/password
        username='ZENOSS'
        password='ZENOSS'


        # proxy - NOTE: ALWAYS use https://INSTANCE.service-now.com, not https://www.service-now.com/INSTANCE for web services URL from now on!
#        proxy = 'https://%s:%s@%s.service-now.com/u_nimsoft.do?WSDL' % (username, password, instance)
        proxy = 'https://%s:%s@%s.service-now.com/incident.do?SOAP' % (username, password, instance)
        namespace = 'http://www.service-now.com/'
        server = SOAPProxy(proxy, namespace)

        # uncomment these for LOTS of debugging output
        #server.config.dumpHeadersIn = 1
        #server.config.dumpHeadersOut = 1
        #server.config.dumpSOAPOut = 1
        #server.config.dumpSOAPIn = 1

        response = server.insert(
                impact=int(params_dict['impact']),
                urgency=int(params_dict['urgency']),
#               caller_id=params_dict['caller_id'],
                category=str(params_dict['category']),
                assignment_group=params_dict['assignment_group'],
                short_description=params_dict['short_description'],
                comments=params_dict['comments'])

        return response


#values = {'impact': sys.argv[2], 'urgency': sys.argv[3], 'priority': sys.argv[2], 'category':str(sys.argv[1]), 'location': 'San Diego', 'user': '3266f43c7d592100f0c72bd877f14ea5', 'assignment_group': '458ea5b10a0a3c5501ba628c54458a48', 'assigned_to': '3ae8efa20a0a3c550126fb97d59918d8', 'short_description': sys.argv[5], 'comments': str(sys.argv[6])}

values = {'impact': sys.argv[2], 'urgency': sys.argv[3], 'priority': sys.argv[2], 'category':str(sys.argv[1]), 'location': 'San Diego', 'caller_id': '3266f43c7d592100f0c72bd877f14ea5', 'assignment_group': '458ea5b10a0a3c5501ba628c54458a48', 'assigned_to': '3ae8efa20a0a3c550126fb97d59918d8', 'short_description': sys.argv[5], 'comments': str(sys.argv[6])}

new_incident_sysid=createincident(values)

print "Returned sysid: "+repr(new_incident_sysid)
