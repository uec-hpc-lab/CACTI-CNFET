#!/usr/bin/env python3
import re 
import subprocess as sp
from subprocess import PIPE

# Do you want to create heat maps?
create_heat_map = True 
# Do you want to fix the number of rows? 'False' means fixing the number of columns if 'create_heat_map = True'
keep_row = False
# Technology node
technology = 5

# 'zeropercentage' only affects single-ended SRAMs.
def cache_cfg_setting(zeropercentage = '50'):
    cache_cfg = "cache.cfg"
    with open(cache_cfg) as file:
        configFile = file.read()
    # Activate the test mode
    configFile = re.sub("\n-test 0", "\n//-test 0", configFile)
    configFile = re.sub("//-test 1", "-test 1", configFile)

    with open(cache_cfg, mode = "w") as file:
        file.write(configFile)

def cacti_input(input, process):
    process.stdin.write(input.encode())
    process.stdin.flush()

# 'round_num' means the number of digits rounded.
def record_data(pattern, file_name, round_num = -1, is_print_output = False, cplb = '8', se_wl_risetime = '50'):
    cacti = sp.Popen(
        ['./cacti', '-infile', 'cache.cfg'],
        stdin=sp.PIPE, 
        stdout=sp.PIPE,
        stderr=sp.PIPE
    )
    #print("record_data:",pattern)
    for (i, j) in sizelist:
        input = (i+"\n"+j+"\n20\n")
        cacti_input(input, cacti)
    # Stop the test mode
    cacti_input(("-1\n"), cacti)
    cacti.stdin.close()
    #print("cacti.stdin.close:",input)
    cacti.wait()
    output = (cacti.stdout.read()).decode()
    if is_print_output:
        print(output)
    matches = re.findall(pattern, output)
    sp.Popen("mkdir -p ./cacti_result_raw", shell=True, stdout=PIPE).communicate()[0]
    f = open("./cacti_result_raw/"+file_name+".csv", "w")
    print("row,col,result", file=f)
    for (i, j), result in zip(sizelist,matches):
        if round_num < 0:
            print(i+","+j+","+result, file=f)
        else:
            round_result = f"{round(float(result), round_num)}"
            print(i+","+j+","+round_result, file=f)
    f.close()

sp.Popen("make").communicate()[0]

cache_cfg_setting()
rows_and_cols = ['32','48','64','80','96','112','128']
sizelist = []
for i in ['32', '48', '64', '80', '96', '112','128']:
    for j in rows_and_cols:
        sizelist.append((i,j))
pattern = r"CellArray and precharge Leakage:\t(.*)\tuW"
record_data(pattern, "cellarray_leakage", round_num=3)
pattern = r"Read:\t(.*)\tfJ"
record_data(pattern, "cellarray_read", round_num=3)
pattern = r"Write:\t(.*)\tfJ"
record_data(pattern, "cellarray_write", round_num=3)
pattern = r"Subarray Leakage:\t(.*)\tuW"
record_data(pattern, "subarray_leakage", round_num=3)
pattern = r"Subarray read total:\t(.*)\tfJ"
record_data(pattern, "subarray_read", round_num=3)
pattern = r"Subarray write total:\t(.*)\tfJ"
record_data(pattern, "subarray_write", round_num=3)
pattern = r"Delay in senseamp:\t(.*)\tps"
record_data(pattern, "senseamp_delay")
pattern = r"subarray delay:\t(.*)\tps"
record_data(pattern, "subarray_delay", round_num=3)
pattern = r"row decoder delay:\t(.*)"
record_data(pattern, "rowdecoder_delay")
sizelist=[]
for i in rows_and_cols:
    sizelist.append(('128', i))
pattern = r"CellArray and precharge Leakage:\t(.*)\tuW"
record_data(pattern, "cellarray_leakage2", round_num=3)
pattern = r"Read:\t(.*)\tfJ"
record_data(pattern, "cellarray_read2", round_num=3)
pattern = r"Write:\t(.*)\tfJ"
record_data(pattern, "cellarray_write2", round_num=3)
pattern = r"Subarray Leakage:\t(.*)\tuW"
record_data(pattern, "subarray_leakage2", round_num=3)
pattern = r"Subarray read total:\t(.*)\tfJ"
record_data(pattern, "subarray_read2", round_num=3)
pattern = r"Subarray write total:\t(.*)\tfJ"
record_data(pattern, "subarray_write2", round_num=3)
pattern = r"Delay in senseamp:\t(.*)\tps"
record_data(pattern, "senseamp_delay2")
pattern = r"subarray delay:\t(.*)\tps"
record_data(pattern, "subarray_delay2", round_num=3)
pattern = r"row decoder delay:\t(.*)"
record_data(pattern, "rowdecoder_delay2")


sizelist = []
rows_and_cols = ['32','48','64','80','96','112','128']
for i in rows_and_cols:
    sizelist.append(('32',i))
pattern = r"write driver leakage:\t(.*)\tuW"
record_data(pattern, "writedriver_leakage")
pattern = r"write driver dynamic energy:\t(.*)\tfJ"
record_data(pattern, "writedriver_write")
pattern = r"sense amp leakage:\t(.*)\tuW"
record_data(pattern, "senseamp_leakage")
pattern = r"row decoder dynamic energy:\t(.*)\tfJ"
record_data(pattern, "rowdecoder_read")
pattern = r"row decoder delay:\t(.*)\tps"
record_data(pattern, "rowdecoder_delay")
sizelist = []
rows_and_cols = ['32','48','64','80','96','112','128']
for i in rows_and_cols:
    sizelist.append((i,'32'))
pattern = r"row decoder leakage:\t(.*)\tuW"
record_data(pattern, "rowdecoder_leakage")
pattern = r"driver width nmos:\t(.*)\tuW"
record_data(pattern, "driver_width_nmos")
pattern = r"driver width pmos:\t(.*)\tuW"
record_data(pattern, "driver_width_pmos")
pattern = r"Delay in total bitline:\t(.*)\tps"
record_data(pattern, "bitline_delay", is_print_output=True)

rows_and_cols = ['32','48','64','80','96','112','128']
sizelist = []
for i in rows_and_cols:
    sizelist.append((i,i))
pattern = r"Subarray area:\t(.*) \(um\)^2"
record_data(pattern, "subarray_area")
