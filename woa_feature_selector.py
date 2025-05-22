import random
import numpy as np

def fitness_function(feature_subset, feature_importances):
    return sum(f * imp for f, imp in zip(feature_subset, feature_importances))

def optimize_features(features, feature_importances, num_agents=5, max_iter=10):
    num_features = len(features)
    
    # Initialize whale agents randomly
    whales = [np.random.randint(0, 2, num_features).tolist() for _ in range(num_agents)]
    best_whale = whales[0]
    best_score = fitness_function(best_whale, feature_importances)

    for t in range(max_iter):
        a = 2 - t * (2 / max_iter)
        for i in range(num_agents):
            r = random.random()
            A = 2 * a * r - a
            C = 2 * r
            D = [abs(C * bf - w) for bf, w in zip(best_whale, whales[i])]
            new_position = [
                1 if abs(A * d) < 1 else 0
                for d in D
            ]
            score = fitness_function(new_position, feature_importances)
            if score > best_score:
                best_score = score
                best_whale = new_position

    # Select features according to the best whale
    selected_features = [f for f, b in zip(features, best_whale) if b == 1]
    return selected_features
