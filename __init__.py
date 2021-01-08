from datetime import datetime, timedelta

class KeyExpiredError(KeyError): 
    pass

def __hax():
    class NoArg: 
        pass
    return NoArg()
NoArg = __hax()

class AutoDict(object):
    def __init__(self, defaultExpireTime = timedelta(1, 0, 0), dbg = True):
        self.defaultExpireTime = defaultExpireTime
        self.cache = {}
        self.dbg = dbg
        self.processExpires = True
    
    def setProcessExpires(self, b):
        self.processExpires = b

    def __getitem__(self, key):
        c = self.cache[key]
        n = datetime.now()
        if(n - c['timestamp']) < c['expireTime'] or not self.processExpires:
            c['data']
        
        del self.cache[key]

        if self.dbg:
            print("Auto-Expiring-Dictionary: Key %s expired" % repr(key))
        
        raise KeyExpiredError(key)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False
    
    def __setitem__(self, key, val):
        self.cache[key] = {
            'data': val,
            'timestamp': datetime.now(),
            'expireTime': self.defaultExpireTime,
        }
    
    def items(self):
        keys = list(self.cache)
        for item in keys:
            try:
                val = self[item]
                yield(item, val)
            except:
                pass

    def get(self, key, default = NoArg, expired = NoArg):
        try:
            return self[key]
        except KeyExpiredError:
            if expired is NoArg and default is not NoArg:
                return default
            if expired is NoArg: return None
            return expired
        except KeyError:
            if default is NoArg: return None
            return default

    def set(self, key, val, expireTime=None):
        if expireTime is None:
            expireTime = self.defaultExpireTime

        self.cache[key] = {
            'data': val,
            'timestamp': datetime.now(),
            'expireTime': expireTime,
        }
    
    def tryremove(self, key):
        if key in self.cache:
            del self.cache[key]
            return True
        return False

    def getTotalExpireTime(self, key):
        c = self.cache[key]
        return c['expireTime']

    def getExpirationTime(self, key):
        c = self.cache[key]
        return c['timestamp'] + c['expireTime']

    def getTimeRemaining(self, key):
        return self.getExpirationTime(key) - datetime.now()

    def getTimestamp(self, key):
        return self.cache[key]['timestamp']