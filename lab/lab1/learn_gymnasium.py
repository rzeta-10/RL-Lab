# gymnasium env == high level py class representing
#                  a markov decision provess

import gymnasium as gym
env = gym.make('Walker2d-v5', render_mode="human") #render_mode == how the env should be visualized
# render_mode = "rgb_array" , "ansi"

obs, info = env.reset()

episode_over = 10000000000
while episode_over:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()
    episode_over = episode_over - 1

env.close()
gym.pprint_registry() # pretty prints all env in registry

