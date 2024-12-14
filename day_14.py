import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


with open('input/day_14.txt') as f:
    patrols = [tuple(map(int, re.findall(r'\-?\d+', l))) for l in f.read().splitlines()]
X_LIMIT, Y_LIMIT = 101, 103

def part1(seconds=100):
    new_pos = [((px + vx * seconds) % X_LIMIT, (py + vy * seconds) % Y_LIMIT) for px, py, vx, vy in patrols]
    uniq_pos = set(new_pos)
    return sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x < X_LIMIT//2 and y < Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x < X_LIMIT//2 and y > Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x > X_LIMIT//2 and y < Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x > X_LIMIT//2 and y > Y_LIMIT//2])

def part2(seconds=10000):
    states = []
    variances = []
    # Prepare states
    for s in range(seconds):
        state = np.zeros((Y_LIMIT, X_LIMIT))
        positions = [((px + vx * s) % X_LIMIT, (py + vy * s) % Y_LIMIT) for px, py, vx, vy in patrols]
        for (x, y) in positions:
            state[y, x] = 1
        states.append(state)
        variances.append(np.var(positions))
    min_var = min(variances)
    print(f'Point of interest at frame: {variances.index(min_var)}')

    # Set up the figure and axis
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)  # Adjust the plot to make room for the slider
    cax = ax.imshow(states[0], cmap='gray', interpolation='nearest')
    # Slider setup
    ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])  # Position of the slider
    slider = Slider(ax_slider, 'Frame', 0, seconds - 1, valinit=0, valstep=1)
    def slider_update(val):
        frame = int(val)
        cax.set_array(states[frame])
        fig.canvas.draw_idle()  # Redraw the figure
    slider.on_changed(slider_update)
    def on_key(event):
        current_value = slider.val
        if event.key == 'right':
            new_value = min(current_value + 1, seconds - 1)
            slider.set_val(new_value)
        elif event.key == 'left':
            new_value = max(current_value - 1, 0)
            slider.set_val(new_value)
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()

# Part 1
part1_answer = part1(seconds=100)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = part2(seconds=10000)
print(f'Part 2: {part2_answer}')