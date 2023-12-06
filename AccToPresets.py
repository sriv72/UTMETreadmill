acc_file_name = 'Accelerations.txt'
input_file_name = 'UTME_Treadmill_Index_Presets_Default.txt'
output_file_name = 'UTME_Treadmill_Index_Presets.txt'

with open(input_file_name, 'r') as input_file:
    # Read all lines into a list
    idx_lines = input_file.readlines()

with open(acc_file_name, 'r') as acc_file:
    # Read all lines into a list
    acc_lines = acc_file.readlines()

acc_lines = [float(line) for line in acc_lines]

for i in range(len(idx_lines)):
    if idx_lines[i] == 'Acceleration,10000000\n':
        idx_lines[i] = f'Acceleration,{int(acc_lines[0] * 10000000)}\n'
    elif idx_lines[i] == 'Deceleration,10000000\n':
        idx_lines[i] = f'Deceleration,{int(acc_lines[0] * 10000000)}\n'
    elif idx_lines[i] == 'Acceleration,20000000\n':
        idx_lines[i] = f'Acceleration,{int(acc_lines[1] * 10000000)}\n'
    elif idx_lines[i] == 'Deceleration,20000000\n':
        idx_lines[i] = f'Deceleration,{int(acc_lines[1] * 10000000)}\n'
    elif idx_lines[i] == 'Acceleration,30000000\n':
        idx_lines[i] = f'Acceleration,{int(acc_lines[2] * 10000000)}\n'
    elif idx_lines[i] == 'Deceleration,30000000\n':
        idx_lines[i] = f'Deceleration,{int(acc_lines[2] * 10000000)}\n'
    elif idx_lines[i] == 'Acceleration,40000000\n':
        idx_lines[i] = f'Acceleration,{int(acc_lines[3] * 10000000)}\n'
    elif idx_lines[i] == 'Deceleration,40000000\n':
        idx_lines[i] = f'Deceleration,{int(acc_lines[3] * 10000000)}\n'
    elif idx_lines[i] == 'Acceleration,50000000\n':
        idx_lines[i] = f'Acceleration,{int(acc_lines[4] * 10000000)}\n'
    elif idx_lines[i] == 'Deceleration,50000000\n':
        idx_lines[i] = f'Deceleration,{int(acc_lines[4] * 10000000)}\n'

with open(output_file_name, "w") as output_file:
    output_file.writelines(idx_lines)