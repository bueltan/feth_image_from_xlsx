# -*- coding: utf-8 -*-

import pandas as pd

def load_data_frame(file_path:str = 'iNSPIRE tables.xlsx', sheet_name:str= 'Standards'  ) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df