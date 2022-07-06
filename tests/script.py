# Class to create weekly workouts
import json
import csv
import sys

class Workout:
    exercises = []
    sets = []
    rests = []
    all = []

    def __init__(self, name, set, rest=60):
        self.name = name
        self.set = set
        self.rest = rest

        # Actions to execute 
        Workout.all.append(self)

        # Call func to add to each class list
        self.workout(self.name, self.set, self.rest)

    # DUNDER method
    def __repr__(self) -> str:
        return f'Workout({self.name}, {self.set}, {self.rest})'

    # Instance methods
    def workout(self, name, set, rest):
        self.exercises.append(name)
        self.sets.append(set)
        self.rests.append(rest)

    def call_workout(self):
        workout =  zip(self.exercises, self.sets, self.rests)
        print('Exercise,Sets,Rest')
        print(*workout)
        return ''

    def to_dict(self):
        workout = {}
        x = zip(self.exercises, self.sets, self.rests)
        print()
        for i in x:
            workout[i[0]] = [i[1], i[2]]
        return workout

    def to_json(self):
        workout = {}
        x = zip(self.exercises, self.sets, self.rests)
        print()
        for i in x:
            workout[i[0]] = [i[1], i[2]]
        # Serialization of JSON obj
        json_obj = json.dumps(workout, indent=4)
        return json_obj
               
    def write_json(self):
        x = self.to_json()
        with open('sample.json', 'a') as f:
            f.write(x)
               
    # Class method -> Call on class level
    @classmethod
    def instantiate_from_csv(cls):
        file = 'test.csv'
        if '.csv' not in file:
            exit()
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            exercises = list(reader)
            for i in exercises:
                Workout(
                    name=i.get('Exercise'),
                    set=i.get('Sets').strip('\t'),
                    rest=i.get('Rest')
                )
            for n in Workout.all:
                print(n)
    

def create_workout():
    
    UpperBody1 = ['Bench press', 'OHP', 'T-bar row', 'Cable Extension + Face Pull', 'Lateral raise']
    UpperBody1Sets = ['90x1+'.strip('\t'), '8x12', '3x10', '4x12', '3x12']
    UpperBody1Rests = [180, 120, 120, 60,60]
    wk = zip(UpperBody1, UpperBody1Sets, UpperBody1Rests)
    for i in wk:
        w = Workout(i[0], i[1], i[2])

    LowerBody1 = ['Squat','Sumo deadlift', 'Hip thrust', 'lying leg curl', 'Hanging leg raises']
    LowerBody1Sets = ['116x1+', '110x5', '80x6', '32.5x10', 'BWx12']
    LowerBody1Rests = [240, 180, 120, 60, 60]
    wk1 = zip(LowerBody1, LowerBody1Sets, LowerBody1Rests)
    for i in wk1:
        w1 = Workout(i[0], i[1], i[2])

    UpperBody2 = ['Bench Press Max', 'C.G.B.P', 'Pull Ups', 'Skullcrusher', 'Hammer curl']
    UpperBody2Sets = ['90x1+', '57.5x8', 'BWx6', '32.5x12', '20x8']
    UpperBody2Rests = [180, 120, 120, 90, 90]
    wk2 = zip(UpperBody2, UpperBody2Sets, UpperBody2Rests)
    for i in wk2:
        w2 = Workout(i[0], i[1], i[2])

    LowerBody2 = ['Max Deadlift', 'Front Squat', 'Shrugs', 'RDL', 'Calve Raises', 'Ball crunch']
    LowerBody2Sets = ['152x1+', '68x8+', '70x10', '80x8', '50x10', '7.5x12']
    LowerBody2Rests = [240, 160, 120, 120, 60, 60]
    wk3 = zip(LowerBody2, LowerBody2Sets, LowerBody2Rests)
    for i in wk3:
        w3 = Workout(i[0], i[1], i[2])

    print(w3.to_dict())
    return 1

if __name__ == '__main__':
    run = input('Y or N: ')
    if run == 'Y':
        print(create_workout())
    else:
        sys.exit()


