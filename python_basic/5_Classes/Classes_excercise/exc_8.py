from datetime import datetime


class Case:
    def __init__(self, case_data):
        self.name = case_data['name']
        self.created_task = datetime.fromisoformat(case_data['created_task'])
        self.end_task = None if case_data['end_task'] is None else \
            datetime.fromisoformat(case_data['end_task'])

    def retrieve_seconds(self):
        if self.end_task is None:
            return None

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
seconds_second_case = second_case.retrieve_seconds()

print(f"time difference first_case: {seconds_first_case} sec")
print(f"time difference second_case: {seconds_second_case} sec")


