# This script accesses Reddit's API to collect text of posts from
# 'nopoo' and 'constipation' subreddits

from time import sleep
import pandas as pd
import requests


def fetch_subreddit(subreddit, pages=2):
    """Function to return text from all posts from a specified
    number of pages (default=150) for a subreddit.

    Parameters
    ----------
    subreddit : str
        Subreddit name (i.e. 'nopoo').
    pages : int
        Number of pages to scrape from a subreddit.

    Returns
    -------
    all_posts : list
        Description of returned object.
        For example,
            [
            {'subreddit': 'NoPoo',
            'selftext': 'Community recommended
            products [here](https://docs.google.com/document/d/1BaAzPnW
            7gyMDf9XrK0T9oP2cvsf0DmYFb7sQsUulJP8/edit#)',
            'name': 't3_butuoi'},
            {'subreddit': 'NoPoo',
            'selftext': 'I feel like I’m drumming on about this a lot lately,
             so I’m making a specific post.\n\n**Do not apply BS dry.**\n\n**
             Do not make a paste.**\n\n**Do not make a 50/50 mix with ACV.**\n
             \nDoing those things **WILL** damage your hair.',
             'name': 't3_c2ykn0'},
             ...]
    """
    all_posts = []
    after = ''
    for i in range(pages):
        # try:
        print(f'Fetching Page {i + 1}')  # progress print
        page = fetch_page(subreddit, after)
        parsed_posts, after = parse_page(page)
        all_posts.extend(parsed_posts)
        sleep(5)
        # except:
        #     print("An exception occurred")
    return all_posts


def fetch_page(subreddit, after=''):
    """Function to return json of each page."""
    URL = f'https://www.reddit.com/r/{subreddit}.json'
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    r = requests.get(URL, headers=headers, params=params)
    return r.json()['data']['children']


def parse_page(page):
    """Function that calls parse_post() for each page."""
    parsed_posts = []
    after = ''
    for post in page:
        p = parse_post(post)
        after = p['name']
        parsed_posts.append(p)
    return parsed_posts, after


def parse_post(post):
    """Function to get the text attached to the 'subreddit',
    'selftext', and 'name' tags of each post."""
    keep = ['subreddit', 'selftext', 'name']
    data = post['data']
    return {k: v for k, v in data.items() if k in keep}


if __name__ == "__main__":

    # list with all posts for NoPoo
    nopoo_posts = fetch_subreddit('nopoo')

    # list with all posts for Constipation
    constipation_posts = fetch_subreddit('constipation')

    # converting lists to pandas dataframes, and concatenating them together
    nopoo = pd.DataFrame(nopoo_posts)
    constipation = pd.DataFrame(constipation_posts)
    df = pd.concat([constipation, nopoo]).reset_index(drop=True)

    # saving results to csv (in case something goes wrong)
    df.to_csv('data.csv')
