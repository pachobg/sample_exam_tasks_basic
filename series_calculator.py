from math import floor
show_name = input()
number_of_seasons = int(input())
episodes = int(input())
duration = float(input())

ad_duration = duration + duration * 0.2
special_ep_duration = number_of_seasons * 10
all_episodes = number_of_seasons * episodes
total_min = all_episodes * ad_duration + special_ep_duration
print(f"Total time needed to watch the {show_name} series is {floor(total_min)} minutes.")