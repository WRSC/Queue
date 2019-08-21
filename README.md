# Queue

Queue is the competition organisation tool for WRSC.

Teams register for an attempt and Queue decide who compete first.
The tool is designed to guarantee at least one attempt for each team.


```

Register team(s) --> Register attempt --> Waiting --> Race --> Finish --> End
                            |                                    |
                            |                                    |
                        Another attempt <------------------------- 
```

The following example show the usage of `RaceQueue`. Use `ipython -i RaceQueue.py` to run the admin tool. 

```python

# Register multiple teams
rq.register_teams(['Shanghai','Zhejiang','Soton'])

# Register one single team
rq.register_team('Plymouth')


# Register attempt by first come first serve rule
rq.register_attempt('Plymouth')

rq.register_attempt('Shanghai')

rq.register_attempt('Soton')

rq.register_attempt('Zhejiang')

# Decide next teams to race
print(rq.next_ready_teams(number=2))

# Record a finish of attempt
rq.finish_attempt('Shanghai')
print(rq.next_ready_teams())

# Duplicate registration would result in waiting from the end of queue
rq.register_attempt('Soton') 

print(rq.next_ready_teams())
print(rq.race_history)

```

Open a new terminal to show the queueing status `python ShowQueue.py`.

![Screenshot from 2019-08-21 17-45-38](https://user-images.githubusercontent.com/6488896/63470847-a745e100-c43b-11e9-80d1-280d0481d676.png)
