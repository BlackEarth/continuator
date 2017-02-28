
import sys 
import pickle, types
from amplitude.lib import id        # implements id.random_id(), an id string

assert 'Stackless' in sys.version   # requires Stackless Python -- http://stackless.com

class Continuator:

    def __init__(self, f, *args, **kargs):
        g = f(*args, **kargs)
        assert type(g)==types.GeneratorType
        self.generator = pickle.dumps(g)
        self.continuations = {}
        
    def __call__(self, cid=None):
        try:
            if cid==None or self.continuations.get(cid) is None:
                g = pickle.loads(self.generator)
            else:
                g = pickle.loads(self.continuations[cid])
            res = next(g)
            new_cid = id.random_id()
            self.continuations[new_cid] = pickle.dumps(g)
            return res, new_cid
            
        except StopIteration:
            # that continuation is expired
            return None, None
      
    def reset(self):
        self.continuations = {}
      
      
class SessionContinuator(Continuator):
    
    def __init__(self, session, key, f, *args, **kargs):
        Continuator.__init__(self, f, *args, **kargs)
        self.session = session
        self.key = key
        if not self.session.has_key(self.key):
            self.session[self.key] = {}
            self.session.save()
        
    def __call__(self, cid=None):
        self.continuations = self.session[self.key]
        res, cid = Continuator.__call__(self, cid)
        self.session[self.key] = self.continuations
        self.session.save()
        return res, cid
        
    def reset(self):
        Continuator.reset(self)
        self.session[self.key] = {}
        self.session.save()
        
    def __del__(self):
        _=self.session.pop(self.key)
        self.session.save()
        