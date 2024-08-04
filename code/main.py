from datetime import datetime
from astronomical_calculations import sun_position, moon_position
from historical_analysis import historical_peaks_and_drops, calculate_average_duration, predict_next_drop, \
    predict_next_peak, plot_predictions


def main():
    peaks, drops = historical_peaks_and_drops()
    avg_duration = calculate_average_duration(peaks, drops)
    print(f"Average duration between peaks and drops: {avg_duration} months")

    # Predict the next drop after the March 2024 peak
    march_2024_peak_date = datetime.strptime("2024-03-14", "%Y-%m-%d")
    predicted_drop_date = predict_next_drop(march_2024_peak_date, avg_duration)
    sun_lambda_predicted_drop = sun_position(predicted_drop_date)
    moon_lambda_predicted_drop = moon_position(predicted_drop_date)

    print(f"Predicted Drop Date: {predicted_drop_date.strftime('%Y-%m-%d')}")
    print(f"Sun Position: {sun_lambda_predicted_drop}°")
    print(f"Moon Position: {moon_lambda_predicted_drop}°")

    # Predict the next peak after the predicted drop
    next_peak_date = predict_next_peak(predicted_drop_date, avg_duration)
    sun_lambda_next_peak = sun_position(next_peak_date)
    moon_lambda_next_peak = moon_position(next_peak_date)

    print(f"Next Peak Date: {next_peak_date.strftime('%Y-%m-%d')}")
    print(f"Sun Position: {sun_lambda_next_peak}°")
    print(f"Moon Position: {moon_lambda_next_peak}°")

    # Plot the predictions
    plot_predictions(peaks, drops, predicted_drop_date, next_peak_date)


if __name__ == "__main__":
    main()
