from datetime import datetime

def historical_peaks_and_drops():
    peaks = [
        ("2017-12-17", 19423.58),
        ("2019-06-26", 13880.00),
        ("2020-12-16", 28993.00),
        ("2021-04-14", 64895.00),
        ("2021-11-10", 69000.00)
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
    for i in range(len(peaks)):
        peak_date = datetime.strptime(peaks[i][0], "%Y-%m-%d")
        drop_date = datetime.strptime(drops[i][0], "%Y-%m-%d")
        total_months += (drop_date.year - peak_date.year) * 12 + drop_date.month - peak_date.month
    return total_months / len(peaks)
