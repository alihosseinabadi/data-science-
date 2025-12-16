num_of_steps = 12
forecast_steps = 3
report_template = """We made {observations} observations by tossing a coin: {tails} were tails and {heads} were heads. The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively. Our forecast is that the next {forecast_steps} observations will be: {forecast_tails} tail(s) and {forecast_heads} head(s)."""