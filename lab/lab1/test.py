import gymnasium as gym

# Create the environment
#env = gym.make("LunarLander-v3", render_mode="human")
#env = gym.make("BipedalWalker-v3", render_mode="human")
env = gym.make("CarRacing-v3", render_mode="human")

# Run for 10 episodes
num_episodes = 100000
for episode in range(num_episodes):
    print(f"Starting Episode {episode + 1}")
    observation, info = env.reset()

    episode_over = False
    total_reward = 0  # To track total reward for the episode
    while not episode_over:
        action = env.action_space.sample()  # Agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        episode_over = terminated or truncated

    print(f"Episode {episode + 1} finished with total reward: {total_reward}")

# Close the environment
env.close()
