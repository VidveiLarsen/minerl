import minerl
import os
import gym
import coloredlogs
import logging
import numpy as np
import tqdm


def test_low_res():
    env = gym.make('MineRLNavigate-v0')

    obs = env.reset()
    env.close()

    assert obs["pov"].shape == (64,64,3)

def test_high_res():
    env = gym.make('MineRLNavigateHighRes-v0')

    obs = env.reset()
    env.close()
    
    assert obs["pov"].shape == (128,256,3)
