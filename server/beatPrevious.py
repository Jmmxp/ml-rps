class BeatPrevious:

    def choose(self, selfHistory, enemyHistory):
        if(not len(enemyHistory)):
            return "r"

        enemyLast = enemyHistory[-1]
        selfLast = selfHistory[-1]

        opposing = {"r": "p","p": "s","s": "r"}

        # if opponent just lost, expect them to switch to beat your previous move
        if (selfLast == opposing[enemyLast]):
            return enemyLast
        else:
            return opposing[enemyLast]

