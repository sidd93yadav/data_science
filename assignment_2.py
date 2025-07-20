# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 11:38:26 2025

@author: Sidd Yadav
"""
import random
import numpy as np
import matplotlib.pyplot as plt



# Basic Probability
#1.
#----Part A: Tossing a coin 10,000 time
def simulate_coin_tosses(trials=10000):
    heads=0
    tails=0
    
    for _ in range (trials):
        toss = random.choice(['H','T'])
        if toss == 'H':
            heads+=1
        else:
            tails+=1
        
    prob_heads = heads / trials
    prob_tails = tails / trials
    
    print("----Coin Toss Simulation -----")
    print(f"Total Tosses:{trials}")
    print(f"Heads: {heads} , Tails:{tails}")
    print(f"Experimental Probability of Heads : {prob_heads:.4f}")
    print(f"Experimental Probability of Tails : {prob_tails:.4f}")
    print()
    
#---Part B : Rolling two dice and checking for sum = 7 ---
def simulate_dice_rolls(trials=10000):
    sum_seven_count = 0
    
    for _ in range(trials):
        die1 = random.randint(1,6 )
        die2 = random.randint(1, 6)
        if die1 +  die2 == 7:
            sum_seven_count += 1
            
    prob_sum_seven = sum_seven_count/trials
    
    
    print("---Dice Roll simulation ---")
    print(f"Total Rolls: {trials}")
    print(f"Number of times sum was 7: {sum_seven_count}")
    print(f"Experimental Probability of Sum = 7: {prob_sum_seven:.4f}")
    
    
#Run simulation 
simulate_coin_tosses()
simulate_dice_rolls()
 
# 2.
def estimate_prob_at_least_one_six(trials=10000):
    success_count = 0
    
    for _ in range(trials):
        found_six = False
        for _ in range(10):
            if random.randint(1,6) == 6:
                found_six = True
                break
            
        if found_six:
            success_count +=1
    probability = success_count / trials
    print(f"Out of {trials} trials, at least one '6' occured {success_count} times.")
    print(f"Estimated probability of at least one '6' in 10 rolls : {probability:.4f}")             

#Run the Function
estimate_prob_at_least_one_six()




#Conditional Probability and Bayes' Theorem
#3.

def simulate_draws(trials=1000):
    colors  = ['Red'] * 5 + ['Green'] * 7 + ['Blue'] * 8 
    draws =[]
    
    #Perform 1000 draws with replacement 
    for _ in range(trials):
        draws.append(random.choice(colors))
        
    return draws 
simulate_draws()
def analyze_draws(draws):
    total_transitions =0
    red_given_blue = 0
    
    red_count= 0
    blue_count = 0
    blue_given_red = 0
    for i  in range(1,len(draws)):
        prev = draws[i-1]
        curr = draws[i]
        
        if prev == 'Blue':
            total_transitions +=1
            if curr == 'Red':
                red_given_blue +=1 
                
        if curr =='Red':
            red_count +=1 
            if prev == 'Blue':
                pass
            elif prev == 'Red' or prev == 'Green':
                pass
            if curr == 'Blue':
                blue_count += 1 
                if prev == 'Red':
                    blue_given_red += 1 
        
        P_R = red_count / len(draws)
        P_B = blue_count / len(draws)
        P_R_given_B = red_given_blue / total_transitions if total_transitions else 0
        P_B_given_R = blue_given_red / red_count if red_count else 0

        bayes_estimate = (P_B_given_R * P_R) / P_B if P_B else 0
        print("---- Simulation Summary ----")
        print(f"Total Draws: {len(draws)}")
        print(f"P(Red | Blue): {P_R_given_B:.4f} (Simulated)")
        print(f"P(Blue | Red): {P_B_given_R:.4f}")
        print(f"P(Red): {P_R:.4f}")
        print(f"P(Blue): {P_B:.4f}")
        print(f"Bayes’ Theorem Estimate of P(Red | Blue): {bayes_estimate:.4f}")

draws = simulate_draws(1000)
analyze_draws(draws)


#Random Variables and Discrete Probability
#4.
values =  [1,2,3]
probabilities = [0.25,0.35,0.40]

sample = np.random.choice(values, size=1000, p=probabilities)


mean = np.mean(sample)
variance = np.var(sample)
std_dev = np.std(sample)
print("---- Empirical Statistics from Sample ----")
print(f"Sample Size: {len(sample)}")
print(f"Empirical Mean: {mean:.4f}")
print(f"Empirical Variance: {variance:.4f}")
print(f"Empirical Standard Deviation: {std_dev:.4f}")


#Continuous Random Variables
#5.

np.random.seed(42)

mean = 5
scale = mean
sample_size = 2000

    
samples = np.random.exponential(scale=scale, size=sample_size)

plt.figure(figsize=(10, 6))
plt.hist(samples, bins=40, stat='density', color='skyblue', label='Histogram', kde=False)

x = np.linspace(0, max(samples), 1000)
pdf = (1/scale) * np.exp(-x/scale)
plt.plot(x, pdf, color='red', linewidth=2, label='Exponential PDF')

plt.title("Exponential Distribution (Mean = 5)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()




#Central Limit Theorem
#6.

population = np.random.uniform(low=0.0, high=1.0, size=10000)


sample_means = []
n = 30


for _ in range(1000):
    sample = np.random.choice(population, size=n, replace=True)
    sample_means.append(np.mean(sample))



plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(population, bins=40, color='skyblue', density=True, edgecolor='black')
plt.title("Original Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)


plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=40, color='salmon', density=True, edgecolor='black')
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.grid(True)

plt.tight_layout()
plt.show()





