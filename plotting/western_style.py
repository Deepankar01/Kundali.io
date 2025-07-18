import matplotlib.pyplot as plt
import numpy as np

from plotting.utils import prepare_planets_by_house


def draw_western_circular_chart(chart):
    planets_by_house = prepare_planets_by_house(chart)
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
    ax.set_theta_zero_location("E")
    ax.set_theta_direction(-1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Western Circular Chart", va="bottom")

    # Each house covers 30 degrees
    for i in range(12):
        theta1 = np.deg2rad(i * 30)
        theta2 = np.deg2rad((i + 1) * 30)
        ax.bar(
            x=theta1, height=1, width=theta2 - theta1, bottom=0.5, color="white", edgecolor="black"
        )

        # Place house number
        mid_angle = (theta1 + theta2) / 2
        ax.text(mid_angle, 1.35, str(i + 1), ha="center", va="center", fontsize=9, color="gray")

    # Plot planets in respective houses
    for house_num, planets in planets_by_house.items():
        index = int(house_num) - 1
        angle = np.deg2rad(index * 30 + 15)  # Middle of the house
        for j, planet in enumerate(planets):
            radius = 1 - 0.05 * j
            ax.text(angle, radius, planet, ha="center", va="center", fontsize=9)

    return fig
