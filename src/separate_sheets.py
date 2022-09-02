"""separate sheets.py"""

import os
import pandas as pd
from configs.configs import configs as cfg

SHEETS = cfg['sheets_names']

for ind, name in enumerate(SHEETS):

    df = pd.read_excel(cfg['data_path'] + cfg['raw_data_name'], sheet_name=name, header=1)
    df.reset_index(drop=True, inplace=True)

    # if path not exist, create it
    if not os.path.exists(cfg['clean_data_path_init']):
        os.makedirs(cfg['clean_data_path_init'])

    # save to csv in path
    df.to_csv(cfg['clean_data_path_init']+'/'+name+'.csv', index=False)
    print('{}/{}'.format(ind+1, len(SHEETS)))
    print('{} saved to {}'.format(name, cfg['clean_data_path_init']))
