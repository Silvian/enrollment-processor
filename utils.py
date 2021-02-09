from datetime import datetime


def fix_number_formatting(number):
    if number:
        number = str(number)
        number = number.strip().replace(" ", "")
        if not number.startswith('+'):
            if not number.startswith('0'):
                return "0" + number
        else:
            if number.find("0") == 3:
                return number[:3] + number[4:]

    return number


def fix_date_formatting(date_string):
    if date_string:
        date = datetime.strptime(date_string, "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")

    return date_string
