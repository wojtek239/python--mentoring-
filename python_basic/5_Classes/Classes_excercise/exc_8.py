from datetime import datetime as dt


class Case:
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"

    def __init__(self, case_data):
        self.name = case_data['name']
        self.created_task = dt.strptime(case_data['created_task'], self.TIME_FORMAT)
        self.end_task = dt.strptime(case_data['end_task'], self.TIME_FORMAT) if case_data['end_task'] else dt.now()

    def retrieve_seconds(self) -> float:

        time_difference = self.end_task - self.created_task
        return time_difference.total_seconds()


first_case = Case({
    'name': 'first_case',
    'created_task': '2021-10-26T19:48:12+00:00',
    'end_task': None
})

second_case = Case({
    'name': 'second_case',
    'created_task': '2021-09-26T19:48:12+00:00',
    'end_task': '2021-10-26T19:48:12+00:00'
})

seconds_first_case = first_case.retrieve_seconds()
print(f"time difference first_case: {seconds_first_case} sec")

seconds_second_case = second_case.retrieve_seconds()
print(f"time difference second_case: {seconds_second_case} sec")
