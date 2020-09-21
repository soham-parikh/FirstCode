import numpy as np

class Cricket:

    def __init__(self, runs, overs):
        self.runs = runs
        self.overs = overs
    

    def changestrike(self, playing):
        return playing[::-1]

    
    def random_runs(self, probs, playing):
        return np.random.choice(np.arange(8), p=probs[playing[0]])

    def print_ball(self, over, ball, player, score):
        if score == 1:
            print(str(over) + "." + str(ball + 1) + " " +
                  str(player) + " scores " + str(score) + " run")
        else:
            print(str(over) + "." + str(ball + 1) + " " +
                  str(player) + " scores " + str(score) + " runs")

    def start(self):
        

        
        overs = self.overs
        
        runs = self.runs
        
        wickets = 0
        
        balls = 6
        
        players = ["Kirat Boli", "NS Nodhi", "R Rumrah", "Shashi Henra"]
        
        remaining = players[2:]
        
        
        scores = {players[0]: {"Score": 0, "Balls": 0, "Out": False},
                  players[1]: {"Score": 0, "Balls": 0, "Out": False}}
        
        probs = {players[0]: [0.05, 0.30, 0.25, 0.10, 0.15, 0.01, 0.09, 0.05],
                 players[1]: [0.10, 0.40, 0.20, 0.05, 0.10, 0.01, 0.04, 0.10],
                 players[2]: [0.20, 0.30, 0.15, 0.05, 0.05, 0.01, 0.04, 0.20],
                 players[3]: [0.30, 0.25, 0.05, 0.00, 0.05, 0.01, 0.04, 0.30]}
        
        playing = [players[wickets], players[wickets + 1]]

        for over in range(overs):
            print()
            print(str(overs - over) + " overs left. " +
                  str(runs) + " runs to win")
            print()
            for ball in range(balls):
                
                
                randno = self.random_runs(probs, playing)
                
                scores[playing[0]]["Balls"] += 1
                
                if randno != 7:
                    
                    runs = runs - randno
                    
                    scores[playing[0]]["Score"] += randno
                    
                    self.print_ball(over, ball, playing[0], randno)
                    
                    if randno % 2 != 0:
                        playing = self.changestrike(playing)
                    else:
                        pass
                    
                    if runs <= 0:
                        print()
                        print("Lengaburu won by " + str(3 - wickets) + " wickets and " +
                              str(((overs - 1 - over) * 6) +
                                  (5 - ball)) + " balls remaining")
                        self.print_scores(scores)
                        return
                else:
                    
                    wickets += 1
                    
                    scores[playing[0]]['Out'] = True
                    print(str(over) + "." + str(ball) +
                          " " + str(playing[0]) + " Out!")
                    
                    if wickets == 3:
                        print()
                        print("Lengaburu lost by " + str(runs) + " runs")
                        self.print_scores(scores)
                        return
                    else:
                       
                        playing = [remaining[0], playing[1]]
                        scores[remaining[0]] = {
                            "Score": 0, "Balls": 0, "Out": False}
                       
                        remaining.remove(remaining[0])
            
            playing = self.changestrike(playing)
        print()
       
        if runs == 0:
            print("Match tied!")
        
        else:
            print("Lengaburu lost by " + str(runs) + " runs")
        self.print_scores(scores)
        return

   

    def print_scores(self, scores):
        print()
        print("-----------------")
        print("SCOREBOARD")
        print("-----------------")
        for player in scores:
            
            if scores[player]["Out"] is False:
                print(player + " - " + str(scores[player]["Score"]) +
                      "* (" + str(scores[player]["Balls"]) + " balls)")
            else:
                print(player + " - " + str(scores[player]["Score"]) +
                      " (" + str(scores[player]["Balls"]) + " balls)")



if __name__ == "__main__":
    match1 = Cricket(40, 4)
    match1.start()
