import gspread
import requests
import settings

from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.SECRETS_FILE, scope)
gc = gspread.authorize(credentials)

wks = gc.open_by_key(settings.DOCUMENT_KEY).sheet1


def fix_number_formatting(number):
    if number:
        number = str(number)
        if not number.startswith('+'):
            if not number.startswith('0'):
                return "0" + number

    return number


def fix_date_formatting(date_string):
    if date_string:
        date = datetime.strptime(date_string, "%d/%m/%Y")
        return date.strftime("%Y-%m-%d")

    return date_string


def process_data(data):
    try:
        response = requests.post(
            url=settings.SERVICE_WEBHOOK_URL,
            headers={
                'Content-Type': 'application/json',
                'api-key': settings.WEBHOOK_SECRET,
            },
            json={
                'first_name': data['First name'],
                'last_name': data['Last name'],
                'date_of_birth': fix_date_formatting(data['Date of birth']),
                'telephone': fix_number_formatting(data['Mobile number']),
                'email': data['Email address'],
                'address_no': data['No'],
                'address_street': data['Street'],
                'address_locality': data['Locality'],
                'address_city': data['City'],
                'address_postcode': data['Postcode'],
                'is_baptised': True if data['Are you baptised?'] == "Yes" else False,
                'baptismal_date': fix_date_formatting(data['Baptismal date']),
                'baptismal_place': data['Baptismal place'],
                'gdpr': True if data['Data policy'] else False,
            }
        )
        if response.status_code == 201:
            return True

    except requests.exceptions.ConnectionError:
        pass

    return False


def main():
    row = 2
    for record in wks.get_all_records():
        if not record['Processed timestamp']:
            if record['Data policy']:
                if process_data(record):
                    cell = "P" + str(row)
                    wks.update_acell(cell, str(datetime.now()))

        row += 1


if __name__ == "__main__":
    main()
