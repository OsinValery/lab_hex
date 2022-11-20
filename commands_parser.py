
Bytes = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",   
}

no_arg = { "1001010011111000": "CLI", "0000000000000000": "NOP", "1001010001111000": "SEI"}



def getCommand(command: str):
    if command in no_arg:
        return no_arg[command]
    
    if command[0:6] == "001011":
        r = command[6] + command[12:]
        d = command[7:12]
        R = int(r, base=2)
        D = int(d, base=2)
        return f"MOV R{D} R{R}"

    if command[0:4] == "1110":
        K = command[4:8] + command[12:16]
        r = command[8:12]
        R = int(r, base=2)
        return f"LDI R{R+16} {K}"
    
    if command[0:6] == "000011":
        r = command[6] + command[12:]
        d = command[7:12]
        R = int(r, base=2)
        D = int(d, base=2)
        return f"ADD R{D} R{R}"
    
    if command[0:7] == "1001010" and command[12:16] == "0011":
        d = command[7:12]
        D = int(d, base=2)
        return f"INC R{D}"
    
    if command[0:7] == "1001010" and command[12:16] == "1010":
        d = command[7:12]
        D = int(d, base=2)
        return f"DEC R{D}"
    
    if command[0:7] == "1001010" and command[12:16] == "0001":
        d = command[7:12]
        D = int(d, base=2)
        return f"NEG R{D}"

    if command[0:7] == "1001010" and command[12:16] == "0110":
        d = command[7:12]
        D = int(d, base=2)
        return f"LSR R{D}"

    if command[0:7] == "1001010" and command[12:16] == "0111":
        d = command[7:12]
        D = int(d, base=2)
        return f"ROR R{D}"

    if command[0:7] == "1001010" and command[12:16] == "0101":
        d = command[7:12]
        D = int(d, base=2)
        return f"ASR R{D}"
    
    if command[0:7] == "1001010" and command[12:15] == "110":
        if len(command) == 16:
            return -1
        d = command[7:12] + command[15:]
        D = int(d, base=2)
        return f"JMP {D}"

    if command[0:7] == "1001001" and command[12:16] == "1111":
        d = command[7:12]
        D = int(d, base=2)
        return f"PUSH R{D}"

    if command[0:7] == "1001000" and command[12:16] == "1111":
        d = command[7:12]
        D = int(d, base=2)
        return f"POP R{D}"   

    if command[0:7] == "1001010" and command[12:15] == "111":
        if len(command) == 16:
            return -1
        d = command[7:12] + command[15:]
        D = int(d, base=2)
        return f"CALL {D}"
    
    if command[0:9] == "100101010" and command[11:16] == "01000":
        return "RET"
    
    if command[0:7] == "1001010" and command[12:16] == "0000":
        d = command[7:12]
        D = int(d, base=2)
        return f"COM R{D}"   

    if command[0:6] == "000110":
        d = command[7:12]
        r = command[6] + command[12:16]
        D = int(D, base=2)
        R = int(R, base=2)
        return f"SUB R{D} R{R}"
    
    if command[1:4] == "0101":
        d = command[8:12]
        K = command[4:8] + command[12:16]
        d = int(d, base=2)
        K = int(K, base=2)
        return f"SUBI R{d+16} {K}"

    if command[0:8] == "10010110":
        K = command[8:10] + command[12:16]
        d = command[10:12]
        K = int(K, base=2)
        d = int(d, base=2)
        regs = ['R24', 'R26', 'R28', 'R30']
        return f'ADIW {regs[d]} {K}'
    
    if command[0:8] == "10010111":
        K = command[8:10] + command[12:16]
        d = command[10:12]
        K = int(K, base=2)
        d = int(d, base=2)
        regs = ['R24', 'R26', 'R28', 'R30']
        return f'SBIW {regs[d]} {K}'

    if command[0:6] == "000111":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"ADC R{d} R{r}"
    
    if command[0:6] == "000010":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"SBC R{d} R{r}"

    if command[0:4] == "0100":
        d = command[8:12]
        K = command[4:8] + command[12:16]
        d = int(d, base=2)
        K = int(K, base=2)
        return f"SBCI R{d} {K}"

    if command[0:6] == "001000":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"AND R{d} R{r}"

    if command[0:6] == "001010":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"OR R{d} R{r}"

    if command[0:4] == "0111":
        d = command[8:12]
        K = command[4:8] + command[12:16]
        d = int(d, base=2)
        K = int(K, base=2)
        return f"ANDI R{d+16} {K}"
    
    if command[0:4] == "0110":
        d = command[8:12]
        K = command[4:8] + command[12:16]
        d = int(d, base=2) + 16
        K = int(K, base=2)
        return f"ORI R{d} {K}"

    if command[0:6] == "001001":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"EOR R{d} R{r}"

    if command[0:6] == "001001":
        d = command[7:]
        d = int(d, base=2)
        return f"LSL R{d}"

    if command[0:6] == "000111":
        d = command[7:]
        d = int(d, base=2)
        return f"ROL R{d}"

    if command[0:8] == "11101111" and command[12:16] == "1111":
        d = int(command[8:12], base=2)
        return f"SEP R{d+16}"
    
    if command[0:6] == "001001":
        d = command[6:]
        d = int(d, base=2)
        return f"CLR R{d}"

    if command[0:4] == "1100":
        d = command[4:]
        return f"RJMP {d}  // digit can be negative, transform this bite digit to int"
    
    if command[0:4] == "1111":
        k = command[6:13]
        k = int(k, base=2)
        if command[4:6] == '00':
            if command[13:16] == "000":
                return f"BRCS {k} // digit can be negative, transform this bite digit to int"
            else:
                return f"BREQ {k} // digit can be negative, transform this bite digit to int"
        else:
            if command[13:16] == "000":
                return f"BRCC {k} // digit can be negative, transform this bite digit to int"
            else:
                return f"BRNE {k} // digit can be negative, transform this bite digit to int"

    if command[0:6] == "000101":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"CP R{d} R{r}"

    if command[0:6] == "000001":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"CPC R{d} R{r}"

    if command[0:4] == "0011":
        d = command[8:12]
        K = command[4:8] + command[12:16]
        d = int(d, base=2)
        K = int(K, base=2)
        return f"CPI R{d+16} {K}"

    if command[0:6] == "000100":
        r = command[6] + command[12:16]
        d = command[7:12]
        r = int(r, base=2)
        d = int(d, base=2)
        return f"CPSE R{d} R{r}"

    if command[0:5] == "10111":
        P = command[5:7] + command[12:16]
        R = command[7:12]
        P = int(P, base=2)
        R = int(R, base=2)
        return f"OUT {P} R{R}"

    if command[0:5] == "10110":
        P = command[5:7] + command[12:16]
        R = command[7:12]
        P = int(P, base=2)
        R = int(R, base=2)
        return f"IN {P} R{R}"

    if command[0:4] == "1101":
        d = command[4:]
        d = int(d, base=2)
        return f"RCALL {d}"

    if command[0:7] == "1001001" and command[12:16] == "0000":
        if len(command) != 16:
            return -1
        d = command[7:12]
        K = command[16:]
        return f"STS {int(K,base=2)} R{int(d, base=2)}"

    if command[0:7] == "1001000" and command[12:16] == "0000":
        if len(command) != 16:
            return -1
        d = command[7:12]
        K = command[16:]
        return f"LDS {int(K,base=2)} R{int(d, base=2)}"

    if command[0:7] == "1001001":
        r = command[7:12]
        r = int(r, base=2)
        tail = command[12:16]
        if tail == f'1100': return "ST X R{r}"
        if tail == f'1101': return "ST X+ R{r}"
        if tail == f'1110': return "ST -X R{r}"
        if tail == f'1001': return "ST Y+ R{r}"
        if tail == f'1010': return "ST -Y R{r}"
        if tail == f'0001': return "ST Z+ R{r}"
        if tail == f'0010': return "ST -Z R{r}"



    print(command)


