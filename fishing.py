import sys
import time
import os

import keyboard
import pyautogui

def main():
    # Path to the screenshot used for detecting a bite.
    image_path = 'splash.png' 

    # Key to terminate the program. Change this to any key you prefer.
    exit_button = 'F12' 

    # Time interval (in seconds) for checking the fishing bobber splash. Lower values are better for enchants.
    check_time = 0.025 
    
    # Check if the screenshot file exists.
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        sys.exit(1)

    # Message when program starts correctly
    print(f"Image loaded. Press {exit_button} to quit the program.")

    # Main loop to continuously check for the fishing bobber splash.
    while True:
        
        # Check if the exit button is pressed. If so, terminate the program.
        if keyboard.is_pressed(exit_button):
            print(f"{exit_button} pressed. Exiting the program.")
            sys.exit(0)  

        try:
            # Check for a bite using the screenshot.
            loc = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.8)
            
            # If there was a bite
            if loc:
          
                pyautogui.click(loc, button='right') # Pull up the fishing rod.
                
                time.sleep(1) # Short delay before casting again.
                
                pyautogui.click(button='right') # Cast the fishing rod.
                
                time.sleep(1) # Wait for a moment before next action.
                
        except pyautogui.ImageNotFoundException:
            pass # Ignore if the splash image is not found on the screen.
        
        except Exception as e:
            print(f"An exception occurred: {e}") # Catch and display any other exceptions that occur.

        # Wait for the check time before checking again.
        time.sleep(check_time)

if __name__ == "__main__":
    main()