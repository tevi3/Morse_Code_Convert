from morse_code_dict import MORSE_CODE


def encrypt(message):

    encrypted_msg = ''

    for word in message.upper():
        if word == ' ':
            encrypted_msg += ' '
        else:
            encrypted_msg += MORSE_CODE[word] + ' '

    return encrypted_msg


def decrypt(morse_code):

    decrpyted_code = ''

    for code in morse_code.split(' '):
        if code == '':
            decrpyted_code += ' '
        else:
            code_index = list(MORSE_CODE.values()).index(code)
            decrpyted_code += list(MORSE_CODE.keys())[code_index]

    return decrpyted_code



