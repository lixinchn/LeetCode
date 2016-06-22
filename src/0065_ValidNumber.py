class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        state = 0
        for i in xrange(0,len(s)):
            state = self.nextState(state, s[i])
            if state == -1: 
                return False
        state = self.nextState(state, ' ')
        return state == 8
    
    def nextState(self, state,char):
        transititionTable = [[0,2,1,3,-1,-1], [-1,2,-1,3,-1,-1], [8,2,-1,4,5,-1], [-1,4,-1,-1,-1,-1], [8,4,-1,-1,5,-1],[-1,7,6,-1,-1,-1],[-1,7,-1,-1,-1,-1], [8,7,-1,-1,-1,-1], [8,-1,-1,-1,-1,-1]];
        return transititionTable[state][self.getSymbol(char)]
    
    def getSymbol(self, char):
        if char == ' ' or char == '\t':
            return 0
        if char.isdigit():
            return 1
        if char == '+'  or char == '-':
            return 2
        if char == '.':
            return 3
        if char == 'E' or char =='e':
            return 4
        return 5