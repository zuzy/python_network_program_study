#!/usr/bin/python3
# -*- coding: utf-8 -*-

import upnp

device = upnp.Device({
  'deviceType': 'urn:sadmin-fr:device:demo:1',
  'friendlyName': 'UPnP Test',
  'uuid': '00a56575-78fa-40fe-b107-8f4b5043a2b0',
  'manufacturer': 'BONNET',
  'manufacturerURL': 'http://sadmin.fr'
})

service = upnp.Service({
  'serviceType': 'sadmin-fr:service:dummy',
  'serviceId': 'sadmin-fr:serviceId:1',
})

device.addService(service)

server = upnp.Annoncer(device)
server.initLoop()
server.notify()
server.foreaver()
server.dispose()