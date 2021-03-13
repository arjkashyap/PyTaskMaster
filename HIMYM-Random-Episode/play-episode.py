"""
Play random episode from How I met your Mother 
Any Season
Any episode
"""

import os
import random
import pickle
import vlc
import time

# Path to all seasons folder 
PATH = "E:/Series/How-I-met-your-mother"
pickle_path = "./episodes"
TOTAL_EPISODES = 208
DURATION = 1260

def create_pickle(path):
	"""
		Function takes the absolute path of all HIMYM episodes in 
		the format
		It does not matter what/how you name your episodes or seasons
		- path
		    - season 1
		        - episode 1
		        - episode 2
		        .
		        .
		        .
		    - season 2
		    - season 3
		    .
		    .
		It generates a pickle file of episode index (starting from 0)
		and the absolute path of the video file

	"""
	index = 0
	dct = {}

	# scan all sub folders and store episode paths in dict
	seasons = os.listdir(path)
	for season in seasons:
		print(season)
		season_path = os.path.join(path, season)
		episodes = os.listdir(season_path)
		for episode in episodes:
			episode_path = os.path.join(season_path, episode)
			dct[index] = episode_path
			index += 1

	# store dict in current folder
	try:
		pickle.dump(dct, open("episodes", "wb"))
		print("Pickle File created")
	except:
		print("Something went wrong. Checkout Readme.md")

def read_pickle(pickle_path = "./episodes", index=0):
	dct = pickle.load(open(pickle_path, "rb"))
	episode_path = dct[index]
	TOTAL_EPISODES = len(dct)
	print("---")
	return episode_path



def play_video(video_path):
	"""
		Function runs the video in vlc media player
	"""
	try:
		media = vlc.MediaPlayer(video_path)
		media.play()
		time.sleep(DURATION)
	   
	except Exception as e:
		print("Terminated")
		print(e)

def main():
	print("Ba baa baaa baa")
	#print(os.listdir(path))
	total_episodes = 0
	if(os.path.exists(pickle_path)):
		print("file is already there")
		read_pickle()
	else:
		create_pickle(PATH)
	random_episode_index = random.randint(0, TOTAL_EPISODES)
	random_episode_path = read_pickle(pickle_path, random_episode_index)
	print("Playing episode ", random_episode_path)

	play_video(random_episode_path)

	

if __name__ == "__main__":
	main()