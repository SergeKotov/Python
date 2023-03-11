import requests
from datetime import datetime, timedelta
import time

class StackOverflowQuest:

    def __init__(self):
        self.stackover_url = 'https://api.stackexchange.com/2.3/questions'

    def get_questions(self, tag, days):
        date_from = datetime.today() - timedelta(days=days)
        timestamp = int(datetime.timestamp(date_from))
        params = {
             'fromdate': str(timestamp),
             'order': 'desc',
             'sort': 'activity',
             'tagged': tag,
             'site': 'stackoverflow'
        }
        url = 'https://api.stackexchange.com/2.3/questions'
        response = requests.get(url=url, params=params)
        return response.json()


if __name__ == '__main__':
    # set data for a request to the stack exchange 
    tag = 'python'
    last_days = 2

    print("\nGet questions from stackoverflow")
    print(f'By tag: {tag}')
    print(f'Number of previous days: {last_days}')    

    # get questions
    stackover = StackOverflowQuest()
    json_data = stackover.get_questions(tag=tag, days=last_days)
    items_list = json_data["items"]
    print(f'\nNumber of questions founded: {len(items_list)}')
    print('Question titles:')
    for item in items_list:
	    print(item["title"])
    