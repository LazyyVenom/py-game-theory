import simpy
import random

def customer(env, name, queue):
    print(f"{name} arrives at the queue at {env.now}")
    with queue.request() as req:
        yield req
        print(f"{name} starts being served at {env.now}")
        yield env.timeout(random.uniform(0.5, 1.5))
        print(f"{name} leaves at {env.now}")

def setup(env):
    queue = simpy.Resource(env, capacity=1)
    for i in range(3):
        env.process(customer(env, f'Customer {i}', queue))
        yield env.timeout(0.1)  # Add a delay between each customer arrival

env = simpy.Environment()
env.process(setup(env))
env.run(until=5)  # Run the simulation for 5 time units
