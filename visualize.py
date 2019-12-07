import numpy as np
import argparse
import time
import plotly.graph_objects as go

def d_dt(v, args):
    x, y, z = v[0], v[1], v[2]
    dx = args.sigma*(y-x)
    dy = args.rho*x - y - x*z
    dz = -args.beta*z + x*y
    return dx, dy, dz

def update(v, args):
    dx, dy, dz = d_dt(v, args)
    v += args.dt*np.array([dx, dy, dz])
    return v

def run(args):
    v = np.array([args.x, args.y, args.z]).astype(np.float64)
    t = 0
    g = np.zeros((3,1))
    g[0][0] = v[0]
    g[1][0] = v[1]
    g[2][0] = v[2]
    #graph.show()
    while t<args.timesteps:
        v = update(v, args)
        g = np.concatenate((g, v.reshape((3,1))), axis=1)
        #time.sleep(0.1)
        t += 1
    graph = go.Figure(data=[go.Scatter3d(x=g[0], y=g[1], z=g[2], 
    					 mode='markers', opacity=0.8,
					 marker=dict(color=g[2],
					 size=2))])
    graph.show()                
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rho', default=28, type=float)
    parser.add_argument('--beta', default=8/3, type=float)
    parser.add_argument('--sigma', default=10, type=float)
    parser.add_argument('--dt', default=0.01, type=float)
    parser.add_argument('--timesteps', default=5000, type=int)
    parser.add_argument('--x', default=0.1, type=float)
    parser.add_argument('--y', default=0.1, type=float)
    parser.add_argument('--z', default=0.1, type=float)
    args = parser.parse_args()
    run(args)

   
