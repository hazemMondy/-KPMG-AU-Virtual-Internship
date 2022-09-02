"""configs.py"""

DATA_PATH = '../data/raw'
RAW_DATA_NAME = '/KPMG_VI_New_raw_data_update_final.xlsx'
CLEAN_DATA_PATH_INIT = '../data/clean/init'
CLEAN_DATA_PATH_FINAL = '../data/clean/final'
SHEETS_NAMES = ['Transactions', 'NewCustomerList', 'CustomerDemographic', 'CustomerAddress']

configs = {
    'data_path': DATA_PATH,
    'clean_data_path_init': CLEAN_DATA_PATH_INIT,
    'sheets_names': SHEETS_NAMES,
    'clean_data_path_final': CLEAN_DATA_PATH_FINAL,
    'raw_data_name': RAW_DATA_NAME
}
