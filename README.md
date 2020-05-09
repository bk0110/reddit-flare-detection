# Reddit-flare-detection
A web app for detecting reddit post's flair through link as input.
## Requirements:
* pandas
* numpy
* scikit
* gensim
* nltk
* seaborn

## Experiment log:

### Part I - Reddit Data Collection
* Web Scraping from r/india using Reddit API for Python PRAW and pandas library.
https://praw.readthedocs.io/en/latest/
* Got Reddit API access by authenticating via OAuth to generate client id,client secret and user agent.
* Scraping top 500 posts of 11 categories from reddit India.
* Scraping their title, description, id, url, author, and flair and stored in a .csv format. 

### Part II - Exploratory Data Analysis (EDA) 
* Read the scraped data by using pandas library. There was a bias in the no. of posts scraped so to keep the no. of posts in a range, I had then removed certain categories from the data. ( total 6 categories at last). 
* Text normalizing: Used re, inflection, nltk-natural language toolkit, beautiful soup and pandas library
  * Replaced null values: using fillna() which replaces the cells having nan values with a particular text which is “missing” in my case. This was done because only the description and flair columns had nan values, and I didn’t want to lose data from the posts which had only a title. Then the posts having the flair column as missing were removed. 
  * Resetting index of the dataframe- as removing certain posts categories which were less in number and removing missing flair category results in losing some indices making the data discontinuous so resetting them to make consistent.
  * Removed links and html tags- using re
  * Tokenized sentences to words- using nltk
  * Removed punctuation marks, numbers, stopwords- using nltk,re
  * Converted everything into lower case. -using re
  * Performed lemmatization of the words- using nltk
  * Did the text normalization on title and description one by one using df.loc[][] and accessing each cell and changing it with normalized text.	
  * For all the different types of flair word clouds were generated which show the most similar words to the flair name as per frequency.
  
### Part III - Building a Flare Detector
* Trained the model using word2vec as it takes the relation between words in a sentence into account.
* Split the dataset- test:train=30:70 using test_train_split
* Applied 3 algorithms: Naive Bayes, SGD Classifier, Logistic Regression
* Logistic Regression gave best results every time (both datasets one having all the flairs and the second from which some flairs were removed based on certain threshold) with around 72% accuracy

## To Do:
### Part IV - Building a Web Application
* Used node.js to make the app and then deployed on heroku

Complete Experiment log and Refernces: https://docs.google.com/document/d/1XcaFrAADsaAijsA2_7WAsSvhMZmxq-6zHvvLOh5f7Is/edit?usp=sharing
