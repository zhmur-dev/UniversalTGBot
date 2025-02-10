from gspread import Client, Spreadsheet, service_account

from config_data.config import settings


def client_init_json() -> Client:
    return service_account(settings.GOOGLE_ACCOUNT_JSON)


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
    table = get_table_by_id(client, settings.GOOGLE_TABLE_ID)
    info = get_worksheet_info(table)
    reply_message = (
        f'Connected to Google Sheet with {info['count']} sheets in total.\n'
        f'Sheet names are:\n')
    for name in info['names']:
        reply_message += f'{name}\n'
    return reply_message
