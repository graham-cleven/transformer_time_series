#!/usr/bin/env python3

import numpy as np
import random


def geometric_brownian_motion(T, N, mu, sigma, S0):
    dt = T / N
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)  ### standard brownian motion ###
    X = (mu - 0.5 * sigma**2) * t + sigma * W
    S = S0 * np.exp(X)  ### geometric brownian motion ###
    return S


# T = 1
# N = 252
# mu = 0.15
# sigma = 0.2
# S0 = 100
# S = geometric_brownian_motion(T, N, mu, sigma, S0)
# print(S)


def brownian_motion(n):
    # Initialize the list with the first value
    motion = [0]
    for i in range(1, n):
        # Generate a random number between -1 and 1
        dx = random.uniform(-1, 1)
        # Add the random number to the previous value in the list
        motion.append(motion[i - 1] + dx)
    return motion
