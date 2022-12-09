#!/usr/bin/python3

#
# (C) Copyright 2022 Larry Milne (https://www.larrycloud.ca)
#
# This code is distributed on "AS IS" BASIS,
# WITHOUT WARRANTINES OR CONDITIONS OF ANY KIND.
# See the License for the specific language governing permissions and
# limitations under the License.
# @author: qawse3dr a.k.a Larry Milne
#

# To run this example install
# matplotlib using pip
# $pip install matplotlib
#
# Then use python3 to create the graph
# $python3 homogenous_heat_equation.py
#
# Feel free to tune the parameters before creating graphs
# The default graph is a homogenous heat equation with a
# BC: Homogenous Dirichlet 
# IC:  f(x) = 1
# Length: 1
#

import matplotlib.pyplot as plt
import math

# Length of Rod for
# f(x) = C or x -> L = 1 is recommended
# f(x) = sin(x) -> L = math.pi is recommended
length = 1

k = 1
delta_x = 0.01
delta_t = delta_x**2/(4*k)

# how many itterations  of time should we do
# Max will become time_ittr * delta_t
# for f(x) = C or x -> 100 is recommended
# for f(x) = math.sin(x) -> 2500 is recommended
time_ittr = 100000
# How man itterations should be displayed
# This must be <= time_itter
# Recommended is about 5-10 for best results
# This won't always be exact depending on time_itter/time_itter_displayed
time_itter_displayed = 10

# IC
def f(x):
    return math.log(x)

# Boundry condition from u(0,t)
def BC_1(t):
    return t**2

# Boundry condition for u(l,t)
def BC_2(t):
    return t + 1

def Q(x,t):
    return 2 *x + 1 + t



# values for our IC (1-d arrays)
x_values = []
IC_t_values = []

# Solve for s once to save compute
s = k* delta_t/(delta_x**2)

# 2-d array of values for t
forward_diff_t_values = []

# Find our initial distribution
x_values.append(0)
IC_t_values.append(BC_1(0))
for j in range(1, int(length/delta_x)):
    x_values.append(delta_x*j)
    IC_t_values.append(f(delta_x*j))
x_values.append(length)
IC_t_values.append(BC_2(0))

prev_U = IC_t_values
for m in range(1, time_ittr):
    forward_diff_t_values.append([])
    forward_diff_t_values[-1].append(BC_1(m*delta_t))
    for j in range(1, int(length/delta_x)):
        u = prev_U[j] + s * (prev_U[j+1] - 2 * prev_U[j] + prev_U[j-1]) + delta_t * Q(j*delta_x, m*delta_t)
        forward_diff_t_values[-1].append(u)
    forward_diff_t_values[-1].append(BC_2(m*delta_t))
    prev_U = forward_diff_t_values[-1] #prob shouldn't do a copy


display_format = '-'
# plot ic
plt.plot(x_values,IC_t_values, display_format, label="IC")

# plot other times
for p in range(0, len(forward_diff_t_values), int(time_ittr/ time_itter_displayed)):
    plt.plot(x_values, forward_diff_t_values[p], display_format,  label = f"t = {(p+1)*delta_t}")

plt.legend()
plt.xlabel("x")
plt.ylabel("u(x,t)")

plt.xlim([0,length])


# ylim for unstable example
# plt.ylim([-10, 10])
plt.show()