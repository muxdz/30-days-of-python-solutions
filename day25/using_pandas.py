import pandas as pd

data = pd.read_csv('day25/hacker_news.csv')

print(data.head())
print(data.tail())

print(data.columns)

print(data['title'])

print(data.shape)

python_titles = [title for title in data['title'] if 'python' in title.lower()]
print('Titles containing python:', python_titles)

javascript_titles = [title for title in data['title'] if 'javascript' in title.lower()]
print('Titles containing javascript:', javascript_titles)

'''
The data is about news on hacks and security breaches.
It gives the ID, title, urlm, number of comments and points.

In some cases gives the author and when it was created.
'''

