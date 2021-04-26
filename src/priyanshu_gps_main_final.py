# main program file

import fetch
import decode
import execute
import memory
import Writeback

def assemble():
    instruction_dict = {}  # dictionary storing instructions
    data_dict = {}  # dictionary storing data in memory

    reg = {}  # registers
    write_df_reg = {}
    val_df_reg = {}
    clock=1
    reg[0] = '0x0'
    for i in range(32):
        reg[i] = '0x00000000'
        write_df_reg[i] = 0
        if i == 2:
            reg[i] = '0x7FFFFFF0'
        if i == 3:
            reg[i] = '0x10000000'


    file = open("data.mc", "r")

    instruction_dict, data_dict = fetch.fetch_file(file)

    pc = "0x0"  # initial pc is by default 0x0
    pc_temp = "0x0"
    pc = fetch.increment_pc(pc)
    decoded_info = {}
    rz = hex(0)
    rm = hex(0)
    muxy = hex(0)
    btb = {}
    mem_pc = []
    write_pc = []
    execute_pc = []
    decode_pc = []
    fetch_pc = []
    decode_pc.append("0x0")
    control_inst = False
    remove_decode = False
    flowchart_list=[]
    output=""
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output]
    return reg,instruction_dict,data_dict,clock,varlist
def runstep(reg,instruction_dict,data_dict,clock,varlist):
    pc=varlist[0]
    pc_temp=varlist[1]
    decoded_info=varlist[2]
    rz=varlist[3]
    rm=varlist[4]
    muxy=varlist[5]
    btb=varlist[6]
    mem_pc=varlist[7]
    write_pc=varlist[8]
    execute_pc=varlist[9]
    decode_pc=varlist[10]
    fetch_pc=varlist[11]
    control_inst=varlist[12]
    remove_decode=varlist[13]
    write_df_reg=varlist[14]
    val_df_reg=varlist[15]
    flowchart_list=varlist[16]
    output=varlist[17]
    output=""
    if len(write_pc) == 0 and len(mem_pc) == 0 and len(execute_pc) == 0 and len(decode_pc) == 0:
        varlist=[-1,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output]
        return reg,instruction_dict,data_dict,clock,varlist
    clock += 1

    # write_back
    if len(write_pc) != 0:
        this_pc = write_pc[0]
        write_pc.pop(0)

        if('rd' in decoded_info[this_pc]):
            x = int(decoded_info[this_pc]['rd'], 2)
            write_df_reg[x] = write_df_reg[x]-1  # as now its use has ended
            if(x == 0):
                write_df_reg[x] = 0

            if(int(decoded_info[this_pc]['rd'], 2) != 0):
                reg, temp_string_writeback = Writeback.write_back(
                    muxy, [decoded_info[this_pc]['type'], decoded_info[this_pc]['opr'], decoded_info[this_pc]['rd']], reg)
                output+=temp_string_writeback


    # memory
    if len(mem_pc) != 0:
        this_pc = mem_pc[0]

        mem_pc.pop(0)
        write_pc.append(this_pc)

        rm = None
        if 'rs2' in decoded_info[this_pc]:
            rm = reg[int(decoded_info[this_pc]['rs2'], 2)]
            rm = rm[2:]
            rm = "0"*(8-len(rm))+rm
        if(int(rz, 16) < 0):
            if(len(rz) != 11):
                rz = '-'+rz[1:3]+'0'*(11-len(rz))+rz[3:]
        else:
            if(len(rz) != 10):
                rz = rz[:2]+'0'*(10-len(rz))+rz[2:]

        opr = decoded_info[this_pc].get('opr', '-1')

        muxy, data_dict, temp_string_memory = memory.memory(
            0x0, rz, [decoded_info[this_pc]['type'], decoded_info[this_pc]['opr']], rm, data_dict, pc_temp)
        output+=temp_string_memory

    # execute
    if len(execute_pc) != 0:
        this_pc = execute_pc[0]
        for x in decoded_info[this_pc]:
            output+=str(x)+" is "+str(decoded_info[this_pc][x])+"\n"
        execute_pc.pop(0)
        mem_pc.append(this_pc)

        pc_temp = fetch.increment_pc(this_pc)

        rz, pc_final, temp_string_execute = execute.execute(
            decoded_info[this_pc], reg, pc_temp)
        output+=temp_string_execute
        rz = hex(rz)
        buffer_exec = rz
        rd = decoded_info[this_pc].get('rd', '-1')
        if(rd != '-1'):
            x = int(rd, 2)
            val_df_reg[x] = rz
            if(x == 0):
                val_df_reg[x] = 0
            if(decoded_info[this_pc]['opr'] == 'lw'):
                val_df_reg[x] = data_dict[rz]
        if control_inst:
            control_inst = False
            if this_pc in btb:
                if pc_final == btb[this_pc]:
                    pass
                else:
                    remove_decode = True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0] == pc_final:
                            remove_decode = False
            else:
                btb[this_pc] = pc_final
                if pc_final == fetch.increment_pc(this_pc):
                    pass
                else:
                    remove_decode = True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0] == pc_final:
                            remove_decode = False

    # decode
    if len(decode_pc) != 0:
        this_pc = decode_pc[0]
        output+="Fetch Instruction "+instruction_dict[this_pc]+" from address "+this_pc+"\n"
        flowchart_list.append(this_pc)
        decode_pc.pop(0)
        flg = 0
        if remove_decode == False:
            execute_pc.append(this_pc)
            flg = 1
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.append(fetch.increment_pc(this_pc))
        else:
            flowchart_list[len(flowchart_list)-1]=-1
        remove_decode = False
        instruction_register = instruction_dict[this_pc]

        pc_temp = fetch.increment_pc(this_pc)
        decoded_info[this_pc] = decode.decode(instruction_register)
        

        rd = decoded_info[this_pc].get('rd', '-1')
        rs1 = decoded_info[this_pc].get('rs1', '-1')
        rs2 = decoded_info[this_pc].get('rs2', '-1')
        if(rs1 != '-1' and flg == 1):
            x = int(rs1, 2)
            if(write_df_reg[x] == 1):  # that means data forwarding is required
                reg[x] = val_df_reg[x]  # i add the value stored in the buffer
        if(rs2 != '-1' and flg == 1):
            x = int(rs2, 2)
            if(write_df_reg[x] == 1):  # that means data forwarding is required
                reg[x] = val_df_reg[x]  # i add the value stored in the buffer

        if(rd != '-1' and flg == 1):
            x = int(rd, 2)
            if(x != 0):
                write_df_reg[x] = write_df_reg[x]+1
            else:
                write_df_reg[x] = 0

        # print(write_df_reg)
        opr = decoded_info[this_pc]['opr']
        if(opr == 'jal' or opr == 'jalr' or opr == 'beq' or opr == 'bne' or opr == 'bge' or opr == 'blt'):
            # print("cheee")
            control_inst = True
            if len(decode_pc) != 0:

                decode_pc.pop()
            if this_pc in btb:
                if btb[this_pc] in instruction_dict:
                    decode_pc.append(btb[this_pc])
            else:
                if fetch.increment_pc(this_pc) in instruction_dict:
                    decode_pc.append(fetch.increment_pc(this_pc))

    # print(remove_decode)

    print(data_dict)
    print(reg)
    print(clock)
    varlist=[-1,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output]
    return reg,instruction_dict,data_dict,clock,varlist