def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

convert_number(123)
convert_number('ins')
