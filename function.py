import os
import pandas as pd
from datetime import datetime
from functools import wraps

def loger(func):
    def wrapper(*args, **kwargs):
        log_file = 'logs.csv'
        exists = os.path.isfile(log_file) and os.path.getsize(log_file) > 0
        current_id = len(pd.read_csv(log_file, sep=';')) if exists else 0

        now = datetime.now()
        row = {
            'pc_username': os.getlogin(),
            'function_name': func.__name__,
            'Date': now.strftime('%d.%m.%Y'),
            'Time': now.strftime('%H:%M:%S'),
        }

        pd.DataFrame([row], index=[current_id]).to_csv(
            log_file, mode='a', index_label='id',
            header=not exists, sep=';', encoding='UTF-8',
        )

        return func(*args, **kwargs)

    return wrapper
