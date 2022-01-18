#실제 Airflow(D+)에서 수행하는 함수
def proc(interface, op, _d, _p) :
    _print(logger, ">>> proc:_d", _d)
    cache = RedisCache()
    db_client = proc_db.client(dbtype="mysql", _conn=info.get_connection(op[0]["conn"]))
    _print(logger, '쿼리: ', _p["api"])

    records = db_client.get_records(_p["api"], parameters=_p.get("parameters"))
    _print(logger, '>>> ucsd db records ', records)
    ret = []
    keys = [ 'filterName','portGroup','userType','status']
    
    for items in records :
        temp_d = {}
        for i, item in enumerate(items) :
            item = item.replace('-','_') if keys[i] == 'portGroup' else item
            temp_d[keys[i]] = item
            _print(logger, ">>>> temp_d[keys[{}]] : ".format(i), temp_d[keys[i]] )
        ret.append(temp_d)
    return ret