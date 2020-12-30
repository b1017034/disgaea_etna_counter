import tkinter as tk
from tkinter import ttk

from const import stairs
import math

common_count = 0
rare_count = 0
legend_count = 0

goal_stairs = stairs.ETNA_COMMON

if __name__ == '__main__':
    def count_common(event):
        global common_count, rare_count, legend_count
        common_count += 1

        common_count_label.configure(text=f"{common_count}")
        goal_common(common_count, rare_count, legend_count)
        goal_common_and_rare(common_count, rare_count, legend_count)

    def count_rare(event):
        global common_count, rare_count, legend_count
        rare_count += 1

        rare_count_label.configure(text=f"{rare_count}")
        goal_common(common_count, rare_count, legend_count)
        goal_common_and_rare(common_count, rare_count, legend_count)

    def count_legend(event):
        global common_count, rare_count, legend_count
        legend_count += 1

        legend_count_label.configure(text=f"{legend_count}")
        goal_common(common_count, rare_count, legend_count)
        goal_common_and_rare(common_count, rare_count, legend_count)

    def goal_common(common, rare, legend):
        now_stairs = goal_stairs - (common * stairs.ITEM_WORLD_COMMON) - (rare * stairs.ITEM_WORLD_RARE) - (legend * stairs.ITEM_WORLD_LEGEND)
        goal_common_count = now_stairs / stairs.ITEM_WORLD_COMMON

        goal_common_only_label.configure(text=f"コモン：{math.ceil(goal_common_count)}個")

    def goal_common_and_rare(common, rare, legend):
        now_stairs = goal_stairs - (common * stairs.ITEM_WORLD_COMMON) - (rare * stairs.ITEM_WORLD_RARE) - (legend * stairs.ITEM_WORLD_LEGEND)
        goal_common_count, goal_rare_count = math.modf(now_stairs / stairs.ITEM_WORLD_RARE)

        goal_common_and_rare_label.configure(text=f"レア；{math.floor(goal_rare_count)}個, コモン：{math.ceil(goal_common_count)}個")

    def refresh(event):
        global common_count, rare_count, legend_count
        common_count = rare_count = legend_count = 0

        common_count_label.configure(text=f"{common_count}")
        rare_count_label.configure(text=f"{rare_count}")
        legend_count_label.configure(text=f"{legend_count}")

        goal_common(common_count, rare_count, legend_count)
        goal_common_and_rare(common_count, rare_count, legend_count)

    root = tk.Tk()
    # Setting Theme
    # s = ttk.Style()
    # s.theme_use('scidgrey')

    # keep front
    root.attributes("-topmost", True)

    root.title("Disgaea Counter")
    root.minsize(width=400, height=140)

    # common
    common_label = ttk.Label(root, text="コモン")
    common_label.grid(column=0, row=0, padx=5, pady=5)

    common_count_label = ttk.Label(root, text=f"{common_count}")
    common_count_label.grid(column=0, row=1, padx=5, pady=5)

    # Count Button
    common_count_button = ttk.Button(text="count", width=10)
    common_count_button.bind("<Button-1>", count_common)
    common_count_button.grid(column=0, row=2, padx=5, pady=5)

    # rare
    rare_label = ttk.Label(root, text="レア")
    rare_label.grid(column=1, row=0, padx=5, pady=5)

    rare_count_label = ttk.Label(root, text=f"{rare_count}")
    rare_count_label.grid(column=1, row=1, padx=5, pady=5)

    # Count Button
    rare_count_button = ttk.Button(text="count", width=10)
    rare_count_button.bind("<Button-1>", count_rare)
    rare_count_button.grid(column=1, row=2, padx=5, pady=5)

    # legend
    legend_label = ttk.Label(root, text="レジェンド")
    legend_label.grid(column=2, row=0, padx=5, pady=5)

    legend_count_label = ttk.Label(root, text=f"{legend_count}")
    legend_count_label.grid(column=2, row=1, padx=5, pady=5)

    legend_count_button = ttk.Button(text="count", width=10)
    legend_count_button.bind("<Button-1>", count_legend)
    legend_count_button.grid(column=2, row=2, padx=5, pady=5)

    # refresh
    refresh_button = ttk.Button(text="refresh", width=10)
    refresh_button.bind("<Button-1>", refresh)
    refresh_button.grid(column=1, row=3, padx=5, pady=5)

    # goal
    goal_title_label = ttk.Label(root, text="コモン装備レベル39まで")
    goal_title_label.grid(column=3, row=0, padx=5, pady=5)
    goal_common_only_label = ttk.Label(root, text="コモン：13個")
    goal_common_only_label.grid(column=3, row=1, padx=5, pady=5)
    goal_common_and_rare_label = ttk.Label(root, text="レア：6個、コモン：1個")
    goal_common_and_rare_label.grid(column=3, row=2, padx=5, pady=5)

    root.mainloop()
