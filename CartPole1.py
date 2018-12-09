import gym
import numpy as np

def run_episode(env, parameters):
	observation = env.reset()
	totalreward = 0
	#for 200 timesteps
	for _ in xrange(2000):
		env.render()
		#initalize random weights
		action = 0 if np.matmul(parameters, observation)<0 else 1
		observation, reward, done, info = env.step(action)
		totalreward += reward
		if done:
			break
	return totalreward

#hill climbing algo training
def train(submit):
	env = gym.make('CartPole-v0')

	episodes_per_update = 5
	noise_scaling = 0.1
	parameters = np.random.rand(4) * 2 -1
	bestreward = 0

	#2000 episodes
	for i in range(2000):
		newparams = parameters + (np.random.rand(4) *2 -1) * noise_scaling
		reward = run_episode(env, newparams)
		print "---------------------------- EPISODE : %d ----------------------------" % int(i+1)
		print "Episode reward	: %d" % reward
		print "Best reward   	: %d" % bestreward 
		if reward >= bestreward: 
			bestreward = reward
			parameters = newparams
	print "========================== TRAINING FINISHED =========================="
	return parameters


#hill climbing algo training
def run(parameters):
	env = gym.make('CartPole-v0')
	episodes_per_update = 5

	print "---------------------------- RUN ----------------------------"

	while(1):
	
		observation = env.reset()
		totalreward = 0
		#for 200 timesteps
		for _ in xrange(200):
			env.render()
			#initalize random weights
			action = 0 if np.matmul(parameters, observation)<0 else 1
			observation, reward, done, info = env.step(action)
			if done:
				break





good_params = train(submit=False)
r = run(good_params)

