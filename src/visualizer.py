# src/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

class FeedbackVisualizer:
    def plot_sentiment_distribution(self, df):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='sentiment')
        plt.title('Sentiment Distribution')
        plt.savefig('sentiment_distribution.png')
        plt.close()
    
    def plot_category_trends(self, df):
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, x='category', hue='sentiment')
        plt.title('Category Distribution by Sentiment')
        plt.xticks(rotation=45)
        plt.savefig('category_trends.png')
        plt.close()
