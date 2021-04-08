#main program file

import fetch
import decode
import execute
import memory
import Writeback

instruction_dict={}    #dictionary storing instructions
data_dict={}    #dictionary storing data in memory

reg={} #registers
reg[0]='0x0'
for i in range(32):
    reg[i]='0x00000000'
    if i==2:
        reg[i]='0x7FFFFFF0'
    if i==3:
        reg[i]='0x10000000'


file=open("sample.mc","r")

instruction_dict,data_dict = fetch.fetch_file(file)
#print(instruction_dict)
#print(data_dict)
#print(data_dict)
pc="0x0"    #initial pc is by default 0x0
pc_temp="0x0"
pc_final="0x0"

instruction_register=None

<<<<<<< HEAD
while(1):
    if pc not in instruction_dict:
        break
    instruction_register=instruction_dict[pc]
    pc_temp=fetch.increment_pc(pc)
    decoded_info=decode.decode(instruction_register)
    #print("HI ADITI",decoded_info)
=======
for i in range(80):
    if pc not in instruction_dict:
        break
    print("pc",pc)
    instruction_register=instruction_dict[pc]
    pc_temp=fetch.increment_pc(pc)
    decoded_info=decode.decode(instruction_register)
    print(decoded_info)
>>>>>>> 31eb8883be8e77578a3c8ed2bf0311e418eb1ea7
    rm=None
    
    if 'rs2' in decoded_info:
        rm=reg[int(decoded_info['rs2'],2)]
        rm=rm[2:]
        for i in range(8-len(rm)):
            rm="0"+rm
    #print(rm)
    #print(hex(int(decoded_info['imm'],2)))
    rz,pc_final=execute.execute(decoded_info,reg,pc_temp)
    
    #print(rz)
    rz=hex(rz)
<<<<<<< HEAD
=======
    print(rz,pc_final)
>>>>>>> 31eb8883be8e77578a3c8ed2bf0311e418eb1ea7
    if(len(rz)!=10):
        rz=rz[:2]+'0'*(10-len(rz))+rz[2:]
    #print(rz)
    
    muxy,data_dict=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
    #print(ry)
    if('rd' in decoded_info):
<<<<<<< HEAD
        reg=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
    pc=pc_final
    #print(reg)
print("Done")
#print(reg)
=======
        if(int(decoded_info['rd'],2)!=0):
            reg=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
    pc=pc_final
    print(reg,data_dict)
    #print(reg)
print("Done")
print(reg)
>>>>>>> 31eb8883be8e77578a3c8ed2bf0311e418eb1ea7
#print(data_dict)