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
# $ pip install matplotlib
#
# Then use python3 to create the graph
# $ python3 1c.py
#

import matplotlib.pyplot as plt
import math

delta_x = 1

def f(x): return float(x**2)

x_values = [j * delta_x for j in range(-int(4/delta_x),int(4/delta_x) +1)]
x_2_y_values = []
for x_0 in x_values:
    x_2_y_values.append(f(x_0))

plt.plot(x_values, x_2_y_values, '-o', label="x^2")

x_2_d2y_values = []
for x_0 in x_values:
    x_2_d2y_values.append((f(x_0 + delta_x) - 2*f(x_0) + f(x_0 - delta_x))/(delta_x**2))

plt.plot(x_values, x_2_d2y_values, '-o', label="d^2y/dx^2 = x^2")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    