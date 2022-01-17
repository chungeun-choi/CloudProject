def parternList():
    #line(input_d)를 데이터를 파싱하기위한 정규표현식 패턴 파트
    _samePart = r'access-list\s(?P<ply>\w+)\sline\s(?P<lineNum>\d+)\sextended\s(?P<exInfo>\w+)\s'
    _objectPart = r'object-group\s(?P<pobj>\w+\-\w+)\s',r'object-group\s(?P<sobj>\w+\-\w+)\s',r'object-group\s(?P<dobj>\w+\-\w+)\s'
    _hostPart = r'host\s(?P<sobj>\d+\.+\d+\.+\d+\.+\d+)\s',r'host\s(?P<dobj>\d+\.+\d+\.+\d+\.+\d+)\s'
    _hitPart = r'\(?hitcnt=(?P<hit>\d+)\)\s'
    _aclId = r'(?P<aclId>\w+)' #other 사용시 꼭 뒤에 '\s' 
    _portType = r'eq\s(?P<pobj>\w+)\s'
    _portInfo = r'(?P<portInfo>\w+)'
    _loggingPart = r'log\sinformational\sinterval\s(?P<interval>\w+)\s'
    _timeRangePart = r'time-range\s(?P<tobj>\w+\-\w+)\s'
    _statePart = r'\(inactive\)\s'
    _anyPart = r'(?P<sobj>\w+)\s',r'(?P<dobj>\w+)\s'
    _echoPart = r'(?P<echo>\w+)',r'(?P<echoreply>\w+\-+\w+)'
    _icmp = r'(?P<pobj>\w+)'


    #현재 장비에서 출력해주는 형태를 패턴 파트를 조합하여 구성
    partern1 = _samePart+_portInfo+'\s'+_objectPart[1]+_hostPart[1]+_portType+_hitPart+_aclId
    partern2 = _samePart+_portInfo+'\s'+_hostPart[0]+_hostPart[1]+_portType+_hitPart+_aclId
    partern3 = _samePart+_objectPart[0]+_hostPart[0]+_objectPart[2]+_hitPart+_aclId
    partern4 = _samePart+_objectPart[0]+_objectPart[1]+_objectPart[2]+_hitPart+_aclId
    partern5 = _samePart+_objectPart[0]+_objectPart[1]+_hostPart[1]+_hitPart+_aclId
    partern6 = _samePart+_portInfo+'\s'+_hostPart[0]+_hostPart[1]+_portType+_loggingPart+_hitPart+_aclId
    partern7 = _samePart+_icmp+'\s'+_anyPart[0]+_anyPart[1]+_echoPart[0]+'\s'+_hitPart+_aclId
    partern8 = _samePart+_icmp+'\s'+_anyPart[0]+_anyPart[1]+_echoPart[1]+'\s'+_hitPart+_aclId
    partern9 = _samePart+_portInfo+'\s'+_anyPart[0]+_hostPart[1]+_portType+_loggingPart+_hitPart+_aclId
    partern10 = _samePart+_objectPart[0]+_anyPart[0]+_hostPart[1]+_hitPart+_aclId
    partern11 = _samePart+_objectPart[0]+_objectPart[1]+_objectPart[2]+_loggingPart+_timeRangePart+_hitPart+_aclId
    partern12 = _samePart+_objectPart[0]+_objectPart[1]+_objectPart[2]+_loggingPart+_timeRangePart+_hitPart+_statePart+_aclId
    partern13 = _samePart+_objectPart[0]+_hostPart[0]+_objectPart[2]+_timeRangePart+_hitPart+_statePart+_aclId
    partern14 = _samePart+_objectPart[0]+_hostPart[0]+_hostPart[1]+_timeRangePart+_hitPart+_statePart+_aclId

            
        #패턴 리스트
    partern = [partern1,partern2,partern3,partern4,partern5,partern6,partern7,partern8,partern9,partern10,partern11,partern12,partern13,partern14]

    return partern

def serviceToPort(serviceName):
    return {
        'aol':'5190',
        'bgp':'179',
        'biff':'512',
        'bootpc':'68',
        'bootps':'67',
        'chargen':'19',
        'cifs':'3020',
        'citrix-ica':'1494',
        'cmd':'514',
        'ctiqbe':'2748',
        'daytime':'13',
        'discard':'9',
        'dnsix':'195',
        'domain':'53',
        'echo':'7',
        'exec':'512',
        'finger':'79',
        'ftp':'21',
        'ftp-data':'20',
        'gopher':'70',
        'h323':'1720',
        'hostname':'101',
        'http':'80',
        'https':'443',
        'ident':'113',
        'imap4':'143',
        'irc':'194',
        'isakmp':'500',
        'kerberos':'750',
        'klogin':'543',
        'kshell':'544',
        'ldap':'389',
        'ldaps':'636',
        'login':'513',
        'lotusnotes':'1352',
        'lpd':'515',
        'mobile-ip':'434',
        'nameserver':'42',
        'netbios-dgm':'138',
        'netbios-ns':'137',
        'netbios-ssn':'139',
        'nfs':'2049',
        'nntp':'119',
        'ntp':'123',
        'pcanywhere-data':'5631',
        'pcanywhere-status':'5632',
        'pim-auto-rp':'496',
        'pop2':'109',
        'pop3':'110',
        'pptp':'1723',
        'radius':'1645',
        'radius-acct':'1646',
        'rip':'520',
        'rsh':'514',
        'rtsp':'554',
        'secureid-udp':'5510',
        'sip':'5060',
        'smtp':'25',
        'snmp':'161',
        'snmptrap':'162',
        'sqlnet':'1521',
        'ssh':'22',
        'sunrpc':'111',
        'syslog':'514',
        'tacacs':'49',
        'talk':'517',
        'telnet':'23',
        'tftp':'69',
        'time':'37',
        'uucp':'540',
        'vxlan':'4789',
        'who':'513',
        'whois':'43',
        'www':'80',
        'xdmcp':'177'
    }[serviceName]
