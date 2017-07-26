import re
import datetime
import sys
import itertools as it
f=open("Main.txt","a")
#line="Oct  3 15:30:18 mail1 postfix/lmtp[5369]: DB10242054: to=<XXXXX>, orig_to=<XXXXXX>, relay=ip[ip]:port, delay=1.4, delays=0.04/0/0.01/1.4, dsn=2.0.0, status=sent (250 2.0.0 from MTA(smtp:[iP]:port): 250 2.0.0 Ok: queued as 4580B4208C)Oct  3 15:30:18 mail1 postfix/smtp[5175]: 4580B4208C: to=<XXXXX>, relay=XXXXX[IP]:port, delay=0.52, delays=0.02/0.01/0.27/0.22, dsn=2.0.0, status=sent (250 2.0.0 OK 1412343018 rr9si6866736lbb - gsmtp)Oct  3 15:33:57 mail1 amavis[5542]: (05542-09) Passed CLEAN {RelayedInbound}, [ip]:port [ip] <XXXX> -> <XXX>, Message-ID: <XXX>, mail_id: XXXXX, Hits: -1.899, size: 6483, queued_as: 806A24207B, 1483 msOct  3 15:33:57 mail1 postfix/lmtp[6694]: F1FDD41F9D: to=<XXXXXX>, orig_to=<BBBBBB>, relay=ip[ip]:port, delay=1.7, delays=0.18/0/0.01/1.5, dsn=2.0.0, status=sent (250 2.0.0 from MTA(smtp:[127.0.0.1]:10025): 250 2.0.0 Ok: queued a 806A24207B"
line = "Jan  5 09:02:48 localhost postfix/cleanup[5978]: 1733D16A90A: message-id=&lt;20170105140248.1733D16A90A@mail.testserver.com&gt;Jan  5 09:02:48 localhost postfix/qmgr[2596]: 1733D16A90A: from=&lt;root@mail.testserver.com&gt;, size=460, nrcpt=1 (queue active)Jan  5 09:02:51 localhost postfix/smtp[5980]: 1733D16A90A: to=&lt;divij.sehgaal7@gmail.com&gt;, relay=gmail-smtp-in.l.google.com[74.125.130.27]:25, delay=3.4, delays=0.05/0.01/1.9/1.5, dsn=2.0.0, status=sent (250 2.0.0 OK 1483624971 s11si76004239pgc.259 - gsmtp)"
#match = re.search(r'[\w\.-]+@[\w\.-]+', line)
#print match.group(0)
# line = "why people don't know what regex are? let me know 321dsasdsa@dasdsa.com.lol   dssdadsa dadaads@dsdds.com"
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
#print match
#['321dsasdsa@dasdsa.com.lol', 'dadaads@dsdds.com']
m = re.findall(r"\[([0-9_]+)\]", line)
#print m
z=dict(zip(m, match))
#print z
#date = datetime.datetime.strptime(line, "\[jan-dec]\  %d %H:%M:%S.%f")
dat=re.findall('[A-Za-z]{3}\s+\d{1,2}\s(?:\d{1,2}:){2}\d{1,2}',line)
#print dat
#a=dict(zip(z, dat))
#print a
l=list(it.chain.from_iterable(it.izip(dat,m,match)))
#print l
for i in range(0,len(dat)):
     print "\n","Date:"+dat[i],"","","ID: "+m[i],"","MAIL:"+match[i]
