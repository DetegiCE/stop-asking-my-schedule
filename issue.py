import os
from github import Github
from datetime import datetime
import pytz

token = os.environ['MY_GITHUB_TOKEN']
git = Github(token)
repo = git.get_user().get_repo('stop-asking-my-schedule')

dt_utc = datetime.now(tz=pytz.UTC)
dt_kst = dt_utc.astimezone(pytz.timezone('Asia/Seoul'))
dt_str = dt_kst.strftime('%Y%m%d')

weektitle = f'WEEK{dt_str}'
repo.create_issue(title=weektitle, body='')
