from decouple import config
from gspread import Client, Spreadsheet, service_account


GOOGLE_ACCOUNT_JSON = config('GOOGLE_ACCOUNT_JSON')
GOOGLE_TABLE_ID = config('GOOGLE_TABLE_ID')


def client_init_json() -> Client:
    return service_account(GOOGLE_ACCOUNT_JSON)


def get_table_by_id(client: Client, table_id):
    return client.open_by_key(table_id)


def get_worksheet_info(table: Spreadsheet) -> dict:
    worksheets = table.worksheets()
    return {
        'count': len(worksheets),
        'names': [worksheet.title for worksheet in worksheets]
    }


def test_gsheets_connection():
    client = client_init_json()
    table = get_table_by_id(client, GOOGLE_TABLE_ID)
    info = get_worksheet_info(table)
    reply_message = (
        f'Connected to Google Sheet with {info['count']} sheets in total.\n'
        f'Sheet names are:\n')
    for name in info['names']:
        reply_message += f'{name}\n'
    return reply_message
