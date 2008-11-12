import threading, gtk
from gettext import gettext as _
from gettext import ngettext
from gourmet.gdebug import *

class Terminated (Exception):
    def __init__ (self, value):
        self.value=value
    def __str__(self):
        return repr(self.value)

class SuspendableThread (threading.Thread):
    """A SuspendableThread. We take a runnerClass which must have a
    run, suspend, terminate, and resume method. We then launch our thread
    and provide methods by the same name that interface with our runnerClass.
    Before running the run() method, we call pre_hooks. Afterward we call any
    post_hooks. (Pre and post hooks get called with this instance as their only
    argument."""
    def __init__ (self, runnerClass, name=None, pre_hooks=[], post_hooks=[],
                  display_errors=True):
        self.display_errors=display_errors
        self.c = runnerClass
        self.pre_hooks=pre_hooks
        self.post_hooks=post_hooks
        self.name = name
        self.completed = False
        debug("SuspendableThread starting thread.",2)
        self.initialize_thread()

    def initialize_thread (self):
        threading.Thread.__init__(self, target=self.target_func, name=name)

    def target_func (self):
        self.run_hooks(self.pre_hooks)
        try:
            debug('SuspendableThread Running %s'%self.c,3)
            self.c.run()
        except Terminated:
            import gourmet.dialogs.extras as de
            de.show_message(
                    label=_("%s stopped."%self.name.title()),
                    sublabel=_("%s was interrupted by user request."%self.name.title())
                    )
        except:            
            if self.display_errors:
                self._threads_enter()
                import gourmet.dialogs.extras as de
                de.show_traceback(
                    label=_("%s interrupted")%self.name.title(),
                    sublabel=_("There was an error during %s.")%self.name,
                    )
                self._threads_leave()
            self.run_hooks(self.post_hooks)
            raise
        else:
            self.completed = True
            self.run_hooks(self.post_hooks)

    def run_hooks (self, hooks):
        """We hand all hooks ourselves as an argument"""
        for h in hooks:
            debug('Running %s'%h,3)
            h(self)
        
    def suspend (self):
        debug('suspending thread',0)
        self.c.suspend()

    def resume (self):
        debug('resuming thread',0)
        self.c.resume()

    def terminate (self):
        debug('terminating thread',0)
        self.c.terminate()

    def _threads_enter (self):
        gtk.gdk.threads_enter()

    def _threads_leave (self):
        gtk.gdk.threads_leave()

class SuspendableDeletions:
    def __init__ (self, rg, recs):
        self.suspended = False
        self.terminated = False
        self.recs = recs
        print 'SuspendableDeletions handed ',recs
        self.rg = rg
        
    def check_for_sleep (self):
        if self.terminated:
            raise Terminated("Deletion Terminated!")
        while self.suspended:
            if self.terminated:
                raise "Deletion Terminated!"
            time.sleep(1)
    
    def run (self):
        debug('running GourmetThreads.py',0)
        rtot = len(self.recs)
        n = 0        
        for r in self.recs:
            self.check_for_sleep()
            self.rg.set_progress_thr(float(n)/float(rtot),
                                     _("Deleting recipes from database... (%s of %s deleted)"%(n,rtot))
                                       )
            self.rg.delete_rec(r)
            n += 1
        msg = ngettext('Deleted %s recipe','Deleted %s recipes',
                       rtot)%rtot
        self.rg.reset_prog_thr(message=msg)
        self.rg.doing_multiple_deletions=False

    def suspend (self): self.suspended = True

    def terminate (self): self.terminated = True

    def resume (self): self.suspended = False

def get_lock ():
    return threading.Lock()

def gtk_enter ():
    print 'threads_enter'
    gtk.gdk.threads_enter()

def gtk_leave ():
    print 'threads_leave'
    gtk.gdk.threads_leave()

def gtk_threads_init ():
    print 'threads_init'
    gtk.gdk.threads_init()