# Jeremy Lance
# Functions Problem 2

def compute_avg(hits, at_bats):
    avg = hits / at_bats
    return avg

def main():
    player_count = 0
    response = input("Do you want to enter a player? (Yes/No): ")

    while response.lower() == "yes":
        last_name = input("Enter player's last name: ")
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))

        avg = compute_avg(hits, at_bats)
        player_count += 1

        print(f"\nPlayer: {last_name}")
        print(f"Batting Average: {avg:.3f}\n")

        response = input("Do you want to enter another player? (Yes/No): ")

    print(f"\nNumber of players entered: {player_count}")

main()
