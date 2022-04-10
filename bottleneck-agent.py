import gym
import highway_env

import pprint

env = gym.make('bottleneck-v0')
pprint.pprint(env.config)

env.reset()
done = False
while not done:
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())

env.close()
