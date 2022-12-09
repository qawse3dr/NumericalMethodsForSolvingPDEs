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
from matplotlib import animation
import math

'''
This will represent a heat equation PDE with Dirichlet Boundary conditions
'''
class HomogenousDirichletHeatEquation:
    def __init__(self, delta_x, delta_t, display_time_int, k = 1, IC = lambda x: 1, BC_1 = 0, BC_2 = 0, length = 1):
        '''
        :param delta_x: the delta x that will be used when approximating the PDE
        :param delta_t: the delta time that will be used when approximating the PDE
        :param display_time_int: The interval that in which the display is 
                                 updated in time delta_t should fit equally into this
        :param k: k value of heat equation
        :param IC: IC of the heat equation this should be a function
        :param BC_1: Dirichlet BC at length 0
        :param BC_1: Dirichlet BC at length 1
        :param length: Length of the rod
        '''
        # Runtime vars
        self.paused = False
        self.t_ittr = 0 # Current time
        self.x_plots = [] # x values for all plots this will always be the same
        self.plots = [] # Currently rendered plots
        
        # Setup vars
        self.IC = IC
        self.length = length
        self.BC_1 = BC_1
        self.BC_2 = BC_2
        self.k = 1

        # Graph parameter vars
        self.delta_x = delta_x
        self.delta_t = delta_t
        self.time_itter_displayed = display_time_int
        self.s = self.k* self.delta_t/(self.delta_x**2) # Solve for s once to save compute
        
        # Graph
        self.ax = plt.axes(xlim=(0, length), ylim=(-0.25,1.5))
        self.line, = self.ax.plot([], [], lw=2)
        
    def get_first_frame(self):
        # Find our initial distribution
        self.plots = [[]]
        self.t_ittr = 0
        self.x_plots.append(0)
        self.plots[0].append(self.BC_1)
        for j in range(1, int(self.length/self.delta_x)):
            self.x_plots.append(self.delta_x*j)
            self.plots[0].append(self.f(self.delta_x*j))
        self.x_plots.append(self.length)
        self.plots[0].append(self.BC_2)
        
        return self.frame(0)

    def get_next_frame(self):
        self.t_ittr += 1
        # Check if we haven't calculated this frame yet
        if self.t_ittr  >= len(self.plots):
            # Calculate next frame
            time = self.t_ittr * self.time_itter_displayed
            end_time = (1+self.t_ittr) * self.time_itter_displayed
            
            # the new graph will be generated from the prev PDE
            prev_PDE = self.plots[-1]
            
            # run the iterations will we hit the desired time
            while (time < end_time):
                # First value will always be the BC_1 (because Dirichlet BC's that don't depend on time)
                forward_diff_t_values = [self.BC_1]
                for j in range(1, int(self.length/self.delta_x)):
                    u = prev_PDE[j] + self.s * (prev_PDE[j+1] - 2 * prev_PDE[j] + prev_PDE[j-1])
                    forward_diff_t_values.append(u)
                
                # Last value will always be the BC_2 (because Dirichlet BC's that don't depend on time)
                forward_diff_t_values.append(self.BC_2) 
                
                # Set the prev_PDE  to the new value
                prev_PDE = forward_diff_t_values
                
                # Move time by delta_t
                time += self.delta_t
            
            # Set the prev_PDE to be our newest Ittr of the frame
            self.plots.append(prev_PDE)
        
        # increment the frame by one
        return self.frame(self.t_ittr)
    
    def frame(self ,t):
        self.line.set_data(self.x_plots, self.plots[t])
        return self.line,
    def get_data_as_tuple(self, t):
        return (self.x_plots, self.plots[t])
    def get_last_data_as_tuple(self):
        return self.get_data_as_tuple(self.t_ittr)
    def f(self, x):
        return self.IC(x)


'''
OnClick for allowing you to control the graphs made
by matplotlib. You can safely ignore this code
as it doesn't really teach you much about math but
makes it easier to pause and play the graph
'''
def on_press(event):
    # Pause graph if space bar is pressed 
    if event.key.isspace():
        if pde.paused: anim.resume()
        else: anim.pause()        
        pde.paused ^= True
            
pde = None
def init():
    global pde
    # Under here will be all the different example PDE's we use in the book
    
    # Example 3 in the textbook part 1
    # pde = HomogenousDirichletHeatEquation(delta_x= 0.2, delta_t= 0.01, display_time_int = 0.01)
    
    # Answer to FFYT 1 This should be done by hand in FYTT
    # pde = HomogenousDirichletHeatEquation(delta_x=0.2, delta_t=0.01, display_time_int = 0.01, IC= lambda x: x)
    
    # Answer to FFYT 2
    pde = HomogenousDirichletHeatEquation(delta_x=0.1, delta_t=0.0025, display_time_int = 0.25, IC= lambda x: math.sin(x), length=math.pi)
    
    
    
    # Unable heat equation
    #pde = HomogenousDirichletHeatEquation(delta_x=0.1, delta_t=1, display_time_int = 1, IC= lambda x: 1)
    
    # stable heat equation
    #pde = HomogenousDirichletHeatEquation(delta_x=0.1, delta_t=0.0025, display_time_int = 0.1, IC= lambda x: 1)
def animate(t):
    val = pde.get_first_frame() if (len(pde.plots) == 0)  else pde.get_next_frame()
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.legend([f"t = {round((t)*pde.time_itter_displayed,5)}"])
    return  val


# If set to true it will show an animation of the pde
# if set to falls it will create a static image
use_animation = False

# If the animation should be saved and the filename
save_animation = False
save_name = "Plot.mp4"

if use_animation:
    # How the animation should be played
    frames = 3
    frame_time = 1000 # in ms
    fig = plt.figure()
    fig.canvas.mpl_connect('key_press_event', on_press)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=frames, interval=frame_time)
    
else:
    # how many lines should be displayed
    line_count = 5
    
    # get init pde
    init()
    
    # Draw IC
    pde.get_first_frame()
    data = pde.get_last_data_as_tuple()
    plt.plot(data[0], data[1], '-o', label="IC")
    
    for i in range(line_count):
        pde.get_next_frame()
        data = pde.get_last_data_as_tuple()
        plt.plot(data[0], data[1], '-o', label = f"t = {round((i+1)*pde.time_itter_displayed,5)}")
    
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    

# Must have ffmpeg installed for this to work
if save_animation:
    anim.save(save_name, fps=1)

plt.show()
