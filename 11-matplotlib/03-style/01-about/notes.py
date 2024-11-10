#!/usr/bin/env python3

# Reference:
# https://python3.info/matplotlib/style/about.html

#%% Style About



#%% How to understand charts?



#%% Figure anatomy



#%% Axes
# A given figure can contain many Axes, but a given Axes object can only be in one Figure
# Data limits can be controlled via set_xlim() and set_ylim() methods
# Each Axes has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label (set via set_ylabel())



#%% Axis
# These are the number-line-like objects
# Axis can be integers



#%% Artist
# Everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects)
# This includes Text objects, Line2D objects, collection objects, Patch objects, etc
# Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another