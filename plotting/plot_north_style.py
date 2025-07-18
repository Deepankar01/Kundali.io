import matplotlib.pyplot as plt
from plotting.utils import prepare_planets_by_house


def draw_north_indian_chart(chart):
    planets_by_house = prepare_planets_by_house(chart)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Draw diamond structure
    center = (5, 5)
    corners = [(5, 9.5), (9.5, 5), (5, 0.5), (0.5, 5)]  # Top  # Right  # Bottom  # Left
    inner = [(7.5, 7.5), (7.5, 2.5), (2.5, 2.5), (2.5, 7.5)]
    # Outer box
    diamond = [
        corners[0],
        inner[0],
        corners[1],
        inner[1],
        corners[2],
        inner[2],
        corners[3],
        inner[3],
        corners[0],
    ]
    ax.plot(*zip(*diamond), color="black")

    # House positions (clockwise from top center)
    house_centers = [
        (5, 9),
        (7.5, 7.5),
        (9, 5),
        (7.5, 2.5),
        (5, 1),
        (2.5, 2.5),
        (1, 5),
        (2.5, 7.5),
        (5, 7),
        (7, 5),
        (5, 3),
        (3, 5),
    ]

    for i, (x, y) in enumerate(house_centers):
        house_num = str(i + 1)
        ax.text(x, y + 0.3, house_num, ha="center", va="center", fontsize=8, color="gray")
        planets = planets_by_house[house_num]
        for j, planet in enumerate(planets):
            ax.text(x, y - 0.2 * j, planet, ha="center", va="center", fontsize=9)

    plt.title("North Indian Style Chart")
    plt.tight_layout()
    return fig
