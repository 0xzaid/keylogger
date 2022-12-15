# Python Keylogger

The keylogger captures key presses from the keyboard and writes them to a log file, along with a timestamp for each key press.

The keylogger uses the pynput library to capture key presses from the keyboard, and the queue module to store the key press data in memory before writing it to the log file. This helps reduce the number of writes to the log file, which can improve the performance of the keylogger.

The keylogger also hides the log file by using the attrib command to set the "hidden" attribute for the file. This makes it difficult to locate the log file manually, which can help prevent the keylogger from being detected.

The keylogger uses the datetime module to generate timestamps for each key press, with the format YYYY-MM-DD HH:MM:SS. These timestamps are written to the log file along with the key press data, which can help with analyzing the captured data later.

Overall, the keylogger uses a combination of techniques and optimizations to capture key presses from the keyboard and write them to a log file in a efficient and stealthy manner.