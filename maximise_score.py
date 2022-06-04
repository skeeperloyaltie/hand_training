def player(player1, player2):
    if player1[0] > 1:
        if player1[0] > player2[0]:
            return player1
        else:
            return player2
    else:
        if player1[1] > player2[1]:
            return player1
        else:
            return player2

    
def main():
    player1 = [int(i) for i in input().split()]
    player2 = [int(i) for i in input().split()]
    print(player(player1, player2))



if __name__ == '__main__':
    main()
    