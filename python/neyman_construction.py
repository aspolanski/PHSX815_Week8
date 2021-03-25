#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy 
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

plt.style.use("/home/custom_style1.mplstyle")

#Other Modules:

##### Author: Alex Polanski #####


if __name__ == "__main__":

    # Define the number of bins to use

    bin_num = 100


    # define some parameters specific to each distribution

    gauss = {'dist': 'Gaussian',
            'lower' : -10.0,
            'upper' : 10.0,
            'std' : 2.0}

    ray = {'dist' : 'Rayleigh',
            'lower': 0.5,
            'upper' : 5.0}


    #initialize the image arrays

    gauss_vals = np.zeros((bin_num,bin_num))

    ray_vals = np.zeros((bin_num,bin_num))

    # initialize the truth values for each distribution

    gauss_mu = np.linspace(gauss['lower'],gauss['upper'], bin_num)

    ray_mu = np.linspace(ray['lower'],ray['upper'], bin_num)

    # loop over each truth array, sample the distribution and get the histogram values

    for i in range(len(gauss_mu)):
        b = np.random.normal(gauss_mu[i],gauss['std'], 10000)
        hist, bin_edges = np.histogram(b, bins=bin_num, range=(gauss['lower'],gauss['upper']))
        gauss_vals[:,i] = hist

    for i in range(len(gauss_mu)):
        b = np.random.rayleigh(ray_mu[i], 10000)
        hist, bin_edges = np.histogram(b, bins=bin_num, range=(ray['lower'],ray['upper']))
        ray_vals[:,i] = hist


    # plot that shiz up

    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (16,9))

    im0 = ax[0].imshow(gauss_vals,origin='lower',
            cmap= 'gist_yarg',
            extent=[gauss['lower'],gauss['upper'],gauss['lower'],gauss['upper']])
    ax[0].set_xlabel('True Value')
    ax[0].set_ylabel('Measured Value')
    ax[0].set_title(f'{gauss["dist"]} Distribution ($\sigma$ = {gauss["std"]})')



    im1 = ax[1].imshow(ray_vals, origin='lower', 
            cmap= 'gist_yarg',
            extent = [ray['lower'],ray['upper'],ray['lower'],ray['upper'] ])
    ax[1].set_xlabel('True Value')
    ax[1].set_ylabel('Measured Value')
    ax[1].set_title(f'{ray["dist"]} Distribution')
    
    
    
    plt.colorbar(im0,ax=ax[0])
    plt.colorbar(im1,ax=ax[1])
    plt.tight_layout()
    plt.show()


