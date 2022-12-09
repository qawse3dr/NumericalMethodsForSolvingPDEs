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
# $ python3 1b.py
#

import matplotlib.pyplot as plt
import math

delta_x = [(math.pi/2, "pi/2"), (math.pi/4, "pi/4")]


for dx in delta_x:
    y_values = []
    x_values = [j * dx[0] for j in range(-int(2*math.pi/dx[0]),int(2*math.pi/dx[0]))]
    # Ittr though the points to get the y value for each x_0
    for x_0 in x_values:
        y_values.append(math.sin(x_0))

    plt.plot(x_values, y_values, '-o', label=dx[1])

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    
