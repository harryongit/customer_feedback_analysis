# main.py
from src.data_processor import DataProcessor
from src.analyzer import FeedbackAnalyzer
from src.visualizer import FeedbackVisualizer

def main():
    # Initialize components
    processor = DataProcessor('data/sample_feedback.csv')
    analyzer = FeedbackAnalyzer()
    visualizer = FeedbackVisualizer()
    
    # Process data
    df = processor.load_data()
    df = processor.clean_data(df)
    df = processor.categorize_feedback(df)
    
    # Analyze data
    summary_stats = analyzer.get_summary_stats(df)
    print("Summary Statistics:", summary_stats)
    
    # Visualize results
    visualizer.plot_sentiment_distribution(df)
    visualizer.plot_category_trends(df)

if __name__ == "__main__":
    main()
