import tkinter as tk
import random
import time

def create_error_window():
    # Create a new Tkinter window
    error_window = tk.Toplevel()
    error_window.title("Idiot_error")
    
    # Set the size and position randomly
    window_width, window_height = 300, 100
    screen_width = error_window.winfo_screenwidth()
    screen_height = error_window.winfo_screenheight()

    # Make the window stay on top of all other windows
    error_window.attributes("-topmost", True)
    
    x_position = random.randint(0, screen_width - window_width)
    y_position = random.randint(0, screen_height - window_height)
    error_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    # Display an error message
    label = tk.Label(error_window, text="An error has occurred", font=("Arial", 12))
    label.pack(pady=20)
    
    # Close event binding to create two more windows on close
    error_window.protocol("WM_DELETE_WINDOW", lambda: on_close(error_window))

def on_close(error_window):
    # Destroy the current window
    error_window.destroy()
    # Create two new error windows
    create_error_window()
    create_error_window()

def create_windows_passively():
    # Create a new error window in the background
    create_error_window()
    # Schedule the next window to open after 2 seconds (2000 milliseconds)
    root.after(2000, create_windows_passively)

# Main Tkinter application
root = tk.Tk()
root.withdraw()  # Hide the main window if not needed

create_error_window()  # Start with the first error window
create_windows_passively()
root.mainloop()
