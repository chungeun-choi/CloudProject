"""전달해야 하는 정보값 형태
{
    'state': 'active',
    'line': '1', 
    'ply': 'permit', 
    'aclId': '0x6ff34d69',  
    'hitCnt': '0',  
    'timeRange': '',    
    'pobj': 'tcp/80',   
    'sobj': '172.30.48.2',  
    'dobj': '124.243.57.216',   
    'startTime': '', 
    'endTime': '', 
    'log': 'down' 
}

해당 로직은 기존의 IF문과 \s를 통한 인덱싱 작업으로 파싱하던 로직에 대해 확장성을 기준으로 편리성을 제공하기 위해 변경을 하였습니다.
getAcl 함수는 4가지의 큰 형태로 이루어져있습니다.
1.패턴의 기본이 되는 패턴 파트를 나누는 문단
2.나누어진 파트를 조합하여 패턴을 만드는 문단
3.패턴을 비교하기위해 패턴 리스트를 비교하는 로직
4.찾아낸 패턴을 통해 필요한 데이터를 파싱하여 Json형식으로 치환하는 로직

*해당 메소드는 비정형 데이터로 출력되는 데이터를 정형화 시키는데 있어서 편리성을 제공해주기 위함으로 수정에대한 사항은 '1.'항목과 '2.'항목에 대해서만 수정을 필요로 
*1번과 2번항목이 독립적으로 정의되게끔 하기위해 partern.py 파일로 옮겨 참조하게끔 정의 하였습니다.

"""
import re
from unicodedata import name
import json
import os, copy, logging
from ServiceName import serviceToPort
from patern import parternList



def getAcl(policyDict,input_d):
  
    input_d = input_d
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
            
            
            for i in parternList():
                a = re.match(i,line) #match 되는 partern 찾기
                if a != None:
                    #timeRange 여부를 판단하기 -> 해당 사항이 에러코드로서 출력 되기 때문에 try,except로 처리
                    try:
                        timeRange = a.group('tobj')
                    except:
                        timeRange = ""
                    #pobj 변환 및 확인
                    try:
                        pobj = a.group('portInfo')+'/'+serviceToPort(a.group('pobj'))
                    
                    except:
                        pobj = a.group('pobj')
                    
                    #Dic에 추가하기 
                    aclDict['line'] = a.group('lineNum')
                    aclDict['hitCnt'] = a.group('hit')
                    aclDict['ply'] = a.group('ply').replace('_access_in','')
                    aclDict['aclId'] = a.group('aclId')
                    aclDict['pobj'] = pobj
                    aclDict['sobj'] = a.group('sobj')
                    aclDict['dobj'] = a.group('dobj')
                    aclDict['log'] ="up" if 'log' in line else 'down'
                    aclDict['timeRange'] = timeRange
                    aclDict['startTime'] = policyDict[aclDict['timeRange']][0] if timeRange !='' else ''
                    aclDict['endTime'] = policyDict[aclDict['timeRange']][1] if timeRange !='' else ''
                    
                    
            data.append(aclDict)

    return json.dumps(data)



#테스트하기위한 영역
test = {'CST-TIM_200042_100045': ('2022-01-18 00:00', '2022-01-31 23:59'), 'CST-TIM_200042_100048': ('2022-01-18 14:54', '2022-01-27 14:54')}
defalut =  "access-list OUT_access_in line 36 extended permit tcp host 124.243.70.138 host 172.16.28.2 eq https (hitcnt=0) 0xaa6639db\naccess-list VN2_access_in line 115 extended permit object-group CST-PRT_100000_000023 host 172.16.29.11 object-group CST-NET_100000_000058 (hitcnt=0) 0x90327c20\naccess-list VN1_access_in line 1 extended permit object-group CST-PRT_200042_100049 object-group CST-NET_200042_100062 object-group CST-NET_200042_100063 log informational interval 300 time-range CST-TIM_200042_100045 (hitcnt=0) 0x3caabcec\naccess-list OUT_access_in line 1 extended permit object-group CST-PRT_200042_100049 host 2.3.11.2 host 12.3.45.12 time-range CST-TIM_200042_100045 (hitcnt=0) (inactive) 0x2e035b4d"
checkdata = "access-list VN2_access_in line 101 extended permit tcp object-group CST-NET_200043_000037 host 210.93.149.28 eq smtp (hitcnt=0) 0x2caab8a2 \naccess-list VN2_access_in line 101 extended permit tcp host 172.29.22.10 host 210.93.149.28 eq smtp (hitcnt=0) 0x6aba8cbb \naccess-list VN2_access_in line 106 extended permit object-group CST-PRT_200043_000011 host 172.16.29.3 object-group CST-NET_200043_000043 (hitcnt=0) 0x385da5a4\naccess-list VN2_access_in line 108 extended permit object-group CST-PRT_200043_000047 object-group CST-NET_200043_000046 object-group CST-NET_200043_000047 (hitcnt=0) 0x2408c494\naccess-list VN2_access_in line 133 extended permit object-group CST-PRT_200043_000068 object-group CST-NET_200043_000004 host 203.248.240.140 (hitcnt=0) 0x5c88c7fe \naccess-list VN2_access_in line 136 extended permit tcp host 172.29.22.14 host 210.93.181.140 eq www log informational interval 300 (hitcnt=0) 0x44453cbf \naccess-list OUT_access_in line 7 extended permit icmp any any echo (hitcnt=0) 0x23facbd6 \naccess-list OUT_access_in line 8 extended permit icmp any any echo-reply (hitcnt=0) 0x4206f227 \naccess-list OUT_access_in line 13 extended permit tcp any host 172.16.62.2 eq https log informational interval 300 (hitcnt=0) 0x5d8cb7ca \naccess-list OUT_access_in line 28 extended permit object-group CST-PRT_200043_000016 any host 172.16.62.6 (hitcnt=0) 0xf4ff5bf0"



print(getAcl(test,defalut))
#print(serviceToPort('teresds'))