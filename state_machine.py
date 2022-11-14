import time

class StateMachine:
    state = None
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start_state(self, name):
        self.startState = name

    def run(self):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise  InitializationError("at least one state must be an end_state")
    
        while True:
            (newState) = handler()
            if newState in self.endStates:
                break 
            else:
                handler = self.handlers[newState]   

    def start_transition(self):
        while True:
            print("Initializing...")
            time.sleep(3)
            newstate = "state_one"
            return (newstate)
    
    def state_one(self):
        time.sleep(1)
        while True:
            self.state = 2
            print("state one reached...")
            time.sleep(4)
            if self.state == 2:
                newState = "state_two"
                return (newState)
            else:
                print("waiting for transition...")
                time.sleep(1)
    
    def state_two(self):
        time.sleep(1)
        while True:
            self.state = 3
            print("state two reached...")
            time.sleep(4)
            if self.state == 3:
                newState = "state_three"
                return (newState)
            else:
                print("waiting for transition...")
                time.sleep(1)

    def state_three(self):
        while True:
            self.state = 4
            print("Final state reached... Shutting down.")
            time.sleep(4)
            if self.state == 4:
                newState = "final_state"
                return (newState)
            else:
                print("Waiting for transition..")
                time.sleep(1)
    

m = StateMachine()

m.add_state("init_state", m.start_transition)
m.add_state("state_one", m.state_one)
m.add_state("state_two", m.state_two)
m.add_state("state_three", m.state_three)
m.add_state("final_state", None, end_state=1)
m.set_start_state("init_state")

m.run()