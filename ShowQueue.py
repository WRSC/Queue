import datetime
import time
import pickle

def next_ready_teams(self, number=3):
        sorted_waiting_list = sorted(self.waiting_list, key=lambda d: (d["number_of_attempts"], d["ready_time"]))
        for waiting_teams in sorted_waiting_list[:min(number,len(sorted_waiting_list))]:
            print('Team {} please wait to start race.'.format(waiting_teams['id']))


if __name__ == "__main__":
    pass