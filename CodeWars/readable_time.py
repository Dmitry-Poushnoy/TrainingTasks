# Write a function, which takes a non-negative integer (seconds)
# as input and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.
import sec as sec


def make_readable(seconds: int) -> str:
    try:
        if seconds > 359999:
            raise ValueError
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        secs = seconds - hours * 3600 - minutes * 60
        return '{:02}:{:02}:{:02}'.format(hours, minutes, secs)
    except ValueError as e:
        print(e, "Число секунд должно быть менее 359999")


if __name__ == '__main__':
    print(make_readable(86399))
