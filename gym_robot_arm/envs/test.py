#test.py

#
import gym 
from robot_arm_env import RobotArmEnvV2

#env = gym.make('gym_robot_arm:robot-arm-v1')
env = RobotArmEnvV2(num_links=4, link_length=50)
for i_episode in range(20):
    observation = env.reset()
    for t in range(10):
        env.render()
        print(observation, end=', reward: ')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(round(reward))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()