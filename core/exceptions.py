import traceback

import jimi

class concurrentCrash(Exception):
    """Concurrent crash"""
    pass

class triggerConcurrentCrash(Exception):
    """Trigger concurrent crash"""
    pass

class workerKilled(Exception):
    def __init__(self,workerID,workerName):
        self.workerName = workerName
        self.workerID = workerID
        jimi.logging.debug("Error: Worker killed. workerName='{0}', workerID='{1}'".format(self.workerName,self.workerID),-1)
        jimi.systemTrigger.failedTrigger(self.workerName,self.workerID,"WorkerKilled","")
        
    def __str__(self):
        return "Error: Worker killed. workerName='{0}', workerID='{1}'".format(self.workerName,self.workerID)

class workerCrash(Exception):
    def __init__(self,workerID,workerName,trace):
        self.workerName = workerName
        self.workerID = workerID
        self.trace = trace
        jimi.logging.debug("Error: Worker crash. workerName='{0}', workerID='{1}', trace='{2}'".format(self.workerName,self.workerID,self.trace),-1)
        jimi.systemTrigger.failedTrigger(self.workerName,self.workerID,"WorkerCrash",self.trace)

    def __str__(self):
        return "Error: Worker killed. workerName='{0}', workerID='{1}', trace='{2}'".format(self.workerName,self.workerID,self.trace)

class actionCrash(Exception):
    def __init__(self,actionID,actionName,exception):
        self.actionName = actionName
        self.actionID = actionID
        self.trace = ''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__))
        jimi.logging.debug("Error: Action Crashed. actionName='{0}', actionID='{1}', trace='{2}'".format(self.actionName,self.actionID,self.trace),-1)
        jimi.systemTrigger.failedAction(self.actionName,self.actionID,"actionCrashed",self.trace)

    def __str__(self):
        return "Error: Worker Crashed. workerName='{0}', workerID='{1}', trace='{2}'".format(self.workerName,self.workerID,self.trace)

class linkCrash(Exception):
    def __init__(self,flowID,exception):
        self.flowID = flowID
        self.trace = ''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__))
        jimi.logging.debug("Error: Link Crashed. flowID='{0}', trace='{2}'".format(self.flowID,self.trace),-1)

    def __str__(self):
        return "Error: Link Crashed. flowID='{0}', trace='{1}'".format(self.flowID,self.trace)

class functionCallFailure(Exception):
    def __init__(self,functionName,trace):
        self.functionName = functionName
        self.trace = trace
        
    def __str__(self):
        return "Error: Exception during function call. funcation='{0}', trace='{1}'".format(self.functionName,self.trace)

class variableDefineFailure(Exception):
    def __init__(self,varDict,exception):
        self.varDict = varDict
        self.trace = ''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__))
        
    def __str__(self):
        return "Error: Exception setting variable. varDict='{0}', trace='{1}'".format(self.varDict,self.trace)