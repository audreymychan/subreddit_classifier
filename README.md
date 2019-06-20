# subreddit_classifier
> r/NoPoo vs r/Constipation classifier using NLP and Reddit's API

## Executive Summary
In this project, Reddit's API and Natural Language Processing (NLP) are used to:

1. Collect posts from two subreddits

   - Posts were collected from the subreddits by accessing Reddit's API.
   - *See **`reddit_scraper.py`***

2. Pre-process text (tokenization, normalization, clean up)

   |             Technique |                                   Function/Module |
   | --------------------: | ------------------------------------------------: |
   |           Remove HTML |                                   `BeautifulSoup` |
   | Convert to lower case |                           Python string `lower()` |
   |            Tokenizing |                            `nltk.tokenize.regexp` |
   |         Lemmatization |             `nltk.stem.wordnet.WordNetLemmatizer` |
   |   Removing stop words |                    `stopwords` from `nltk.corpus` |
   |           Vectorizing | `sklearn.feature_extraction.text.TfidfVectorizer` |

3. Train a classifer

   - Different classification models were tried to determine the best model.
     - Logistic Regression
     - Nearest Neighbors
     - Naive Bayes
     - Linear SVM
     - Random Forest
   - The best model was found to be Random Forest with a score of: **100%**!

4. Using the best model, predict which subreddit a new post belongs to!

*See **`subreddit_post_classifier.ipynb`** for code and examples of new posts to predict.*

### Subreddits
Here are the two subreddits that were compared. How do you think posts would differ between each subreddit?
1. [r/NoPoo](https://www.reddit.com/r/nopoo)<br>
👨‍🦱 "No Shampoo" A place to discuss natural hair care and alternatives to shampoo.
2. [r/Constipation](https://www.reddit.com/r/constipation)<br>
🚫💩 A place for people with constipation issues, where all questions related with the condition can be debated.
