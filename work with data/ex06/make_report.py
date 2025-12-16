import sys
import os
from analytics import Research, Analytics
import config
import logging

def generate_report(file_path):
    research = Research(file_path)
    success = False
    
    try:
        # Read and process data
        data = research.file_reader()
        
        # Pass data to Analytics constructor
        analytics = Analytics(data)
        heads, tails = analytics.counts()
        head_perc, tail_perc = analytics.fractions(heads, tails)
        
        # Generate predictions
        predictions = analytics.predict_random(config.NUM_OF_STEPS)
        
        # Count prediction summary
        pred_heads = sum(1 for p in predictions if p == [0, 1])
        pred_tails = sum(1 for p in predictions if p == [1, 0])
        
        # Format prediction summary
        tail_word = "tail" if pred_tails == 1 else "tails"
        head_word = "head" if pred_heads == 1 else "heads"
        prediction_summary = f"{pred_tails} {tail_word} and {pred_heads} {head_word}"
        
        # Generate report text
        report_text = config.REPORT_TEMPLATE.format(
            total_observations=len(data),
            tails_count=tails,
            heads_count=heads,
            tail_percentage=tail_perc,
            head_percentage=head_perc,
            num_predictions=config.NUM_OF_STEPS,
            prediction_summary=prediction_summary
        )
        
        # Save report
        analytics.save_file(report_text, "report", "txt")
        print("Report generated successfully!")
        print("\nReport content:")
        print("=" * 50)
        print(report_text)
        print("=" * 50)
        
        success = True
        return True
        
    except Exception as e:
        logging.error(f"Report generation failed: {e}")
        print(f"Error generating report: {e}")
        return False
        
    finally:
        # Send Telegram notification (will skip if not configured)
        research.send_telegram_message(success)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py <file_path>")
        sys.exit(1)
    
    generate_report(sys.argv[1])

if __name__ == '__main__':
    main()