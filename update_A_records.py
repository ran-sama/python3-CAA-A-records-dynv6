#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, socket, time
from dns import resolver

def get_res(name):
    return socket.gethostbyname('resolver%s.opendns.com' % name)

aresolver = resolver.Resolver()
aresolver.nameservers = [get_res('1'), get_res('2'), get_res('3'), get_res('4')]

def DNS_magic(hostname):
    DNS_reply = aresolver.resolve(hostname, 'A')
    for rdata in DNS_reply:
        return str(rdata)

expected = DNS_magic('myip.opendns.com')

def run_SSH(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    output, error = process.communicate()
    print(output.replace('\n', ''))
    time.sleep(3)

def zone_updater(domain):
    current = DNS_magic(domain)
    if current != expected:
        run_SSH('ssh -i /home/ran/.ssh/dynv6 api@dynv6.com hosts example.dns.navy set ipv4addr ' + expected)

def record_updater(shortname, fullname):
    current = DNS_magic(fullname)
    if current != expected:
        run_SSH('ssh -i /home/ran/.ssh/dynv6 api@dynv6.com hosts example.dns.navy records set %s a addr ' % shortname + expected)

zone_updater('example.dns.navy')
record_updater('sub1', 'sub1.example.dns.navy')
record_updater('sub2', 'sub2.example.dns.navy')
