import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
G = 6.674 * 10e-11
M = 6.42 * 10e23
m = 1000
GMm = G * M * m

h = 10000
e = 1.3
# simulation time, timestep and time
t_max = 500000
dt = 5
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position = np.array([6*10e6 + h, 0, 0]) # These are vector representations of the two (position and velocity)
velocity = np.array([0, e*np.sqrt(G*M/(6*10e6+ h)), 0])
# list of all 3d positions
p_list = []

# Euler integration
for t in t_array:

    # append current state to trajectories
    p_list.append(position)
    scalar_distance_s = position[0]*position[0] + position[1]*position[1] + position[2]*position[2]
    scalar_distance = np.sqrt(scalar_distance_s)
    r_n = position / scalar_distance

    F_scalar = - GMm / (scalar_distance*scalar_distance)
    F = F_scalar * r_n

    # calculate new position and velocity
    a = F / m
    position = position + dt * velocity
    velocity = velocity + dt * a

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)

p_x = np.array([p_list[i][0] for i in range(len(p_list))])
p_y = np.array([p_list[i][1] for i in range(len(p_list))])
p_z = np.array([p_list[i][2] for i in range(len(p_list))])

# plot the position-time graph
plt.title('Euler Method in Orbit')
plt.figure(1)
plt.clf()
plt.xlabel('y')
plt.grid()
#plt.plot(t_array, p_x, label='x (m)')
#plt.plot(t_array, p_y, label='y (m)')
#plt.plot(t_array, p_z, label='z (m)')
plt.plot(p_x, p_y, label='position')
#xplt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
