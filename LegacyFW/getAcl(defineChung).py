import re
from unicodedata import name
import json
import os, copy, logging
from directorplus.common._print import _print
from custom_operator.error_code import ErrorCode as E, _e
import patern




def getAcl(policyDict, fpIp, interface, userName, password, contextName, vnType): 
    filter = ''
    if interface == "outbound" and vnType =="VN1":
        filter="show+access-list+%7C+grep+^access-list+VN1_"
    if interface == "outbound" and vnType =="VN2":
        filter="show+access-list+%7C+grep+^access-list+VN2_"
    elif interface == "inbound":
        filter="show+access-list+%7C+grep+^access-list+OUT_"
    elif "XG" in interface:
        filter="show+access-list+%7C+grep+^access-list+XG_"

    url = 'curl -k -s -u '+userName+':'+password+' -A ASDM https://'+fpIp+'/gadmin/exec/changeto+context+'+contextName+'/'+filter
    status, input_d = subprocess.getstatusoutput(url)
    _print(logger, ">>> fwparser.getAcl:url : ", url)
    _print(logger, ">>> fwparser.getAcl:status : ", status)
    _print(logger, ">>> fwparser.getAcl:lines : ", input_d)

    data  = [] 
   

    
    if len(input_d.splitlines())<0 :
        print("조회된 데이터가 존재하지 않습니다") #_print(logger, ">>> fwparser.getAcl:lines : ", lines)
    else : 
        for line in input_d.splitlines() :
            #데이터 형태
            aclDict = {
                'state':None,
                'line':None,
                'ply':None,
                'aclId':None,
                'hitCnt':None,
                'timeRange':None,
                'pobj':None,
                'sobj':None,
                'dobj':None,
                'startTime':None,
                'endTime':None,
                'log':None
                }

            #전달하지 말아야할 내용 필터
            if "elements; name hash" in line : continue 
            #state 정보 입력
            aclDict['state'] = 'inactive' if 'inactive' in line else 'active'
            
            for i in patern.parternList():
                a = re.match(i,line) #match 되는 partern 찾기
                if a != None:
                    #timeRange 여부를 판단하기 -> 해당 사항이 에러코드로서 출력 되기 때문에 try,except로 처리
                    try:
                        timeRange = a.group('tobj')
                    except:
                        timeRange = ""
                    #pobj 변환 및 확인
                    try:
                        pobj = a.group('portInfo')+'/'+patern.serviceToPort(a.group('pobj'))
                    
                    except:
                        pobj = a.group('pobj')
                    
                    
                    #Dic에 추가하기 
                    aclDict['line'] = a.group('lineNum')
                    aclDict['hitCnt'] = a.group('hit')
                    aclDict['ply'] = a.group('ply').replace('_access_in','')
                    aclDict['aclId'] = a.group('aclId')
                    aclDict['pobj'] = a.group('pobj')
                    aclDict['sobj'] = a.group('sobj')
                    aclDict['dobj'] = a.group('dobj')
                    aclDict['log'] ="up" if 'log' in line else 'down'
                    aclDict['timeRange'] = timeRange
                    aclDict['startTime'] = policyDict[aclDict['timeRange']][0] if timeRange !='' else ''
                    aclDict['endTime'] = policyDict[aclDict['timeRange']][1] if timeRange !='' else ''
                    
                    
            data.append(aclDict)

    return json.dumps(data)

