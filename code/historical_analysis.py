import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from astronomical_calculations import sun_position  # Import the sun_position function


def historical_peaks_and_drops():
    peaks = [
        ("2017-12-17", 19423.58),
        ("2019-06-26", 13880.00),
        ("2020-12-16", 28993.00),
        ("2021-04-14", 64895.00),
        ("2021-11-10", 69000.00),
        ("2024-03-14", 75830.00)  # Predicted peak for March 2024
    ]

    drops = [
        ("2018-12-17", 3232.00),
        ("2019-12-26", 7140.00),
        ("2021-07-16", 31522.00),
        ("2021-06-14", 40000.00),
        ("2021-12-10", 46211.00)
    ]

    return peaks, drops


def calculate_average_duration(peaks, drops):
    total_months = 0
    count = 0
    for i in range(len(drops)):
        peak_date = datetime.strptime(peaks[i][0], "%Y-%m-%d")
        drop_date = datetime.strptime(drops[i][0], "%Y-%m-%d")
        total_months += (drop_date.year - peak_date.year) * 12 + drop_date.month - peak_date.month
        count += 1
    return total_months / count if count > 0 else 0


def predict_next_drop(peak_date, avg_duration):
    next_drop_date = peak_date + timedelta(days=avg_duration * 30.44)
    return next_drop_date


def predict_next_peak(drop_date, avg_duration):
    next_peak_date = drop_date + timedelta(days=avg_duration * 30.44)
    return next_peak_date


def get_constellation(ecliptic_longitude):
    if 0 <= ecliptic_longitude < 30:
        return "Aries"
    elif 30 <= ecliptic_longitude < 60:
        return "Taurus"
    elif 60 <= ecliptic_longitude < 90:
        return "Gemini"
    elif 90 <= ecliptic_longitude < 120:
        return "Cancer"
    elif 120 <= ecliptic_longitude < 150:
        return "Leo"
    elif 150 <= ecliptic_longitude < 180:
        return "Virgo"
    elif 180 <= ecliptic_longitude < 210:
        return "Libra"
    elif 210 <= ecliptic_longitude < 240:
        return "Scorpio"
    elif 240 <= ecliptic_longitude < 270:
        return "Sagittarius"
    elif 270 <= ecliptic_longitude < 300:
        return "Capricorn"
    elif 300 <= ecliptic_longitude < 330:
        return "Aquarius"
    elif 330 <= ecliptic_longitude < 360:
        return "Pisces"
    return "Unknown"


def plot_predictions(peaks, drops, predicted_drop_date, next_peak_date):
    peak_dates = [datetime.strptime(date, "%Y-%m-%d") for date, _ in peaks]
    drop_dates = [datetime.strptime(date, "%Y-%m-%d") for date, _ in drops]

    peak_dates.append(next_peak_date)
    drop_dates.append(predicted_drop_date)

    peak_constellations = [get_constellation(sun_position(date)) for date in peak_dates]
    drop_constellations = [get_constellation(sun_position(date)) for date in drop_dates]

    data = pd.DataFrame({
        "Date": peak_dates + drop_dates,
        "Event": ["Peak"] * len(peak_dates) + ["Drop"] * len(drop_dates),
        "Constellation": peak_constellations + drop_constellations
    })

    data["Month"] = data["Date"].dt.strftime("%b")

    plt.figure(figsize=(10, 6))
    for label, df in data.groupby("Event"):
        plt.plot(df["Date"], df["Event"], marker="o", linestyle="-" if label == "Peak" else "--", label=label)
        for i, row in df.iterrows():
            plt.text(row["Date"], row["Event"], f'{row["Month"]}\n{row["Constellation"]}', ha='right')

    plt.xlabel("Date")
    plt.ylabel("Event")
    plt.title("Bitcoin Price Peaks and Drops with Constellations")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
