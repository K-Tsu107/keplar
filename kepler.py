# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

def draw_graph(x,y):
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion')
    plt.plot(x,y)
    plt.show()

  
def animate(i):
  # 50回 1回  表示
  earth.center = (x_graph[i*50], y_graph[i*50]) 
  time_text.set_text("t={}".format(i*50)) 
  return earth,

# 初期化
def init():
    earth.center = (x_graph[0], y_graph[0])
    ax.add_patch(earth)
    ax.add_patch(sun)
    return earth,


if __name__=="__main__":
  dt = 0.01
  t = 0.0
  G = 6.67408 * 10**(-11)
  M = 1.989 * 10**30
  m = 5.972 * 10**24
  Position0 = np.array([1.521*10**11,0.0]) # 位置の初期値
  Momentum0 = np.array([0.0,29291]) # 運動量の初期値

  # variable for draw 
  x_graph = []
  y_graph = []

  k1_Position = np.array([0.0,0.0])
  k2_Position = np.array([0.0,0.0])
  k3_Position = np.array([0.0,0.0])
  k4_Position = np.array([0.0,0.0])
  k1_Momentum = np.array([0.0,0.0])
  k2_Momentum = np.array([0.0,0.0])
  k3_Momentum = np.array([0.0,0.0])
  k4_Momentum = np.array([0.0,0.0])
  Position = np.array([0.0,0.0])
  Momentum = np.array([0.0,0.0])

  Position = Position0
  Momentum = Momentum0

  tPosition = np.array([0.0,0.0])
  tMomentum = np.array([0.0,0.0])

  while(t < 100.0): 
    #Runge-kutta
    # k1
    tPosition[0] = Position[0]
    tPosition[1] = Position[1]
    tMomentum[0] = Momentum[0]
    tMomentum[1] = Momentum[1]
    r = np.math.hypot(tPosition[0],tPosition[1])
    k1_Position[0] = tMomentum[0] / m * dt
    k1_Position[1] = tMomentum[1] / m * dt
    k1_Momentum[0] = -G * M * m * tPosition[0] * (1.0/(r**3)) * dt
    k1_Momentum[1] = -G * M * m * tPosition[1] * (1.0/(r**3)) * dt
    # k2
    tPosition[0] = Position[0] + 0.5 * k1_Position[0]
    tPosition[1] = Position[1] + 0.5 * k1_Position[1]
    tMomentum[0] = Momentum[0] + 0.5 * k1_Momentum[0]
    tMomentum[1] = Momentum[1] + 0.5 * k1_Momentum[1]
    r = np.math.hypot(tPosition[0],tPosition[1])
    k2_Position[0] = tMomentum[0] / m * dt
    k2_Position[1] = tMomentum[1] / m * dt
    k2_Momentum[0] = -G * M * m * tPosition[0] * (1.0/(r**3)) * dt
    k2_Momentum[1] = -G * M * m * tPosition[1] * (1.0/(r**3)) * dt
    # k3
    tPosition[0] = Position[0] + 0.5 * k2_Position[0]
    tPosition[1] = Position[1] + 0.5 * k2_Position[1]
    tMomentum[0] = Momentum[0] + 0.5 * k2_Momentum[0]
    tMomentum[1] = Momentum[1] + 0.5 * k2_Momentum[1]
    r = np.math.hypot(tPosition[0],tPosition[1])
    k3_Position[0] = tMomentum[0] / m * dt
    k3_Position[1] = tMomentum[1] / m * dt
    k3_Momentum[0] = -G * M * m * tPosition[0] * (1.0/(r**3)) * dt
    k3_Momentum[1] = -G * M * m * tPosition[1] * (1.0/(r**3)) * dt
    # k4
    tPosition[0] = Position[0] + k3_Position[0]
    tPosition[1] = Position[1] + k3_Position[1]
    tMomentum[0] = Momentum[0] + k3_Momentum[0]
    tMomentum[1] = Momentum[1] + k3_Momentum[1]
    r = np.math.hypot(tPosition[0],tPosition[1])
    k4_Position[0] = tMomentum[0] / m * dt
    k4_Position[1] = tMomentum[1] / m * dt
    k4_Momentum[0] = -G * M * m * tPosition[0] * (1.0/(r**3)) * dt
    k4_Momentum[1] = -G * M * m * tPosition[1] * (1.0/(r**3)) * dt
    # 加重平均
    Position[0] += (k1_Position[0] + 2*k2_Position[0] + 2*k3_Position[0] + k4_Position[0])/6.0
    Position[1] += (k1_Position[1] + 2*k2_Position[1] + 2*k3_Position[1] + k4_Position[1])/6.0
    Momentum[0] += (k1_Momentum[0] + 2*k2_Momentum[0] + 2*k3_Momentum[0] + k4_Momentum[0])/6.0
    Momentum[1] += (k1_Momentum[1] + 2*k2_Momentum[1] + 2*k3_Momentum[1] + k4_Momentum[1])/6.0
    
    x_graph.append(Position[0])
    y_graph.append(Position[1])
    t += dt

    
  draw_graph(x_graph,y_graph)
  # fig = plt.figure()
  # ax = plt.axes(xlim=(-3, 3), ylim=(-3, 3))
  # earth = plt.Circle((1, 0), 0.1, fc='b')
  # sun = plt.Circle((0, 0), 0.2, fc='r')
  # time_text = ax.text(0.05, 0.9, 't=0', transform=ax.transAxes) 
  # plt.gca().set_aspect('equal', adjustable='box')
  # plt.plot(x_graph, y_graph, 'k')
  # anim = animation.FuncAnimation(fig, animate,
  #                              init_func=init,
  #                              frames=200,
  #                              interval=50,
  #                              blit=False,
  #                              repeat=False)

  # plt.show()
