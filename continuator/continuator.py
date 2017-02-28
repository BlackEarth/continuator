
import sys 
import pickle, types
from bl.id import random_id        # implements id.random_id(), an id string

assert 'Stackless' in sys.version or 'PyPy' in sys.version   # requires Stackless or PyPy

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
            new_cid = random_id(32)
            self.continuations[new_cid] = pickle.dumps(g)
            return res, new_cid
            
        except StopIteration:
            # that continuation is expired
            return None, None
      
    def reset(self):
        self.continuations = {}
      
      
