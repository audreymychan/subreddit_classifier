import datetime
from time import sleep
import pandas as pd
import requests

# function to return json of each page
def fetch_page(subreddit, after=''):
    URL = f'https://www.reddit.com/r/{subreddit}.json'
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    r = requests.get(URL, headers=headers, params=params)
    return r.json()['data']['children']

# function that calls parse_post() for each page
def parse_page(page):
    parsed_posts = []
    after = ''
    for post in page:
        p = parse_post(post)
        after = p['name']
        parsed_posts.append(p)
    return parsed_posts, after

# function to get the text attached to the 'subreddit', 'selftext', 'name' tags of each post
def parse_post(post):
    keep = ['subreddit', 'selftext', 'name']
    data = post['data']
    return {k: v for k, v in data.items() if k in keep}

# function to return text from all posts from 150 pages for a subreddit, this will take some time
def fetch_subreddit(subreddit, pages = 150):
    all_posts = []
    after = ''
    for i in range(pages):
        # try:
        print(f'Fetching Page {i + 1}')
        page = fetch_page(subreddit, after)
        parsed_posts, after = parse_page(page)
        all_posts.extend(parsed_posts)
        sleep(5)
        # except:
        #     print("An exception occurred")
    return all_posts

if __name__ == "__main__":

    # list with all posts for NoPoo
    nopoo_posts = fetch_subreddit('nopoo')

    # list with all posts for Constipation
    constipation_posts = fetch_subreddit('constipation')

    # converting lists to pandas dataframes, and concatenating them together
    nopoo = pd.DataFrame(nopoo_posts)
    constipation = pd.DataFrame(constipation_posts)
    df = pd.concat([constipation, nopoo]).reset_index(drop = True)

    # saving results to csv (in case something goes wrong)
    df.to_csv('data.csv')
