import itertools as it

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    for i in range(6):
        for j in range(6):
            if (dice1[i] > dice2[j]):
                dice1_wins += 1
            elif (dice1[i] < dice2[j]):
                dice2_wins += 1
            else:
                pass

    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    # count the winning times of each dice
    wins_count = [0 for _ in range(len(dices))]
    for i, j in it.combinations(range(len(dices)), r=2):
        dicei_wins, dicej_wins = count_wins(dices[i], dices[j])
        if (dicei_wins > dicej_wins):
            wins_count[i] += 1
        elif (dicei_wins < dicej_wins):
            wins_count[j] += 1
        else:
            pass
    # find if there is a best dice
    for dice in range(len(dices)):
        if wins_count[dice] == len(dices) - 1:
            return dice

    return -1

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)
        
    # Check which strategy to apply
    dice = find_the_best_dice(dices)
    if dice == -1:
        strategy["choose_first"] = False
    else:
        strategy["first_dice"] = dice
    # If don't choose first, find which dice to choose after the opponent chooses his/her dice
    n = len(dices)
    for i in range(n): # the dice which the opponent chooses
        max_win_count = 0
        max_win_dice = 0
        for j in range(n):
            i_wins, j_wins = count_wins(dices[i], dices[j])
            win_count = j_wins - i_wins
            if win_count > max_win_count:
                max_win_count = win_count
                max_win_dice = j
        strategy[i] = max_win_dice

    return strategy

if __name__ == "__main__":
    dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
    res = compute_strategy(dices)
    print(res)