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
# $ python3 1a.py
#

import matplotlib.pyplot as plt
import math

delta_x = 1
y_values = []

# Ittr though the points to get the y value for each x_0
for x_0 in range(-10,11, delta_x):
    y_values.append(x_0)

plt.plot(range(-10,11, delta_x), y_values, '-o')

plt.xlabel("x")
plt.ylabel("y")
plt.show()
    
