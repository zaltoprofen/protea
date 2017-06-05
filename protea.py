import requests
import json
import os
import subprocess
import sys


def main():
    token = os.getenv('SLACK_TOKEN')
    os.chdir(os.path.dirname(os.path.abspath(__name__)))
    p = subprocess.run(['osascript', 'get_playing.scpt'], stdout=subprocess.PIPE)
    status = p.stdout.decode('utf-8')[:-1]
    if status == '' or token is None:
        return
    profile = {
        'status_emoji': ':headphones:',
        'status_text': status,
    }
    payload = {
        'token': token,
        'profile': json.dumps(profile),
    }
    return requests.post('https://slack.com/api/users.profile.set', params=payload).json()['ok']


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
