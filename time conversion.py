def timeConversion(s):
    am_pm = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]

    if am_pm == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}{rest}"