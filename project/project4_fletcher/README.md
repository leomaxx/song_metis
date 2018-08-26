
## Social Media Customer Service Assistant

### Backgound:
According to Twitter, customer service interactions on Twitter increased by 250% in 2017 compared with 2015. For customers, social media is a place where they get instant response; For brands, it is a great upper-funnel marketing channel. With more and more customer service requests, it is difficult for the customer service agent to respond in a timely manner. Most companies also face the challenge of not having social media conversations integrated with their customer care ticketing system and knowledge base.

### Problem definition:
Build a tool that assists Social Media Customer Service agent with 2 features:
  1. Suggest reply to customer enqueries
  2. Categorize customer enqueries (to get ready to be imported to corresponding category in knowldge base)

### Dataset:
https://www.kaggle.com/thoughtvector/customer-support-on-twitter
2.8 Million tweets between customers and customer service agents from different brands

### Implementation
**Stage 1 - Data preprocessing ** <b>
1. Extract the emoji's from tweets, and put emoji's and text into two separate columns
2. Preprocess the text including 
    * convert all text to lower case
    * remove newline characters
    * remove hyperlinks and @accountnames
    * fix contractions - he's -> he is
    * convert the dates into proper timestamps
3. Remove the non-English tweets
 
 **Stage 2 - Sentiment analysis on tweets**<b>
 Purpose of this stage is to analyze the sentiment of customer's last tweet in a conversation. As we would like to only recommend replys (solutions) from resolved conversations, we would like to leverage sentiment analysis to classify conversations that ended with good note as resolved.
 1. http://kt.ijs.si/data/Emoji_sentiment_ranking/ is used to score the sentiment of emoji's in the tweets
 2. User NTLK Vader sentimentanalyzer to score the text sentiment
 
 ** Stage 3 - Reconstruct conversations **<b>
 Group the tweets into conversations
 1. Merge the tweets into conversations with tweet id, tweet in response to, and responding tweets fields
 2. Tweets with time difference longer than 2 days are sparated into different conversations. This is a simple logic to identify different cases opened by same customer
 3. Identify customer id and brand service agent id for each conversation
 4. Remove conversations that contains only tweets from customer or tweets from customer service agents
    
 ** Stage 4 - Build recommendation engines **
 Idea behind the recommendation engine is simple - the assistant tool analyzes each new tweet and identifies the most similar tweets that are already resolved, and displays the corresponding history replies.
 1. Tokenize and lemanize the tweets
 2. Vectorize the tweets with different options:
    * TD-IDF
    * Count Vectorizer
 3. Reduce vectorized data to topics with different options: 
    * NMF
    * TruncatedSVD
 4. Alternatively, replace step 2 and 3 with Google Word2Vec.
 5. Leverage Nearest neighbor to fine the most similar tweet
 6. Experiment with the above options and examine the quality of recommendations manually.
 The final best model is Count Vectorizer + NMF + 10 Topics.
 
  ** Stage 5 - Clustering **
 To categorize the customer requests into subgroups, in anticipation of future import to companys' knowledge base.
 Experiment with different options in the clustering pipeline:
 1. Vectorizes:
    * TD-IDF
    * Count Vectorizer
 2. Reducers:
    * NMF
    * TruncatedSVD
 3. Number of topics:
    * 10 - 100
 4. Number of clusters:
    * 5, 10, 15
 Project each clustering result onto the TSNE space to observe how separate the clusters in order to narrow down the best models. Then for each model, extract 10 tweets that are close to cluster centers and observe if they share a common theme.
 
 The final bext model is Count Vectorizer + NMF + 10 Topics + 15 clusters.
 
For more details about the project and observations/comments, refer to the following link:
https://docs.google.com/presentation/d/1sc8qJ-w9D5gyLAwQheMrc89yxbzo0SaOgKK-f7PeCXU/edit?usp=sharing

