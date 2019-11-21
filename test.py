import gym
import numpy as np

env = gym.make('gym_finger:Finger-v0')
i = 0
while True:
    idx = i % 3
    applied_action = np.zeros(3)
    observation = env.reset()
    env.setRealTimeSimulation()
    print(env.action_space.low[idx], env.action_space.high[idx])
    input("Start")
    for action in range(10):
        applied_action[idx] = env.action_space.high[idx] / 10
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    input("+ve end")
    for action in range(10):
        applied_action[idx] = - env.action_space.high[idx] / 10
        print(applied_action)
        _,_,_,_ = env.step(applied_action)


    input("Middle")
    for action in range(10):
        applied_action[idx] = env.action_space.low[idx] / 10
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    input("-ve End")
    for action in range(10):
        applied_action[idx] = - env.action_space.low[idx] / 10
        print(applied_action)
        _,_,_,_ = env.step(applied_action)

    i += 1
