from irmodel import MEVolume, MEOutgo, METransfer, MESystem,MEEncoder
import json

def init_ir():
    volume1 = MEVolume(228,'liver')
    volume2 = MEVolume(629, 'heart')
    transfer1 = METransfer(0.4586,volume1.id,volume2.id,'k12')
    transfer2 = METransfer(0.01919,volume2.id,volume2.id,'k21')
    outgo1 = MEOutgo(0.0309,volume1.id,'k10')
    system = MESystem([volume1,volume2],[transfer1,transfer2],[outgo1])
    return system

def init_json():
    s = init_ir()
    return json.dumps(s,cls=MEEncoder)

def from_json_str():
    return json.loads(init_json(),object_hook=MESystem.as_system)

def main():
    volume1 = MEVolume(228,'liver')
    volume2 = MEVolume(629, 'heart')
    transfer1 = METransfer(0.4586,volume1.id,volume2.id,'k12')
    transfer2 = METransfer(0.01919,volume2.id,volume1.id,'k21')
    print("transfer1.from_id:\t",transfer1.from_id)
    print("transfer1.to_id:\t",transfer1.to_id)
    print("transfer2.from_id:\n",transfer2.from_id)
    print("transfer2.to_id:\n",transfer2.to_id)
    outgo1 = MEOutgo(0.0309,volume1.id,'k10')
    s = MESystem([volume1,volume2],[transfer1,transfer2],[outgo1])
    st = json.dumps(s,cls=MEEncoder)
    print(st)
    s2 = json.loads(st,object_hook=MESystem.as_system)
    print("s2: ",s2.volumes)
    print("s: ",s.volumes)
    print("s2: ",s2.transfers)
    print("s: ",s.transfers)
    print("s2: ",s2.outgos)
    print("s: ",s.outgos)
    s.to_inner_representation()
    

if __name__ == '__main__':
    main()
