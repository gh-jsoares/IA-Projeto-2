import random
import numpy as np

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        ALPHA = 0.7
        GAMMA = 0.85
        EPSILON = 0.3

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):
                self.nS = nS
                self.nA = nA
                # create a table nS x nA
                self.qTable = np.zeros((nS, nA))
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # print("select one action to learn better")
                # return random.randrange(len(aa))
                if random.uniform(0, 1) < self.EPSILON:
                        return random.randint(0, len(aa) - 1)
                return self.selectactiontoexecute(st, aa)

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                # print("select one action to see if I learned")

                # a = 0
                # for i in range(1, len(aa)):
                #         if self.qTable[st, i] > self.qTable[st, a]:
                #                 a = i
                # return a

                return np.argmax(self.qTable[st, :len(aa)])


        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                #print("learn something from this data")
                self.qTable[ost, a] = self.qTable[ost, a] + self.ALPHA * (r + self.GAMMA * np.max(self.qTable[nst, :]) - self.qTable[ost, a])
                return
