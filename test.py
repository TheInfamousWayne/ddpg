import gym
import numpy as np

env = gym.make('gym_finger:Finger-v0')
observation = env.reset()
i = 0
while True:
    idx = i % 3
    applied_action = np.zeros(3)
    for action in np.linspace(env.action_space.low[idx], env.action_space.high[idx], 10):
        applied_action[idx] += action
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    for action in np.linspace(env.action_space.high[idx], env.action_space.low[idx], 10):
        applied_action[idx] += action
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    for action in np.linspace(env.action_space.high[idx], env.action_space.low[idx], 10):
        applied_action[idx] += action
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    for action in np.linspace(env.action_space.low[idx], env.action_space.high[idx], 10):
        applied_action[idx] += action
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    i += 1
    if i%5 == 0:
        input("")

