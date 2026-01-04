import os
work_path = os.path.dirname(__file__) + '/'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Parameters
a       = 1.0
t       = 1.0
delta1  = np.array([-2.0, 0.0]) * a
delta2  = np.array([1.0, np.sqrt(3)]) * a
delta3  = np.array([1.0, -np.sqrt(3)]) * a
npts    = 100
# Initial empty arrays
kx_vals = np.linspace(-np.pi/a, np.pi/a, npts)
ky_vals = np.linspace(-np.pi/a, np.pi/a, npts)
kx, ky  = np.meshgrid(kx_vals, ky_vals)
k_vecs  = np.stack([kx.ravel(), ky.ravel()], axis=-1)
kd1     = k_vecs @ delta1
kd2     = k_vecs @ delta2
kd3     = k_vecs @ delta3
# Dispersion relation
sqrt_term = np.sqrt(3 + 2 * (np.cos(kd1) + np.cos(kd2) + np.cos(kd3)))
E_plus    = t * (-1 + sqrt_term).reshape(kx.shape)
E_minus   = t * (-1 - sqrt_term).reshape(kx.shape)
E_flat    = 2 * t * np.ones_like(kx)

# Plotting
with PdfPages(work_path + 'kagome_bands.pdf') as pdf:
  # Figure 1: 3D Band Structure (x-y-z view)
  fig1  = plt.figure(figsize = (12, 12))
  ax1   = fig1.add_subplot(111, projection = '3d')
  surf1 = ax1.plot_surface(kx/a, ky/a, E_plus, label = r'$E_+$',
                           linewidth = .1, color = 'red',
                           alpha = .7, edgecolors = 'darkred')
  surf2 = ax1.plot_surface(kx/a, ky/a, E_flat, label = r'$E_\text{flat}$',
                           linewidth = .1, color = 'green',
                           alpha = .7, edgecolors = 'darkgreen')
  surf3 = ax1.plot_surface(kx/a, ky/a, E_minus, label = r'$E_-$',
                           linewidth = .1, color = 'blue',
                           alpha = .7, edgecolors = 'darkblue')
  ax1.set_xlabel(r'$k_x (\pi/a)$', fontsize = 18)
  ax1.set_ylabel(r'$k_y (\pi/a)$', fontsize = 18)
  ax1.set_zlabel(r'Energy ($t$)', fontsize  = 18)
  ax1.set_xlim([-np.pi, np.pi])
  ax1.set_ylim([-np.pi, np.pi])
  plt.xticks(fontsize = 16)
  plt.yticks(fontsize = 16)
  ax1.view_init(elev = 20, azim = 55)
  from matplotlib.patches import Patch
  legend_elements = [
    Patch(facecolor = 'red',    alpha = .7, label = r'$E_+$'),
    Patch(facecolor = 'green',  alpha = .7, label = r'$E_{flat}$'),
    Patch(facecolor = 'blue',   alpha = .7, label = r'$E_-$')
  ]
  ax1.legend(handles = legend_elements, handlelength = 6, fontsize = 15)
  ax1.grid(True, alpha = .2, color = 'gray')
  pdf.savefig(fig1, bbox_inches = 'tight')
  plt.close(fig1)

  # Figure 2: 3D Band Structure (z view)
  fig2  = plt.figure(figsize = (12, 12))
  ax2   = fig2.add_subplot(111, projection = '3d')
  surf1 = ax2.plot_surface(kx/a, ky/a, E_plus, label = r'$E_+$',
                           linewidth = .1, color = 'red',
                           alpha = .7, edgecolors = 'darkred')
  surf2 = ax2.plot_surface(kx/a, ky/a, E_flat, label = r'$E_\text{flat}$',
                           linewidth = .1, color = 'green',
                           alpha = .7, edgecolors = 'darkgreen')
  surf3 = ax2.plot_surface(kx/a, ky/a, E_minus, label = r'$E_-$',
                           linewidth = .1, color = 'blue',
                           alpha = .7, edgecolors = 'darkblue')
  ax2.set_xlabel(r'$k_x (\pi/a)$', fontsize = 18)
  ax2.set_ylabel(r'$k_y (\pi/a)$', fontsize = 18)
  ax2.set_zlabel(r'Energy ($t$)', fontsize  = 18)
  ax2.set_xlim([-np.pi, np.pi])
  ax2.set_ylim([-np.pi, np.pi])
  plt.xticks(fontsize = 16)
  plt.yticks(fontsize = 16)
  ax1.view_init(elev = 70, azim = 45)
  from matplotlib.patches import Patch
  legend_elements = [
    Patch(facecolor = 'red',    alpha = .7, label = r'$E_+$'),
    Patch(facecolor = 'green',  alpha = .7, label = r'$E_{flat}$'),
    Patch(facecolor = 'blue',   alpha = .7, label = r'$E_-$')
  ]
  ax2.legend(handles = legend_elements, handlelength = 6, fontsize = 15)
  ax2.grid(True, alpha = .2, color = 'gray')
  pdf.savefig(fig2, bbox_inches = 'tight')
  plt.close(fig2)
  
  # Figure 3: E_+ band contour
  fig3      = plt.figure(figsize = (13.8, 13.8))
  ax2a      = plt.subplot(1, 1, 1)
  contour1  = ax2a.contourf(kx/a, ky/a, E_plus,
                            levels = 50, cmap = 'Reds')
  ax2a.tick_params(axis = 'x', labelsize = 18)
  ax2a.tick_params(axis = 'y', labelsize = 18)
  ax2a.set_xlabel(r'$k_x (\pi/a)$', fontsize = 21)
  ax2a.set_ylabel(r'$k_y (\pi/a)$', fontsize = 21)
  ax2a.set_aspect('equal')
  CS1 = ax2a.contour(kx/a, ky/a, E_plus, levels = 10,
                     colors = 'black', linewidths = 1, alpha = .5)
  ax2a.clabel(CS1, inline = True, fontsize = 12, fmt = '%1.1f')
  cbar1 = plt.colorbar(contour1, ax = ax2a, shrink = .8)
  cbar1.ax.tick_params(labelsize = 14)
  cbar1.set_label(r'Energy ($t$)', fontsize = 20)
  pdf.savefig(fig3, bbox_inches = 'tight')
  plt.close(fig3)
  
  # Figure 4: E_- band contour
  fig4      = plt.figure(figsize = (13.8, 13.8))
  ax3a      = plt.subplot(1, 1, 1)
  contour3  = ax3a.contourf(kx/a, ky/a, E_minus, levels = 50, cmap = 'Blues')
  ax3a.tick_params(axis = 'x', labelsize = 18)
  ax3a.tick_params(axis = 'y', labelsize = 18)
  ax3a.set_xlabel(r'$k_x (\pi/a)$', fontsize = 21)
  ax3a.set_ylabel(r'$k_y (\pi/a)$', fontsize = 21)
  ax3a.set_aspect('equal')
  CS2 = ax3a.contour(kx/a, ky/a, E_minus, levels = 10,
                     colors = 'black', linewidths = 1, alpha = .5)
  ax3a.clabel(CS2, inline = True, fontsize = 12, fmt = '%1.1f')
  cbar2 = plt.colorbar(contour3, ax = ax3a, shrink = .8)
  cbar2.ax.tick_params(labelsize = 14)
  cbar2.set_label(r'Energy ($t$)', fontsize = 20)
  pdf.savefig(fig4, bbox_inches = 'tight')
  plt.close(fig4)