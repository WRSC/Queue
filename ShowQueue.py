import datetime
import time
import pickle
import curses

def next_ready_teams(waiting_list, number=3):
    sorted_waiting_list = sorted(waiting_list, key=lambda d: (d["number_of_attempts"], d["ready_time"]))
    waiting_teams = sorted_waiting_list[:min(number,len(sorted_waiting_list))]
    return waiting_teams
    


def main(screen_display):
    screen_display = curses.initscr()
    screen_display.border(0)

    while True:
        with open('race_history.txt', 'rb') as f:
            waiting_list = pickle.load(f)

        #next_ready_teams(waiting_list)
        screen_display.addstr(1, 1, "WRSC Queueing System")
        screen_display.addstr(3, 3, "Please be prepared to start your race:")
        waiting_teams = next_ready_teams(waiting_list, number=5)
        team_order = 1
        for waiting_team in waiting_teams:
            screen_display.addstr(6+team_order, 6, "{}. Team {}".format(team_order, waiting_team['id']))
            team_order += 1

        screen_display()
        screen_display.refresh()
        time.sleep(5)

    

if __name__ == "__main__":

    

    curses.wrapper(main)