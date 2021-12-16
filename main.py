from Token import Token

Tokens = []
keywords = ['int', 'char', 'printf', 'scanf']


def add_token(Type, literal, col, row, blockno):
    Tokens.append(Token(Type, literal, row, col, blockno))


code = open("hello.c", mode='r').read()

col = 0
row = 0
block_no = 0
index = -1

while index < len(code)-1:
    index += 1
    current_char = code[index]
    if current_char.isspace():
        match current_char:
            case '\t':
                col += 4
            case ' ':
                col += 1
            case '\n':
                col = 0
                row += 1
        continue

    match current_char:
        case '+':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col, row, block_no)

            elif code[index + 1] == '+':
                col += 2
                add_token('operator', code[index:index + 2], col, row, block_no)

            else:
                col += 1
                add_token('operator', code[index], col, row, block_no)

        case '{':
            col += 1
            block_no += 1
            add_token('operator', code[index], col, row, block_no)

        case '}':
            col += 1
            block_no -= 1
            add_token('operator', code[index], col, row, block_no)

        case '#':
            continue

        case '(':
            col += 1
            add_token('operator', code[index], col, row, block_no)

        case ')':
            col += 1
            add_token('operator', code[index], col, row, block_no)

        case ';':
            col += 1
            add_token('semi-colon', code[index], col, row, block_no)

        case '=':
            if code[index + 1] == '=':
                col += 2
                add_token('boolean operator', code[index], col, row, block_no)
            else:
                col += 1
                add_token('operator', code[index], col, row, block_no)

        case current_char if current_char.isnumeric():
            c_index = index
            while code[index].isnumeric():
                index += 1
                col += 1
            add_token('number', code[c_index:index], col, row, block_no)
            index -= 1

        case '"':
            c_index = index
            index += 1
            col += 1
            while code[index] != '"':
                index += 1
                col += 1
            add_token('string', code[c_index:index + 1], col, row, block_no)

        case ',':
            col += 1
            add_token('comma', code[index], col, row, block_no)

        case '&':
            if code[index + 1] == '=':
                col += 2
                add_token('operator', code[index:index + 2], col, row, block_no)

            elif code[index + 1] == '&':
                col += 2
                add_token('boolean operator', code[index:index + 2], col, row, block_no)

            else:
                col += 1
                add_token('ampersand', code[index], col, row, block_no)

        case _:
            c_index = index
            while code[index].isalnum():
                index += 1
                col += 1

            if code[c_index:index] in keywords:
                add_token('keyword', code[c_index:index], col, row, block_no)
            else:
                add_token('identifier', code[c_index:index], col, row, block_no)
            index -= 1

print("hi")
