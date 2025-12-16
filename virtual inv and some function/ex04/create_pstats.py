# create_pstats.py
import cProfile
import pstats
import sys
from financial_enhanced import get_financial_data

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Call the function we want to profile
    try:
        result = get_financial_data('MSFT', 'Total Revenue')
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    profiler.disable()
    return profiler

if __name__ == '__main__':
    profiler = profile_function()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    
    with open('pstats-cumulative.txt', 'w') as f:
        stats.stream = f
        stats.print_stats(5)  # Top 5 functions by cumulative time