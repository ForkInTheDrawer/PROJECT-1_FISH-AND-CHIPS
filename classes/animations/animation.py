from . import easing


class Animation:
    def __init__(self, start_val, end_val, duration, easing_function=easing.linear):
        self.start_val = start_val
        self.end_val = end_val
        self.duration = duration
        self.easing_function = easing_function

        self.elapsed_time = 0
        self.current_value = start_val

        self.finished_status = False

        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")



    def update(self, dt):

        if self.finished_status:
            return self.current_value

        self.elapsed_time += dt

        progress_status = min(self.elapsed_time / self.duration, 1.0)

        eased_progress_status = self.easing_function(progress_status)

        self.current_value = (
            self.start_val + (self.end_val - self.start_val) * eased_progress_status
        )


        if progress_status >= 1.0:
            self.finished_status = True