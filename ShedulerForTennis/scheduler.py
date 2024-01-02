from datetime import datetime, timedelta

# SETTINGS
SLOT_DURATION = 60  # minutes
START_HOUR = 9
END_HOUR = 21


# CLASSES
class Slot:
    """Class for one slot."""

    def __init__(self, start_time: datetime.time, duration: datetime = timedelta(minutes=SLOT_DURATION)):
        self.start_time = start_time
        self.duration = duration
        self.is_reserved = False
        self.owner = None


class DailySchedule:
    """Class for dayly schedule."""

    def __init__(self, date: datetime.date):
        self.date = date
        self.slots = self.generate_slots_for_day(date)

    @staticmethod
    def generate_slots_for_day(date: datetime.date):
        res = []
        cur = date + timedelta(hours=START_HOUR)
        while cur <= date + timedelta(hours=END_HOUR):
            res.append(Slot(cur))
            cur += timedelta(minutes=SLOT_DURATION)
        return res


class ScheduleManager:
    """Class for managing schedules."""

    def __init__(self):
        self.schedules = {}

    def add_daily_schedule(self, day_date: datetime.date):
        schedule = DailySchedule(day_date)
        self.schedules[day_date] = schedule

    def book_slot(self, slot_: datetime):
        cur_day = datetime(year=slot_.year, month=slot_.month, day=slot_.day, hour=0, minute=0)
        if cur_day in self.schedules.keys():
            schedule = self.schedules[cur_day]
            for slot in schedule.slots:
                if slot.start_time == slot_ and not slot.is_reserved:
                    slot.is_reserved = True
                    print(
                        f"Вы зарезервировали слот {slot.start_time} -- {slot.start_time + timedelta(minutes=SLOT_DURATION)}.")
                elif slot.start_time == slot_ and slot.is_reserved:
                    print(
                        f"К сожалению слот {slot.start_time} -- {slot.start_time + timedelta(minutes=SLOT_DURATION)} уже занят.")


# MAIN PROGRAM

if __name__ == '__main__':
    y = ScheduleManager()

    # Initiate schedules for num_of_days
    start_day = cur_day = datetime(year=2024, month=1, day=1)
    num_of_days = 91
    end_day = start_day + timedelta(days=num_of_days)
    while cur_day < end_day:
        y.add_daily_schedule(cur_day)
        cur_day += timedelta(days=1)

    # Show schedules
    for k, v in y.schedules.items():
        x = y.schedules[k].slots
        print(f"\n{k.strftime('%d.%m.%Y %H:%M')}\n----------")
        for item in x:
            print(item.start_time.strftime('%d.%m.%Y %H:%M'), item.is_reserved, item.owner, sep=' ')

    # Book some slots
    y.book_slot(datetime(year=2024, month=1, day=2, hour=10, minute=0))
    y.book_slot(datetime(year=2024, month=1, day=2, hour=11, minute=0))
    y.book_slot(datetime(year=2024, month=1, day=2, hour=10, minute=0))
