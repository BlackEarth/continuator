
from .continuator import Continuator

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
