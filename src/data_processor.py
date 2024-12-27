# src/data_processor.py
import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load_data(self):
        return pd.read_csv(self.file_path)
    
    def clean_data(self, df):
        df = df.dropna()
        df['date'] = pd.to_datetime(df['date'])
        df['sentiment'] = df['sentiment'].str.lower()
        return df
    
    def categorize_feedback(self, df):
        df['category'] = df['feedback'].apply(self._categorize_text)
        return df
    
    def _categorize_text(self, text):
        categories = {
            'service': ['service', 'staff', 'employee', 'assistance'],
            'product': ['product', 'quality', 'feature', 'broken'],
            'pricing': ['price', 'cost', 'expensive', 'cheap'],
            'other': []
        }
        
        text = text.lower()
        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                return category
        return 'other'
