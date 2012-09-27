from sensor import Sensor

class Alarm(object):

    def __init__(self):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = Sensor()
        self.is_alarm_on = False
        self._alarm_count = 0

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        if psi_pressure_value < self._low_pressure_threshold or self._high_pressure_threshold < psi_pressure_value:
            self.is_alarm_on = True
            self._alarm_count += 1
