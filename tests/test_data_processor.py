# tests/test_data_processor.py
import pytest
from src.data_processor import DataProcessor
import pandas as pd

def test_categorize_text():
    processor = DataProcessor('')
    assert processor._categorize_text('The service was great') == 'service'
    assert processor._categorize_text('Product is broken') == 'product'
    assert processor._categorize_text('Too expensive') == 'pricing'
