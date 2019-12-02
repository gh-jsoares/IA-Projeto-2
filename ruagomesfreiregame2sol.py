import random

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        ALPHA = 1
        GAMMA = 0.9

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):
                self.nS = nS
                self.nA = nA
                # create a table nS x nA
                self.qTable = [[0] * nA ] * nS


              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # print("select one action to learn better")
                a = random.randrange(len(aa))
                #TODO: Missing stuff?
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                a = 0
                # print("select one action to see if I learned")
                for ai in range(len(aa)):
                        if self.qTable[st][ai] > self.qTable[st][a]:
                                a = ai
                return a


        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                #print("learn something from this data")
                self.qTable[ost][a] = self.qTable[ost][a] + self.ALPHA * (r + self.GAMMA * max(self.qTable[nst]) - self.qTable[ost][a])
                #TODO: Missing stuff?
                return
