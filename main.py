def main(program):
    # Commands
    # > = increment dp
    # < = decrement dp
    # + = increment byte at dp
    # - = decrement byte at dp
    # . = output byte at dp
    # [ = if byte at dp is zero, then instead of moving the instruction pointer forward to the next command, jump it
    # forward to the command after the matching ] command.
    # ] = see [
    ip = 0
    dp = 0
    data = [0] * 30000

    while True:
        c = program[ip]

        if c == ">":
            dp += 1
        elif c == "<":
            dp -= 1
        elif c == "+":
            data[dp] = (data[dp] + 1) % 256
        elif c == "-":
            data[dp] = (data[dp] - 1) % 256
        elif c == ".":
            print(data[dp], end="")
        elif c == "[" and data[dp] == 0:
            ip2 = ip + 1
            bracket_balance = 0

            while True:
                c2 = program[ip2]
                
                if c2 == "[":
                    bracket_balance += 1
                elif c2 == "]" and bracket_balance == 0:
                    break
                elif c2 == "]":
                    bracket_balance -= 1

                ip2 += 1

            ip = ip2 + 1

            if ip == len(program):
                break

            continue
        elif c == "]" and data[dp] != 0:
            ip2 = ip - 1

            while True:
                c2 = program[ip2]

                if c2 == "[":
                    break

                ip2 -= 1

            ip = ip2 + 1
            continue

        ip += 1

        if ip == len(program):
            break


if __name__ == '__main__':
    program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    main(program)

