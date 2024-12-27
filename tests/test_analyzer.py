# tests/test_analyzer.py
import pytest
from src.analyzer import FeedbackAnalyzer
import pandas as pd

def test_calculate_sentiment_distribution():
    analyzer = FeedbackAnalyzer()
    df = pd.DataFrame({'sentiment': ['positive', 'negative', 'positive']})
    distribution = analyzer.calculate_sentiment_distribution(df)
    assert distribution['positive'] == 2
    assert distribution['negative'] == 1
