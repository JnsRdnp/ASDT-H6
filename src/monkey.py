import pygame
import time
import threading
import numpy as np
import random

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location, main_running, side="Right"):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.main_running = main_running

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

        self.current_index = None
        self.font = pygame.font.SysFont(None, 24)  # Set up the font for rendering text


        self.kaivuu_kahva = None
        self.apina_kaivaa = False
        self.ditch = None
        
        
        if side == "Left":
            self.sidex = 30
        else:
            self.sidex = 0


        self.sleep_event = threading.Event()  # Create an event for controlling sleep
        self.sleep_event.set()  # Initially allow sleeping


        pygame.mixer.init()
        self.sand_sound = pygame.mixer.Sound("./assets/sand.wav")  # Replace with your beep sound file path


    def draw(self, screen):
        # Draw the monkey image
        screen.blit(self.resized_image, self.rect)

        # Create the text surface for the current index
        # if self.current_index is not None:
        #     index_text = f"Index: {self.current_index}"
        #     text_surface = self.font.render(index_text, True, (255, 255, 255))  # White text color
        #     text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Position below the monkey
        #     screen.blit(text_surface, text_rect)

    def dig(self, Ditch, start_col=None, start_row=None):
        self.apina_kaivaa = True
        self.time_to_dig = 1  # Initial time in seconds between digs
        self.stamina_multiplier = 2  # Time to dig multiplies by 2 every time

        print("Initial ditch matrix:")
        print(Ditch.ditch_matrix)

        if start_col is None and start_row is None:
            # Start digging normally from the last available positions
            while self.apina_kaivaa and self.main_running[0]:
                # Find the indices of all '1's
                indices = np.argwhere(Ditch.ditch_matrix == 1)  # Get indices of all '1's
                
                if len(indices) >= 4:  # Ensure there are at least four '1's to change
                    # Get the last four indices
                    last_four_indices = indices[-4:]  # Get the last four positions

                    # Decrement the values at these indices by 1
                    time.sleep(self.time_to_dig)  # Wait for the specified digging time
                    for row, col in last_four_indices:
                        Ditch.ditch_matrix[row, col] -= 1  # Change value to one less
                        self.sand_sound.play()

                    print(f"Digging at positions: {last_four_indices}")  # Print the positions dug
                    
                    # Update the current index to the last position dug
                    self.current_index = (last_four_indices[-1][0], last_four_indices[-1][1])

                else:
                    print("Not enough '1's to dig. Stopping digging.")
                    break  # Exit if there are fewer than 4 '1's

                # Double the time to dig for the next iteration
                self.time_to_dig *= self.stamina_multiplier
                self.update_position(Ditch)

            print("Updated ditch matrix:")
            print(Ditch.ditch_matrix)
        else:
            # Start digging from specified start_col and start_row
            self.current_col = start_col
            self.current_row = start_row
            print(self.current_row)

            while self.apina_kaivaa and self.main_running[0]:

                if self.current_row >= 1:

                    if Ditch.ditch_matrix[self.current_row,self.current_col] > 0:
                        self.update_position(Ditch, start_col=0, start_row=self.current_row)

                        time.sleep(self.time_to_dig)
                        Ditch.ditch_matrix[self.current_row,self.current_col] -= 1
                        Ditch.ditch_matrix[self.current_row, self.current_col+1] -= 1
                        Ditch.ditch_matrix[self.current_row-1, self.current_col] -= 1
                        Ditch.ditch_matrix[self.current_row-1, self.current_col+1] -= 1
                        self.sand_sound.play()
                        self.time_to_dig *= self.stamina_multiplier

                        print(Ditch.ditch_matrix)

                        self.current_row -= 2

                    else:
                        self.current_row -= 2
                        self.update_position(Ditch, start_col=0, start_row=self.current_row)
                
                else:
                    indices = np.argwhere(Ditch.ditch_matrix == 1)  # Get indices of all '1's
                    
                    if len(indices) >= 4:  # Ensure there are at least four '1's to change
                        # Get the last four indices
                        last_four_indices = indices[-4:]  # Get the last four positions
                        time.sleep(self.time_to_dig)  # Wait for the specified digging time
                        for row, col in last_four_indices:
                            Ditch.ditch_matrix[row, col] -= 1  # Change value to one less
                            self.sand_sound.play()
                        self.time_to_dig *= self.stamina_multiplier
                    else:

                        print("Valmista")
                        break
                


    def random_dig(self, Ditch):
        # Get the number of rows and columns in the ditch matrix
        num_rows, num_cols = Ditch.ditch_matrix.shape  # Should be (200, n)


        odd_row = random.randint(1, (num_rows // 2) - 1) * 2 + 1  # Random odd row index
        col = 0

        print("rows: ", odd_row, "cols: ", num_cols)
        self.update_position(Ditch, odd_row, col)
        self.dig(Ditch, col, odd_row)


        
            
    def update_position(self, Ditch, start_col=None, start_row=None):
        if start_col == None:
            self.ditch = self.get_last_ditch_position(Ditch)
            self.target_location, self.current_index = self.ditch
            self.rect.bottomleft = (self.target_location[0]-self.sidex,self.target_location[1]+10)
        else:
            self.ditch_start = self.get_ditch_position(Ditch,start_row,start_col)
            print("self.ditch_start: ", self.ditch_start)
            self.rect.bottomleft = (self.ditch_start[0]-self.sidex, self.ditch_start[1]+10)


    def move_to_last(self, Ditch):
        """Move the monkey to the target position incrementally."""
        self.ditch = self.get_last_ditch_position(Ditch)
        self.target_location, self.current_index = self.ditch
        # Calculate the total distance to move in x and y directions
        delta_x = self.target_location[0] - self.rect.x - self.sidex
        delta_y = self.target_location[1]-20 - self.rect.y

        # Determine the number of steps to take for each direction
        steps_x = abs(delta_x)
        steps_y = abs(delta_y)

        # Move incrementally in the x direction
        if steps_x > 0:  # Check if movement in x direction is needed
            step_direction_x = 1 if delta_x > 0 else -1  # Determine the direction
            for _ in range(steps_x):
                self.rect.x += step_direction_x  # Move one step in the x direction
                print("Apina liikkui tähän: ", self.rect.topleft)
                time.sleep(0.01)  # Control speed of movement

        # Move incrementally in the y direction
        if steps_y > 0:  # Check if movement in y direction is needed
            step_direction_y = 1 if delta_y > 0 else -1  # Determine the direction
            for _ in range(steps_y):
                self.rect.y += step_direction_y  # Move one step in the y direction
                print("Apina liikkui tähän: ", self.rect.topleft)
                time.sleep(0.01)  # Control speed of movement

        # Start the digging thread after reaching the target
        self.kaivuu_kahva = threading.Thread(target=self.dig, args=(Ditch,))

    def get_ditch_position(self, ditch, row, col):
        """
        Calculate the world coordinates of the given row and column in the ditch matrix.
        """
        x = ditch.rect.x + col * ditch.ppu  # x-coordinate based on column
        y = ditch.rect.y + row * ditch.ppu  # y-coordinate based on row
        print(f"Ditch position for matrix (row: {row}, col: {col}): ({x}, {y})")
        return (x, y)  # Return the position on the screen

    
    def get_last_ditch_position(self, ditch):
        """Find the last available group of four adjacent tiles with values greater than 0 in the ditch matrix and return their position and matrix index."""
        # Reverse iteration: Start from the last row and last column
        for row in range(ditch.ditch_matrix.shape[0] - 1, -1, -1):
            for col in range(ditch.ditch_matrix.shape[1] - 1, -1, -1):
                if self.check_adjacent_tiles(ditch, row, col):
                    # Calculate world coordinates of the matrix position for the first tile of the group
                    x = ditch.rect.x + col * ditch.ppu
                    y = ditch.rect.y + row * ditch.ppu
                    print("Last ditch pos (adjacent tiles): ", x, y)
                    return (x, y), (row, col)  # Return the position of the first tile and its matrix index

        return None, None  # If no position is found

    def check_adjacent_tiles(self, ditch, row, col):
        """Check if there are four adjacent tiles (horizontally, vertically, or diagonally) with values greater than 0."""
        # Check horizontally (right)
        if col + 3 < ditch.ditch_matrix.shape[1] and all(ditch.ditch_matrix[row, col+i] > 0 for i in range(4)):
            return True
        # Check vertically (down)
        if row + 3 < ditch.ditch_matrix.shape[0] and all(ditch.ditch_matrix[row+i, col] > 0 for i in range(4)):
            return True
        # Check diagonally (down-right)
        if row + 3 < ditch.ditch_matrix.shape[0] and col + 3 < ditch.ditch_matrix.shape[1] and \
        all(ditch.ditch_matrix[row+i, col+i] > 0 for i in range(4)):
            return True
        # Check diagonally (down-left)
        if row + 3 < ditch.ditch_matrix.shape[0] and col - 3 >= 0 and \
        all(ditch.ditch_matrix[row+i, col-i] > 0 for i in range(4)):
            return True
        return False
