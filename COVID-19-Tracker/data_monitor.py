#!/usr/bin/python3.6

"""
                        --- Core module ---
Schedules data collector and plots graphs based on current data.
Secoundaly, stores data each day for tracking and monitoring spread of virus.

Note:
    For regular annalysis and data storage, use cron scheduler for running script every day
    as the data is regularly updated.
    This can be done automatically with the help of sh script provided - schedule.sh
 
    I Hope the graphs shows positive signs.
                            -- X --
"""

from get_data import current_data, create_csv
from plot_graph import bar_chart, spread_chart

def covid19_monitor():
    create_csv(current_data())
    bar_chart()
    spread_chart()


if __name__ == "__main__":
    covid19_monitor()

