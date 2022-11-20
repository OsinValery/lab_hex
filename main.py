
from commands_parser import *

with open("SP_6.hex", 'r') as file:
    texts = file.read()

texts = [ t for t in texts.split('\n') if t != '' ]
commands = []
assembler = []

for text_line in texts:
    print(text_line)
    content = text_line[1:]

    record_length = content[0:2]
    r_l = int(record_length, base=16)
    print(f'    record length is {r_l} ({record_length})')

    offset_length = content[2:6]
    offset = int(offset_length, base=16)
    print(f"    offset = {offset} ({offset_length})")

    rec_type = content[6:8]
    rec_t = int(rec_type, base=16)
    print(f"    record type = {rec_t} ({rec_type})")

    data_hex = content[8:8+r_l*2]
    print(f"    data = {data_hex}")

    if rec_t == 0:
        pos = 0
        while pos < len(data_hex):
            c = data_hex[pos:pos+4]
            commands.append(c)
            pos += 4

    control_summ = content[8+r_l*2:]
    print(f"    control sum: {control_summ}")


print('\n\nparse data\n')

was_long_command = False
old_command = ""

for command in commands:
    real_command = command[2:4] + command[0:2]
    bin_command = ''
    for char in real_command:
        bin_command += Bytes[char]

    if not was_long_command:
        command_str = getCommand(bin_command)
        if command_str == -1:
            was_long_command = True
            old_command = bin_command
            continue
    else:
        was_long_command = False
        command_str = getCommand(old_command+bin_command)
    if command_str != None:
        assembler.append(str(command_str))
    else:
        command_str = "unknown"
    print(f'command {command} -> {real_command} -> {bin_command} -> {command_str}')


print("\n\ntotal programm:\n")
for  command in assembler:
    print(command)

