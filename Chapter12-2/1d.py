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
# $ python3 1d.py
#

import matplotlib.pyplot as plt
import math

delta_x = math.pi/8

x_values = [j * delta_x for j in range(-int(2*math.pi/delta_x),int(2*math.pi/delta_x))]
cos_y_values = []
for x_0 in x_values:
    cos_y_values.append(math.cos(x_0))

plt.plot(x_values, cos_y_values, '-o', label="cos(x)")

cos_dy_values = []
for x_0 in x_values:
    cos_dy_values.append((math.cos(x_0 + delta_x) - math.cos(x_0 - delta_x))/(2*delta_x))

plt.plot(x_values, cos_dy_values, '-o', label="dy/dx = cos(x)")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    