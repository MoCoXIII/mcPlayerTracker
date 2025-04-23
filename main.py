import time
import keyboard

# main.py

# Initial values
# probable radius of the area to search in blocks
b = 100
a = b // (-2)
x, y, z = a, a, a
dx, dy, dz = b, b, b
precision_threshold = 1

selector = ""

def get_selector(x, y, z, dx, dy, dz):
    return f"@a[x={x},y={y},z={z},dx={dx},dy={dy},dz={dz}]"

def main():
    global x, y, z, dx, dy, dz, selector, b, a

    print("Press 's' to start.")
    keyboard.wait('s', suppress=True)  # Wait for the start keybind
    print("Started. Listening for confirm ('c') or deny ('d') keybinds.")

    axis_order = ['x', 'z', 'y']  # Order of axes to refine
    current_axis_index = 0

    inMainArea = False

    while True:
        selector = get_selector(x, y, z, dx, dy, dz)
        print(f"Current selector: {selector}")
        keyboard.write(f"/msg @s {selector}")
        time.sleep(0.5)
        keyboard.send('enter')  # Send the command in Minecraft
        time.sleep(0.5)
        keyboard.send('t') # Open chat to see the message

        event = None
        while event is None or event.name not in ['c', 'd', 'q']:
            event = keyboard.read_event(suppress=True)  # Read keyboard events
            print(f"{event.name}", end="\r")
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'c':  # Confirm keybind
                if not inMainArea:
                    inMainArea = True
                # print("Confirmed. Moving closer.")
                if axis_order[current_axis_index] == 'x':
                    dx //= 2
                elif axis_order[current_axis_index] == 'z':
                    dz //= 2
                elif axis_order[current_axis_index] == 'y':
                    dy //= 2
            elif event.name == 'd':  # Deny keybind
                if not inMainArea:
                    print('Expanding search area.')
                    b *= 10
                    a = b // (-2)
                    x, y, z = a, a, a
                    dx, dy, dz = b, b, b
                    continue
                # print("Denied. Moving back.")
                if axis_order[current_axis_index] == 'x':
                    x += dx
                elif axis_order[current_axis_index] == 'z':
                    z += dz
                elif axis_order[current_axis_index] == 'y':
                    y += dy
            elif event.name == 'q':  # Quit keybind
                print("Quitting.")
                break

        # Check for convergence on the current axis
        # print(f"Current axis: {axis_order[current_axis_index]}")
        if axis_order[current_axis_index] == 'x' and dx < precision_threshold:
            dx = precision_threshold
            current_axis_index += 1
        elif axis_order[current_axis_index] == 'z' and dz < precision_threshold:
            dz = precision_threshold
            current_axis_index += 1
        elif axis_order[current_axis_index] == 'y' and dy < precision_threshold:
            dy = precision_threshold
            current_axis_index += 1

        # If all axes are refined, we are done
        if current_axis_index >= len(axis_order):
            print(f"Converged to location: x={x}, y={y}, z={z}")
            break

        # Wait a second before trying again
        time.sleep(1)

if __name__ == "__main__":
    main()
