import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')
nltk.download('punkt')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def classify_sentiment(review):
    score = sia.polarity_scores(review)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def read_reviews(file_path):
    with open(file_path, 'r') as file:
        reviews = file.readlines()
    return reviews

def classify_reviews(file_path):
    reviews = read_reviews(file_path)
    categorized_reviews = {'Positive': [], 'Negative': [], 'Neutral': []}

    for review in reviews:
        sentiment = classify_sentiment(review)
        categorized_reviews[sentiment].append(review.strip())

    return categorized_reviews

def summarize_reviews(reviews):
    # Join all reviews into one large paragraph for each sentiment
    full_review_content = " ".join(reviews)
    return full_review_content

# Save the full reviews into separate files
def save_summarized_reviews(categorized_reviews):
    for sentiment, reviews in categorized_reviews.items():
        if reviews:  # Check if there are any reviews in this category
            full_review_content = summarize_reviews(reviews)
            file_name = f"{sentiment.lower()}_reviews.txt"
            with open(file_name, 'w') as file:
                file.write(full_review_content)
            print(f"Full {sentiment} reviews saved to {file_name}")

def plot_sentiment_counts(categorized_reviews):
    sentiment_counts = {k: len(v) for k, v in categorized_reviews.items()}
    categories = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())

    print("\nSentiment Counts:")
    for category, count in sentiment_counts.items():
        print(f"{category}: {count}")

    # sentiment counts as a bar graph
    plt.bar(categories, counts, color=['teal', 'red', 'blue'])
    plt.title('Sentiment Analysis of product Reviews')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

file_path = '/content/drive/MyDrive/DS_foundation/assignment_7/product_review.txt'
categorized_reviews = classify_reviews(file_path)

save_summarized_reviews(categorized_reviews)

plot_sentiment_counts(categorized_reviews)
