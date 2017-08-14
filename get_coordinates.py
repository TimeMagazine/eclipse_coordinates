# Initialize spiceypy, which interfaces with NASA's SPICE toolkit 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import spiceypy as spice
import json
import math
spice.tkvrsn("TOOLKIT")


# See README.md to download the kernels if they're not present
spice.furnsh("./meta_kernels.txt")


# Get minute-by-minute sun and moon positions for August 21, 2017
step = 24 * 60
utc = ['Aug 21, 2017', 'Aug 22, 2017']
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
times_eclipse = [x*(etTwo-etOne)/step + etOne for x in range(step)]
utc_times_eclipse = list(map(lambda x: spice.et2utc(x, "ISOC", 1), times_eclipse))
print(utc_times_eclipse[0:3])


sun_positions_eclipse, lightTimes = spice.spkpos('SUN', times_eclipse, 'J2000', 'CN+S', 'EARTH')
moon_positions_eclipse, lightTimes = spice.spkpos('MOON', times_eclipse, 'J2000', 'NONE', 'EARTH')

# we can lighten the JSON size by removing the date from the time stamp since it's always the same
values = [{ 
    'time': a.replace("2017-08-21T", "").replace(".0", ""), 
    'sun': {},
    'moon': {}
} for a in utc_times_eclipse]   

# note the weird order of the coordinates. This is because THREE.js and SPICE
# use difference axes

for i, v in enumerate(values):
    v.update({'sun': { 
        'x': float(sun_positions_eclipse[i][1]), 
        'y': float(sun_positions_eclipse[i][2]), 
        'z': float(sun_positions_eclipse[i][0])
    }})
    v.update({'moon': { 
        'x': float(moon_positions_eclipse[i][1]), 
        'y': float(moon_positions_eclipse[i][2]), 
        'z': float(moon_positions_eclipse[i][0])
    }})

print(values[0])


with open('./orbits/eclipse_data.json', 'w') as f:
    json.dump(values, f)


# We Need to Rotate the Earth From the Prime Meridian to J2000 Coordinates

# transform rotation from J2000 to Prime Meridian
# EARTH is ID 399: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/FORTRAN/req/naif_ids.html#Planets and Satellites
m = spice.tipbod("J2000", 399, times_eclipse[0])
a = spice.raxisa(m)
print(a[1:2][0])
