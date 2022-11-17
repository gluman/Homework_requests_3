from pprint import pprint as pp
import requests as rq
import datetime as d
import pandas as pd


class Stackoverflow:
    '''
    class for website stackoverflow.com
    '''

    base_host = 'https://api.stackexchange.com/'

    # def __init__(self, key):
    #     self.key = key

    # def get_headers(self):
    #     return {
    #         'Content-Type': 'applocation/json',
    #         'Authorization': f'OAuth {self.key}'
    #     }

    def get_questions_limit(self, diff_days):
        uri = '2.3/questions'
        today = d.datetime.now().timestamp()  # now date
        delta_days = d.timedelta(days=diff_days).total_seconds()  # diff 2 days in mil sec
        date_eirler = str(int(round(today - delta_days, 0)))

        print(date_eirler)
        url = self.base_host + uri
        params = {'order': 'asc',
                  'min': date_eirler,
                  'sort': 'creation',
                  'site': 'stackoverflow',
                  'filter': '!Oev7Wy_R1VbJ_Uiy-DLg_H7(uGMFWHCMUHTbs(7dTS6'
                  }
        res = rq.get(url, params=params)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pp(pd.DataFrame(res.json()['items']))
        # pp(res.json())


if __name__ == '__main__':
    questions = Stackoverflow()
    questions.get_questions_limit(2)
