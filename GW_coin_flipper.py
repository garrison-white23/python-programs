#   Coin Flipper
#   Author: Garrison White
#   Date: 11/15/2025
#   Description: Flip a coin as many times as you want. Tracks staticstics.

import random

print("------------------------")
print("      coin flipper      ")
print("------------------------")

def main():
    playagain = "1"

    stats = {
        "numheads": 0,
        "numtails": 0,
        }
    stats["totalflips"] = stats["numheads"] + stats["numtails"]
    stats["freqheads"] = 0
    stats["freqtails"] = 0
            
                
    while playagain == "1":
        choice = play_again()
        
        if choice == "":
            stats = flip_coin(stats)
        elif choice == "1":
            show_stats(stats)
        else:
            break
        
    print("\n\nGoodbye!")
    print(input('\nHit Enter to Close\n'))
    

def flip_coin(stats):
    stats["totalflips"] += 1
    flip = random.randint(1,2)

    if flip == 1:
        stats["numheads"] += 1
        print("\nheads")
    else:
        stats["numtails"] += 1
        print("\ntails")

    if stats["numheads"] > 0:
        stats["freqheads"] = (stats["numheads"] / stats["totalflips"]) * 100
    else:
        stats["freqheads"] = 0
    if stats["numtails"] > 0:
        stats["freqtails"] = (stats["numtails"] / stats["totalflips"]) * 100
    else:
        stats["freqtails"] = 0

    return stats


def show_stats(stats):
    print("\n---------------------")
    print(f"number of flips: {stats['totalflips']}")
    print(f"{stats['freqheads']:.2f}% heads")
    print(f"{stats['freqtails']:.2f}% tails")
    print("---------------------")
    

def play_again():
    choice = " "
    while choice not in ["", "1", "2"]:
        choice = input("\n[Enter]Flip coin\n[1]Show stats\n[2]Quit\n>")
        if choice not in ["", "1", "2"]:
            print("\nInvalid response.")
    return choice


if __name__ == "__main__":
    main()
