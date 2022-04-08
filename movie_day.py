time_for_action = int(input())
number_of_scenes = int(input())
scene_duration = int(input())

area_preparing = time_for_action * 0.15
time_for_all_scenes = number_of_scenes * scene_duration
time_for_all_movie = area_preparing + time_for_all_scenes
difference = abs(time_for_action - time_for_all_movie)
if time_for_action >= time_for_all_movie:
    print(f"You managed to finish the movie on time! You have {difference:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference:.0f} minutes.")
