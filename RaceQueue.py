import datetime
import time
import pickle

class RaceQueue():
    
    def __init__(self):
        self.waiting_list = []
        self.ready_teams = []
        self.race_history = []
        self.registered_teams = []
    
    def register_team(self, team_id):
        if team_id not in self.registered_teams:
            self.registered_teams.append(team_id)
    
    def register_teams(self, team_ids):
        for team_id in team_ids:
            self.register_team(team_id)
            
    def register_attempt(self, team_id):
        if team_id in self.registered_teams:
            if team_id in self.ready_teams:
                self.waiting_list[self.ready_teams.index(team_id)]["ready_time"] = datetime.datetime.now()
                waiting_info = self.waiting_list[self.ready_teams.index(team_id)]
                 
            else:
                waiting_info = {"id":team_id, "ready_time":datetime.datetime.now(), "number_of_attempts":0}
                self.waiting_list.append(waiting_info)
                self.ready_teams.append(team_id)
            
            print('Team {} have registered an attempt.'.format(team_id))
            self.race_history.append(waiting_info)
            
        else:
            print('Can\'t find the team name, have you registered it and spell it correct?')

        with open('race_history.txt', 'wb') as f:
            pickle.dump(self.waiting_list, f)
    
            
    def next_ready_teams(self, number=3):
        sorted_waiting_list = sorted(self.waiting_list, key=lambda d: (d["number_of_attempts"], d["ready_time"]))
        for waiting_teams in sorted_waiting_list[:min(number,len(sorted_waiting_list))]:
            print('Team {} please wait to start race.'.format(waiting_teams['id']))
    
    def finish_attempt(self, team_id):
        if team_id in self.registered_teams:
            if team_id in self.ready_teams:
                number_of_attempts = self.waiting_list[self.ready_teams.index(team_id)]["number_of_attempts"]
                self.race_history.append({"id":team_id,
                                          "finish_time":datetime.datetime.now(),
                                          "number_of_attempts":number_of_attempts})
                self.waiting_list[self.ready_teams.index(team_id)]["number_of_attempts"] = number_of_attempts + 1
            else:
                print("This team haven't registered for an attempt yet!")
        
        with open('race_history.txt', 'wb') as f:
            pickle.dump(self.waiting_list, f)
             
if __name__ == "__main__":
    rq = RaceQueue()
    rq.register_teams(['Shanghai','Zhejiang','Soton'])

    rq.register_team('Plymouth')
    time.sleep(5)
    rq.register_attempt('Plymouth')
    time.sleep(5)
    rq.register_attempt('Shanghai')
    time.sleep(5)
    rq.register_attempt('Soton')
    time.sleep(5)
    rq.register_attempt('Zhejiang')
    time.sleep(5)
    print(rq.next_ready_teams(number=2))
    rq.finish_attempt('Shanghai')
    time.sleep(5)
    print(rq.next_ready_teams())
    time.sleep(5)
    rq.register_attempt('Soton') # Unsuccessful attempt
    print(rq.next_ready_teams())
    print(rq.race_history)

