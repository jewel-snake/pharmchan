import uuid
import hashlib
import json

# TODO: create own error types
# TODO: add docstrings
class MEOutgo:
    #comment = ''
    #id = None
    #from_id = None
    #value = None
    def __init__(self, value: float,from_id: uuid.UUID, comment: str = ''):
        self.id = None
        self.from_id = None
        self.value = None
        self.comment = ''

        if not isinstance(comment, str):
            raise NameError("comment is not a string")
        if not isinstance(value, (float,int,NoneType)):
            raise NameError("value is not float")
        if not isinstance(from_id, uuid.UUID):
            raise NameError("value is not a uuid")
        self.comment = comment
        self.value = value
        self.from_id = from_id
        self.id = uuid.uuid1()
        
  
class MEVolume:
    #comment = ''
    #id = None
    #name = ''
    #value = None
    def __init__(self, value: float,name: str = '', comment: str = ''):
        self.id = None
        self.name = ''
        self.comment = ''
        self.value = None

        if not isinstance(value, (float,int,NoneType)):
            raise NameError("value is not float")
        if not isinstance(comment, str):
            raise NameError("value is not a string")
        if not isinstance(name, str):
            raise NameError("value is not a string")
        self.value = value
        self.comment = comment
        self.name = name
        self.id = uuid.uuid1()

class METransfer:
    #comment = ''
    #id = None
    #from_id = None
    #to_id = None
    #value = None
    def __init__(self,value: float, from_id: uuid.UUID, to_id: uuid.UUID, comment: str = ''):
        self.id = None
        self.from_id = None
        self.to_id = None
        self.value = None
        self.comment = ''

        if not isinstance(value, (float,int,NoneType)):
            raise NameError("value is not float")
        if not isinstance(comment, str):
            raise NameError("value is not a string")
        if not isinstance(from_id, uuid.UUID):
            raise NameError("from_id is not a uuid")
        if not isinstance(to_id, uuid.UUID):
            raise NameError("to_id is not a uuid")
        if from_id is None:
            raise NameError("from_id is None")
        if to_id is None:
            raise NameError("to_id is None")
        if from_id == to_id:
            raise NameError("from_id can not be equal to_id")
        self.value = value
        self.from_id = from_id
        self.to_id = to_id
        self.comment = comment
        self.id = uuid.uuid1()
    
class MESystem:
    #volumes = {}
    #transfers = {}
    #outgos = {}
    #comment = ''
    #name = ''
    def __init__(self,volumes: list = [],transfers: list = [], outgos: list = [],name: str = '', comment: str = ''):
        self.volumes = {}
        self.transfers = {}
        self.outgos = {}
        self.comment = ''
        self.name = ''
        
        if not isinstance(volumes,list):
            raise NamedError("volumes is not list")
        
        if not all(map(lambda i: isinstance(i,MEVolume),volumes)):
            raise NamedError("volumes is not a list of MEVolume")
        
        if not isinstance(transfers,list):
            raise NamedError("transfers is not list")
        
        if not all(map(lambda i: isinstance(i,METransfer),transfers)):
            raise NamedError("transfers is not a list of METransfer")
        
        if not isinstance(outgos,list):
            raise NamedError("outgos is not list")
        
        if not all(map(lambda i: isinstance(i,MEOutgo),outgos)):
            raise NamedError("outgos is not a list of MEOutgo")
        
        if not isinstance(name,str):
            raise NameError("name has to be a string")
        if len(name) > 50:
            raise NameError("name's length has not to exceed 50")
        if not isinstance(comment,str):
            raise NameError("comment has to be a string")
        
        self.comment = comment
        self.name = name
        for v in volumes:
            if self.volumes.get(v.id) is not None:
                raise NameError("volume with such uuid already exists")
            self.volumes[v.id] = v
        for t in transfers:
            if self.volumes.get(t.from_id) is None:
                raise NameError("transfer entity references non existing volume entity as from")
            if self.volumes.get(t.to_id) is None:
                raise NameError("transter entity references non existing volume entity as to")
            self.transfers[t.id] = t
        for o in outgos:
            if self.volumes.get(o.from_id) is None:
                raise NameError("outgo entity references non existing volume entity as from")
            self.outgos[o.id] = o
            
    def add_volumes(self,volume):
        #pdb.breakpoint()
        if isinstance(volume, list):
            if not all(map(lambda i: isinstance(i,MEVolume),volumes)):
                raise NamedError("volumes is not a list of MEVolume")
            for v in volume:
                if self.volumes.get(v.id) is not None:
                    raise NameError("volume with such uuid already exists")
                self.volumes[v.id] = v
        elif isinstance(volume, MEVolume):
            if self.volumes.get(v.id) is not None:
                raise NameError("volume with such uuid already exists")
            self.volumes[v.id] = v
        else:
            raise NameError("volume parameter must be either MEVolume or list of MEVolume")

    def add_outgos(self,outgo):
        if isinstance(outgo, list):
            if not all(map(lambda i: isinstance(i,MEOutgos),outgos)):
                raise NamedError("outgos is not a list of MEOutgo")
            for o in outgo:
                if self.outgos.get(o.id) is not None:
                    raise NameError("outgo with such uuid already exists")
                if self.volumes.get(o.from_id) is None:
                    raise NameError("outgo references non existing volume as from")
                self.outgos[o.id] = o
        elif isinstance(outgo, MEoutgo):
            if self.outgos.get(o.id) is not None:
                raise NameError("outgo with such uuid already exists")
            if self.volumes.get(o.from_id) is None:
                    raise NameError("outgo references non existing volume as from")
            self.outgos[o.id] = o
        else:
            raise NameError("outgo parameter must be either MEOutgo or list of MEOutgo")

    def add_transfers(self,transfer):
        if isinstance(transfer, list):
            if not all(map(lambda i: isinstance(i,METransfers),transfers)):
                raise NamedError("transfers is not a list of METransfer")
            for o in transfer:
                if self.transfers.get(t.id) is not None:
                    raise NameError("transfer with such uuid already exists")
                if self.volumes.get(t.from_id) is None:
                    raise NameError("transfer references non existing volume as from")
                if self.volumes.get(t.to_id) is None:
                    raise NameError("transfer references non existing volume as to")
                self.transfers[t.id] = t
        elif isinstance(transfer, METransfer):
            if self.transfers.get(t.id) is not None:
                raise NameError("transfer with such uuid already exists")
            if self.volumes.get(t.from_id) is None:
                raise NameError("transfer references non existing volume as from")
            if self.volumes.get(t.to_id) is None:
                raise NameError("transfer references non existing volume as to")
            self.transfers[t.id] = t
        else:
            raise NameError("transfer parameter must be either METransfer or list of METransfer")

    def to_inner_representation(self):
        n = len(self.volumes)
        matrix = [[0.0]*n]*n
        volumes = [0.0]*n
        outgos = [0.0]*n
        layout = dict(map(lambda tupl: (tupl[1],tupl[0]),enumerate(self.volumes.keys())))
        for v in self.volumes.values():
            volumes[layout[v.id]] = v.value
        for t in self.transfers.values():
            matrix[layout[t.from_id]][layout[t.to_id]] = t.value
        for o in self.outgos.values():
            outgos[layout[o.from_id]] = o
        return {"volumes":volumes,"matrix":matrix,"outgos":outgos}
            
        #raise NameError("TODO")

class MEEncoder(json.JSONEncoder):
    def default(self, obj): # THEY ARE NOT UNIQUE
        if  isinstance(obj,MEVolume):
            return {"value":obj.value,"name":obj.name,"comment":obj.comment,"id":obj.id.hex,"__volume__":True}
        elif isinstance(obj,METransfer):
            return {"value":obj.value,"comment":obj.comment,"from_id":obj.from_id.hex,"to_id":obj.to_id.hex,"id":obj.id.hex,"__transfer__":True}
        elif isinstance(obj,MEOutgo):
            return {"value":obj.value,"comment":obj.comment,"from_id":obj.from_id.hex,"id":obj.id.hex,"__outgo__":True}
        elif isinstance(obj,MESystem):
            return {"volumes":[self.default(v) for v in obj.volumes.values()],"transfers":[self.default(t) for t in obj.transfers.values()],"outgos":[self.default(o) for o in obj.outgos.values()],"name":obj.name,"comment":obj.comment,"__system__":True}
        else:
            return json.JSONEncoder.default(self, obj)

    def as_system(dct):
        if "__system__" in dct:
            system = MESystem(dct.get('volumes'),dct.get('transfers'),dct.get('outgos'),dct.get('name'),dct.get('comment'))
            return system
        elif "__volume__" in dct:
            return MEEncoder.as_volume(dct)
        elif "__transfer__" in dct:
            return MEEncoder.as_transfer(dct)
        elif "__outgo__" in dct:
            return MEEncoder.as_outgo(dct)
        else:
            raise NameError("string does not represent system object")
            
    def as_volume(dct):
        if not ('__volume__' in dct) :
            raise NameError("string does not represent volume object")
        id = dct.get("id")
        name = dct.get("name")
        comment = dct.get("comment")
        value = dct.get("value")
        if id is None:
            raise NameError("json string does not contain id required field")
        if not isinstance(value,(float,int,NoneType)):
            raise NameError("value field has incorrect type if given json string")
        ret = MEVolume(value)
        ret.id = uuid.UUID(id)
        if name is not None:
            if isinstance(name,str):
                ret.name = name
            else:
                raise NameError("name optional field is not a string")
        if comment is not None:
            if isinstance(comment,str):
                ret.name = comment
            else:
                raise NameError("comment optional field is not a string")
        return ret
        
    def as_transfer(dct):
        if not ('__transfer__' in dct):
            raise NameError("string does not represent transfer object")
        id = dct.get("id")
        from_id = dct.get("from_id")
        to_id = dct.get("to_id")
        value = dct.get("value")
        comment = dct.get("comment")
        if id is None:
            raise NameError("json string does not contain id required field")
        if from_id is None:
            raise NameError("json string does not contain from_id required field")
        if to_id is None:
            raise NameError("json string does not contain to_id required field")
        if not isinstance(value,(float,int,NoneType)):
            raise NameError("value field has incorrect type if given json string")
        ret = METransfer(value,uuid.UUID(from_id),uuid.UUID(to_id))
        ret.id = uuid.UUID(id)
        if comment is not None:
            if isinstance(comment,str):
                ret.comment = comment
            else:
                raise NameError("comment optional field is not a sting")
        return ret

    def as_outgo(dct):
        if not ('__outgo__' in dct):
            raise NameError("string does not represent outgos object")
        id = dct.get("id")
        from_id = dct.get("from_id")
        value = dct.get("value")
        comment = dct.get("comment")
        if id is None:
            raise NameError("json string does not contain id required field")
        if from_id is None:
            raise NameError("json string does not contain from_id required field")
        if not isinstance(value,(float,int,NoneType)):
            raise NameError("value field has incorrect type if given json string")
        ret = MEOutgo(value,uuid.UUID(from_id))
        ret.id = uuid.UUID(id)
        if comment is not None:
            if isinstance(comment,str):
                ret.comment = comment
            else:
                raise NameError("comment optional field is not a sting")
        return ret

class DataSet:
    def __init__(self,tau: list, concentrations: dict,name: str, description: str = ''):
        if not isinstance(tau,list):
            raise NameError("tau must be a list")
        if not isinstance(concentrations,dict):
            raise NameError("concentratnions must be a dictionary")
        if not all(lambda i: isnistance(i,(float,int)),tau):
            raise NameError("tau must be a list of numeric values")
        if not all(lambda i: isinstance(i,str),concentrations.keys()):
            raise NameError("concentrations must have names of volumes as keys")
        if not all(lambda i: isinstance(i,list),concentrations.values()):
            raise NameError("concentrations must have lists as values")
        if not all(lambda i: all(lambda j: isinstance(j,(int,float))),concentrations.values()):
            raise NameError("concentrations must have lists of numeric values as values")
        if not isinstance(name,str):
            raise NameError("name must be a string")
        if not isinstance(description,str):
            raise NameError("description must be a string")
        self.tau = tau
        self.concentrations = concentrations
        self.name = name
        self.description = description

    def bind(binder: MESystem, bind_names: dict):
        if not isinstance(binder,MESystem):
            raise NameError("binder must be of MESystem type")
        if not isinstance(bind_names: dict):
            raise NameError("bind_names must be a dictionary")
        if not all(lambda i: isinstance(i,str),bind_names.keys()):
            raise NameError("bind_names must have names of system's volumes as keys of type str")
        if not all(lambda i: isinstance(i,str),bind_names.values()):
            raise NameError("bind_names must have names of dataset's volumes as valuse of type str")
        known_compartments = []
        theoretic_x = self.tau
        theoretic_y = []
        for index,v in enumerate(binder.volumes.values()):
            if bind_names.get(v.name) is not None:
                if self.concentrations.get(bind_names[v.name]) is None:
                    raise NameError(f"could not bind system's name {v.name} to {bind_names[v.name]}. there is no such name in dataset")
                known_compartments.append(index)
                teoretic_y.append(self.concentrations[bind_names[v.name]])
        return (known_compartments,theoretic_x,theoretic_y)
                
        
class DataSetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,DataSet):
            return {"__dataset__":True,"name":obj.name,"description":obj.description,"tau":obj.tau,"values":obj.values}
        else:
            return json.JSONEncoder.default(self, obj)           
    def as_dataset(dct):
        if not ("__dataset__" in dct):
            raise NameError("string does not represent dataset object")
        name = dct.get("name")
        description = dct.get("description")
        tau = dct.get("tau")
        concentrations = dct.get("concentrations")
        if not isinstance(name,str):
            raise NameError("name must be a string")
        if not isinstance(description,str):
            raise NameError("description must be a string")
        if not isinstance(tau,list):
            raise NameError("tau must be a list")
        if not isinstance(concentrations,dict):
            raise NameError("concentrations must be a dict")
        isnum = lambda x: isinstance(x,(float,int))
        isstr = lambda x: isinstance(x,str)
        #islist = lambda x: isinstance(x,list)
        if not all(concentrations.keys(),isstr):
            raise NameError("keys must be strings")
        for v in concentrations.values():
            if not isinstance(v,list):
                raise NameError("concentrations must be lists")
            if not all(v,isnum):
                raise NameError("concentrations must be list of numbers")
        return DataSet(tau,concentrations,name,descriptions)
        
