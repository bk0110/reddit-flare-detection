{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import praw\n",
    "import pandas as pd\n",
    "\n",
    "#Creating a read-only Reddit instance\n",
    "reddit=praw.Reddit(client_id='8ibbu5urH2vjeg', client_secret='iNKYMa_WeYvW6l479sbP5LNEfbM', user_agent='WS_latest_0110')\n",
    "\n",
    "#Getting subreddit reddit India\n",
    "subreddit=reddit.subreddit('india')\n",
    "\n",
    "#Scraping top 1000 hot posts from reddit India\n",
    "hot_posts=subreddit.hot(limit=1000)\n",
    "\n",
    "all_hot_posts=[]\n",
    "\n",
    "for submission in hot_posts:\n",
    "    post={\n",
    "        \"title\": submission.title,\n",
    "        \"description\": submission.selftext,\n",
    "        \"id\": submission.id,\n",
    "        \"author\": submission.author,\n",
    "        \"flair\": submission.link_flair_text\n",
    "    }\n",
    "    all_hot_posts.append(post)\n",
    "    \n",
    "#storing the information in a .csv format\n",
    "all_hot_posts = pd.DataFrame(all_hot_posts,columns=['title', 'description', 'id', 'author','flair'])\n",
    "all_hot_posts.to_csv('rIndia_scrapedData.csv', index=False) \n",
    "#print(all_hot_posts)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
