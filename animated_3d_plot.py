import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as pltanim
import os

input_dir = 'output_files/'
output_dir = 'output_plots/linear_distribution/discrete/'

variable_param = 'pwv'
am0 = 1.2
cloud0 = 0.0

colour_dict = np.load(os.path.join(input_dir,'colour_dict_varying_{0}_airmass_{1}_cloud_{2}.npy'.format(variable_param,am0,cloud0)),allow_pickle=True).ravel()[0]
colour_dict_ref = np.load(os.path.join(input_dir,'colour_dict_varying_{0}_airmass_{1}_cloud_{2}_ref.npy'.format(variable_param,am0,cloud0)),allow_pickle=True).ravel()[0]

sn_colour_dict = np.load(os.path.join(input_dir,'sn_colour_dict_varying_{0}_airmass_{1}_cloud_{2}.npy'.format(variable_param,am0,cloud0)),allow_pickle=True).ravel()[0]
sn_colour_dict_ref = np.load(os.path.join(input_dir,'sn_colour_dict_varying_{0}_airmass_{1}_cloud_{2}_ref.npy'.format(variable_param,am0,cloud0)),allow_pickle=True).ravel()[0]

atm_vals = np.load(os.path.join(input_dir,'atm_vals_{0}_airmass_{1}_cloud_{2}.npy'.format(variable_param,am0,cloud0)),allow_pickle=True).ravel()

spectral_types = ['O','B','A','F','G','K','M']
type_colors = {'O':'violet','B':'cyan','A':'b','F':'g','G':'y','K':'orange','M':'r'}
type_markers = {'O':'s','B':'x','A':'o','F':'v','G':'^','K':'P','M':'*'}

###########################################

def animate(ang):
    ax.view_init(30,ang)

###########################################

colorx = 'i-z'
colory = 'z-Y'
colorz = 'r-i'

fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(projection='3d')

minx, maxx = [], []
miny, maxy = [], []
minz, maxz = [], []

iso_vals1 = []
iso_vals2 = []
iso_vals3 = []
for spec_type in spectral_types:
    for si in colour_dict[spec_type]:
        delta1 = (colour_dict[spec_type][si][colorx.lower()]-colour_dict_ref[spec_type][si][colorx.lower()])*1000.
        delta2 = (colour_dict[spec_type][si][colory.lower()]-colour_dict_ref[spec_type][si][colory.lower()])*1000.
        delta3 = (colour_dict[spec_type][si][colorz.lower()]-colour_dict_ref[spec_type][si][colorz.lower()])*1000.

        msize = [10.]
        msize = msize+[40.]*(len(delta1)-2)
        msize.append(110.)

        ax.scatter(delta1,delta2,delta3,c=type_colors[spec_type],marker='o',s=msize)
        ax.plot(delta1,delta2,delta3,ls='-',marker='',color='grey',alpha=0.2)

        minx.append(np.min(delta1))
        miny.append(np.min(delta2))
        minz.append(np.min(delta3))
        maxx.append(np.max(delta1))
        maxy.append(np.max(delta2))
        maxz.append(np.max(delta3))

        iso_vals1.append(delta1)
        iso_vals2.append(delta2)
        iso_vals3.append(delta3)

    ax.plot([],[],c=type_colors[spec_type],ls='',marker='o',label=spec_type)

for sn in sn_colour_dict.keys():
    delta1_sn = (sn_colour_dict[sn][colorx.lower()]-sn_colour_dict_ref[sn][colorx.lower()])*1000.
    delta2_sn = (sn_colour_dict[sn][colory.lower()]-sn_colour_dict_ref[sn][colory.lower()])*1000.
    delta3_sn = (sn_colour_dict[sn][colorz.lower()]-sn_colour_dict_ref[sn][colorz.lower()])*1000.

    msize = [10.]
    msize = msize+[40.]*(len(delta1)-2)
    msize.append(110.)

    ax.scatter(delta1_sn,delta2_sn,delta3_sn,c='k',marker='o',s=msize)
    ax.plot(delta1_sn,delta2_sn,delta3_sn,ls='-',marker='',color='grey',alpha=0.2)

    minx.append(np.min(delta1_sn))
    miny.append(np.min(delta2_sn))
    minz.append(np.min(delta3_sn))
    maxx.append(np.max(delta1_sn))
    maxy.append(np.max(delta2_sn))
    maxz.append(np.max(delta3_sn))

    iso_vals1.append(delta1_sn)
    iso_vals2.append(delta2_sn)
    iso_vals3.append(delta3_sn)

ax.plot([],[],c='k',ls='',marker='o',label='SN Ia')

iso_vals1 = np.array(iso_vals1)
iso_vals2 = np.array(iso_vals2)
iso_vals3 = np.array(iso_vals3)
for val in range(iso_vals1.shape[1]):
    sort_index = np.argsort(iso_vals1[:,val])
    ax.plot(iso_vals1[:,val][sort_index],iso_vals2[:,val][sort_index],iso_vals3[:,val][sort_index],ls='-',marker='',color='k',zorder=-1)


ax.set_xlabel(r'$\Delta$'+'('+colorx+') [mmag]',fontsize=18)
ax.set_ylabel(r'$\Delta$'+'('+colory+') [mmag]',fontsize=18)
ax.set_zlabel(r'$\Delta$'+'('+colorz+') [mmag]',fontsize=18)

xrange = np.linspace(np.min(minx),np.max(maxx),100)
yrange = np.linspace(np.min(miny),np.max(maxy),100)
zrange = np.linspace(np.min(minz),np.max(maxz),100)

ax.plot(xrange,np.zeros(len(yrange)),np.zeros(len(zrange)),'r--')
ax.plot(np.zeros(len(xrange)),yrange,np.zeros(len(zrange)),'r--')
ax.plot(np.zeros(len(xrange)),np.zeros(len(yrange)),zrange,'r--')

ax.legend(fontsize=12)

#plt.show()

ani = pltanim.FuncAnimation(fig,animate,interval=360,repeat=True, save_count=360)
#plt.show()

writergif = pltanim.PillowWriter(fps=20)
ani.save(os.path.join(output_dir,'{0}_{1}_{2}_plot_animation_varying_{3}_airmass_{4}_cloud_{5}.gif'.format(colorx,colory,colorz,variable_param,am0,cloud0)), writer=writergif)

'''
for angle in range(0,360):
    ax.view_init(30,angle)
    plt.draw()
    plt.pause(0.001)
'''



