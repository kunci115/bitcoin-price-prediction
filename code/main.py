from datetime import datetime
from astronomical_calculations import sun_position, moon_position
from historical_analysis import historical_peaks_and_drops, calculate_average_duration

def main():
    peaks, drops = historical_peaks_and_drops()
    avg_duration = calculate_average_duration(peaks, drops)
    print(f"Average duration between peaks and drops: {avg_duration} months")

    next_peak_date = datetime.strptime("2025-11-25", "%Y-%m-%d")
    next_drop_date = datetime.strptime("2026-05-25", "%Y-%m-%d")

    sun_lambda_peak = sun_position(next_peak_date)
    moon_lambda_peak = moon_position(next_peak_date)
    sun_lambda_drop = sun_position(next_drop_date)
    moon_lambda_drop = moon_position(next_drop_date)

    print(f"Next Peak Date: {next_peak_date.strftime('%Y-%m-%d')}")
    print(f"Sun Position: {sun_lambda_peak}°")
    print(f"Moon Position: {moon_lambda_peak}°")

    print(f"Next Drop Date: {next_drop_date.strftime('%Y-%m-%d')}")
    print(f"Sun Position: {sun_lambda_drop}°")
    print(f"Moon Position: {moon_lambda_drop}°")

if __name__ == "__main__":
    main()
