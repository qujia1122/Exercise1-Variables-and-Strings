import random

def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def move_player(position, direction, grid_size):
    x, y = position
    if direction == 'N' and y > 0:
        y += 1
    elif direction == 'S' and y < grid_size - 1:
        y -= 1
    elif direction == 'E' and x < grid_size - 1:
        x += 1
    elif direction == 'W' and x > 0:
        x -= 1
    else:
        return position  # Illegal move
    return [x, y]

def treasure_hunt(grid_size, max_moves):
    player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    current_moves = 0

    print(f"Game starts! Your initial position is: {player_position}")
    print(f"The treasure is hidden at: {treasure_position} (Keep this a secret!)")
    initial_distance = calculate_distance(player_position, treasure_position)
    print(f"The initial distance to the treasure is: {initial_distance} steps")

    while current_moves < max_moves:
        direction = input("Enter your move direction (N, S, E, W): ")
        new_position = move_player(player_position, direction, grid_size)
        if new_position == player_position:
            print("This move is not allowed, you cannot stay in place.")
        else:
            player_position = new_position
            current_moves += 1
            distance = calculate_distance(player_position, treasure_position)
            if distance < initial_distance:
                print("You are getting closer to the treasure!")
            elif distance > initial_distance:
                print("You are moving farther away from the treasure.")
            else:
                print("Your distance to the treasure remains the same.")

            if player_position == treasure_position:
                print("Congratulations, you've found the treasure!")
                return
            initial_distance = distance

        if current_moves == max_moves:
            print("You have no more moves, the game is over. The treasure was located at:", treasure_position)

grid_size = 5  # Define the size of the grid
max_moves = 10  # Define the maximum number of moves the player can make
treasure_hunt(grid_size, max_moves)