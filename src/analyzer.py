# src/analyzer.py
class FeedbackAnalyzer:
    def calculate_sentiment_distribution(self, df):
        return df['sentiment'].value_counts()
    
    def calculate_category_distribution(self, df):
        return df['category'].value_counts()
    
    def get_monthly_trends(self, df):
        return df.groupby(df['date'].dt.to_period('M'))['sentiment'].value_counts()
    
    def get_summary_stats(self, df):
        return {
            'total_feedback': len(df),
            'sentiment_distribution': self.calculate_sentiment_distribution(df),
            'category_distribution': self.calculate_category_distribution(df)
        }
