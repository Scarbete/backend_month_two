
text = 'lol'


def is_palindrom(output_text: str):
    return output_text == output_text[::-1]


print(is_palindrom(text))