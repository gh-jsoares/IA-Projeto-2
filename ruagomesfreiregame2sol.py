import random

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        ALPHA = 0.8 # learning rate
        GAMMA = 0.8 # discount factor
        EPSILON = 0.3 # exploration rate

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):
                self.nS = nS
                self.nA = nA

                # create a table nS x nA
                self.qTable = [[]] * nS
                for i in range(nS):
                        self.qTable[i] = [0] * nA

                self.actions = [0] * nS
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # print("select one action to learn better")

                self.actions[st] = len(aa)

                if random.uniform(0, 1) < self.EPSILON:
                        return random.randint(0, self.actions[st] - 1)
                return self.selectactiontoexecute(st, aa)

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                # print("select one action to see if I learned")

                self.actions[st] = len(aa)

                a = 0
                for i in range(0, self.actions[st]):
                        if self.qTable[st][i] > self.qTable[st][a]:
                                a = i
                return a


        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                #print("learn something from this data")
                max_a = max(self.qTable[nst][:self.actions[nst]]) if self.actions[nst] != 0 else 0
                self.qTable[ost][a] += self.ALPHA * (r + self.GAMMA * max_a - self.qTable[ost][a])
                return
