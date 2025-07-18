import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from plotting.utils import prepare_planets_by_house


def draw_south_indian_chart(chart):
    planets_by_house = prepare_planets_by_house(chart)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.axis("off")

    # Draw 4x4 grid with house numbering clockwise from top left (starting with 1 at top left)
    positions = [
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 2),
        (3, 1),
        (3, 0),
        (2, 0),
        (1, 0),
        (0, 0),
        (0, 1),
        (0, 2),
    ]

    for i, (x, y) in enumerate(positions):
        house_num = str(i + 1)
        ax.add_patch(Rectangle((x, y), 1, 1, fill=False, edgecolor="black"))
        ax.text(x + 0.5, y + 0.8, house_num, ha="center", va="center", fontsize=8, color="gray")
        planets = planets_by_house[house_num]
        for j, planet in enumerate(planets):
            ax.text(x + 0.5, y + 0.6 - 0.2 * j, planet, ha="center", va="center", fontsize=9)

    plt.title("South Indian Style Chart")
    plt.tight_layout()
    return fig
