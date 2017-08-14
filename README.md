# Eclipse Coordinates
Using SPICE to calculate coordinates for TIME's [eclipse simulation](http://time.com/4882923/total-solar-eclipse-map-places-view/)

# Install

	pip3 install -r requirements.txt

# Kernels

The kernels you need should be included in the repo, but here are direct links as well:

	cd kernels
	# Planetary ephemeris
	wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de432s.bsp
	# Planet orientation and radii
	wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc
	# Leapseconds
	wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls

# Run

	python3 get_coordinates.py