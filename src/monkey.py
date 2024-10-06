import pygame
import time
import threading
import numpy as np

class Monkey(pygame.sprite.Sprite):

    def __init__(self, width, height, location):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        self.image = pygame.image.load("./assets/apina.png")
        self.resized_image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.resized_image.get_rect()
        self.rect.left, self.rect.top = location

        self.current_index = None
        self.font = pygame.font.SysFont(None, 24)  # Set up the font for rendering text

        self.kaivuu_kahva = None
        self.apina_kaivaa = False
        self.ditch = None

    def draw(self, screen):
        # Draw the monkey image
        screen.blit(self.resized_image, self.rect)

        # Create the text surface for the current index
        if self.current_index is not None:
            index_text = f"Index: {self.current_index}"
            text_surface = self.font.render(index_text, True, (255, 255, 255))  # White text color
            text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Position below the monkey
            screen.blit(text_surface, text_rect)

    def dig(self, Ditch):
        self.apina_kaivaa = True
        self.time_to_dig = 1  # Time in seconds between digs
        self.stamina_multiplier = 2  # Example of a stamina multiplier

        print("Initial ditch matrix:")
        print(Ditch.ditch_matrix)

        for i in range(100):  # Repeat the digging process 5 times
            time.sleep(self.time_to_dig)  # Wait for the specified digging time

            # Find the indices of the last four '1's
            indices = np.argwhere(Ditch.ditch_matrix == 1)  # Get indices of all '1's

            if len(indices) >= 4:  # Ensure there are at least four '1's to change
                # Get the last four indices
                last_four_indices = indices[-4:]  # Get the last four positions

                # Change the values at these indices to 0
                for row, col in last_four_indices:
                    Ditch.ditch_matrix[row, col] = 0

                print(f"Digging at positions: {last_four_indices.tolist()}")  # Print the positions dug
                
                # You might want to update the current index here if necessary
                self.current_index = (last_four_indices[-1][0], last_four_indices[-1][1])

            else:
                print("Not enough '1's to dig. Stopping digging.")
                break  # Exit if there are fewer than 4 '1's

        print("Updated ditch matrix:")
        print(Ditch.ditch_matrix)
            


    def move_to_last(self, Ditch):
        """Move the monkey to the target position incrementally."""
        self.ditch = self.get_last_ditch_position(Ditch)
        self.target_location, self.current_index = self.ditch
        # Calculate the total distance to move in x and y directions
        delta_x = self.target_location[0] - self.rect.x
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




    def get_first_ditch_position(self, ditch):
        """Find the first available '1' in the ditch matrix and return its position."""
        for row in range(ditch.ditch_matrix.shape[0]):
            for col in range(ditch.ditch_matrix.shape[1]):
                if ditch.ditch_matrix[row, col] == 1:  # Find the first 1
                    # Calculate world coordinates of the matrix position
                    x = ditch.rect.x + col * ditch.ppu
                    y = ditch.rect.y + row * ditch.ppu
                    print("First ditch pos: ", x,y)
                    return (x, y)
        return None  # If no position is founds 
    
    def get_last_ditch_position(self, ditch):
        """Find the last available '1' in the ditch matrix and return its position and matrix index."""
        # Reverse iteration: Start from the last row and last column
        for row in range(ditch.ditch_matrix.shape[0] - 1, -1, -1):
            for col in range(ditch.ditch_matrix.shape[1] - 1, -1, -1):
                if ditch.ditch_matrix[row, col] == 1:  # Find the last 1
                    # Calculate world coordinates of the matrix position
                    x = ditch.rect.x + col * ditch.ppu
                    y = ditch.rect.y + row * ditch.ppu
                    print("Last ditch pos: ", x, y)
                    return (x, y), (row, col)  # Return both position and matrix index
        return None, None  # If no position is found
