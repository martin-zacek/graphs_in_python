def PlotScheme(Name, options):
	import matplotlib.pyplot as plt
	import numpy as np
	print(Name)
	if Name == 'MercuryTube':
		print('begin') if 'v' in options else 0
		mercury_color = 'gray'
		water_color = '#33bbff'
		# coordinates must be in ratio 4:3 to be grid in 1:1
		# first canvas set, before the picture is done
		xmin = -8
		xmax = 8
		ymin = -4
		ymax = 8
		dec = (xmax - xmin)/10
		cen = (xmax - xmin)/100
		plt.axis([xmin, xmax, ymin, ymax])
		# cutting canvas to convenient borders after the picture is done
		xmin = -4
		xmax = 5
		ymin = -4
		ymax = 8

		pu = 22 # points per one unit on axes
		plt.axis('off')
		R = 3
		d = 1
		h1 = 2
		h2 = 3.5
		h3 = 7
		h4 = 8
		w_l = 1     # width of dimension lines
		w_c = 2     # width of contours
		la = 3*cen  # length of arrows
		wa = cen/2  # width of arrows

		# mercury
		π = 3.14159265358979323
		α = np.linspace(0, -π, 30)
		x_mercury = np.concatenate((np.array([-R, -R]), -R*np.cos(α),np.array([R, R])))
		y_mercury = np.concatenate((np.array([h2,  0]), R * np.sin(α),np.array([0, h1])))
		plt.plot(x_mercury, y_mercury, c=mercury_color, linewidth=d*pu, solid_capstyle='butt')

		# water
		plt.plot([R, R], [h1, h3], c=water_color, linewidth=d*pu, solid_capstyle='butt')

		# contures (tube)
		x_contures=np.concatenate((
		        np.array([-R-d/2, -R-d/2, -R+d/2, -R+d/2]),
		        -(R-d/2)*np.cos(α), 
		        np.array([R-d/2, R-d/2, R+d/2, R+d/2]),
		        (R+d/2)*np.cos(α) ))
		y_contures=np.concatenate((
		        np.array([    0,      h4,     h4,      0]),
		        (R-d/2)*np.sin(α),
		        np.array([    0,    h4,    h4,     0]),
		        (R+d/2)*np.sin(α) ))
		plt.plot(x_contures, y_contures, 'k-', linewidth=w_c, solid_joinstyle='bevel')

		# dimension lines (standard wertical)
		x = R+d/2
		y1, y2 = h1, h3
		delta=2*dec/2
		plt.plot([x, x+delta], [y1, y1], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([x, x+delta], [y2, y2], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([x+delta-cen, x+delta-cen], [y1, y2], 'k-', linewidth=w_l, solid_capstyle='butt')
		# arrows
		plt.plot([x+delta-cen-wa, x+delta-cen, x+delta-cen+wa], [y1+la, y1, y1+la], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([x+delta-cen-wa, x+delta-cen, x+delta-cen+wa], [y2-la, y2, y2-la], 'k-', linewidth=w_l, solid_capstyle='butt')
		# text
		plt.text(x + delta, (y1 + y2)/2, r'$h{_{W}}$')

		# dimension lines (unstandard pair)
		plt.plot([-R+d/2, cen], [h2, h2], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([ R-d/2, -cen], [h1, h1], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([0, 0], [h1, h2], 'k-', linewidth=w_l, solid_capstyle='butt')
		# arrows
		x = 0
		y1, y2 = h1, h2
		plt.plot([x-wa, x, x+wa], [y2-la, y2, y2-la], 'k-', linewidth=w_l, solid_capstyle='butt')
		plt.plot([x-wa, x, x+wa], [y1+la, y1, y1+la], 'k-', linewidth=w_l, solid_capstyle='butt')
		# text
		plt.text(cen, (h1+h2)/2-cen, r'$\Delta h$')

		# annotations are not nice, use better text only
		#plt.annotate('mercury', xy=(R+d/2, -0), xytext=(1.7*R, -0), arrowprops={'facecolor':'black', 'shrink':0.0002})
		#plt.annotate('water', xy=(R-d/2, (h3+h2)/2), xytext=(-d, (h3+h2)/2), arrowprops={'facecolor':'black', 'shrink':0.0002})
		plt.text(d, (h3+h2)/2, 'water')
		plt.text(d/6, -d, 'mercury')


	elif Name == 'SurfaceSin':
		from matplotlib import cm
		from mpl_toolkits.mplot3d import Axes3D
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		x = np.arange(-15, 15, 0.25)
		y = np.arange(-15, 15, 0.25)
		x, y = np.meshgrid(x, y)
		r = np.sqrt(x**2 + y**2)
		z = np.sin(r)
		surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm)
		plt.title('z = sin(r)')

	elif Name == 'sin1overX':
		Pi = 3.14159265358979323
		x = np.linspace(-Pi/4, Pi/4, 1600)
		y = np.sin(1/a)
		plt.plot(x, y)
		plt.title('sin(1/x)')

	elif Name == 'RandomScatter':
		from numpy.random import rand
		a = rand(1000)
		b = rand(1000)
		plt.scatter(a,b)

	elif Name == 'Lines':
		x = [1, 2, 3]
		y = [5, 7, 4]
		x2 = [1, 2, 3]
		y2 = [10, 14, 12]
		x3 = [2, 3, 1]
		y3 = [7, 5, 9]
		plt.title('Lines and points')
		plt.xlabel('osa x')
		#plt.axis(1, 4, 4, 14)
		plt.plot(x, y, 'y-', linewidth=50)
		plt.plot(x, y, 'gs')
		plt.plot(x2, y2, 'r--')
		plt.plot(x2, y2, 'b^')
		plt.plot(x3, y3, 'b-')
		plt.plot(x3, y3, 'ro')

	elif Name == 'Rectangle':
		import matplotlib.pyplot as plt
		left, width = 0, 1
		bottom, height = 0, 1
		right = left + width
		top = bottom + height
		p = plt.Rectangle((left, bottom), width, height, fill=True)
		dir(plt)
		ax = plt.gca()
		p.set_transform(ax.transAxes)
		p.set_clip_on(False)
		ax.add_patch(p)
		ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'box',
				horizontalalignment='center',
				verticalalignment='center',
				transform=ax.transAxes)
		plt.axis('off')

	if 'n' in options:
		plt.savefig(Name+'.png', format='png')
	if 'd' in options:
		plt.savefig(Name+'.pdf', format='pdf')
	if 's' in options:
		plt.savefig(Name+'.svg', format='svg')
	if 'w' in options: #show must be at the end
		plt.show()

if __name__ == '__main__':
	from sys import argv
	if len(argv)==1:
		print(' +--------------------------------------------------+')
		print(' | pictures                                         |')
		print(' |  2020 Martin Žáček                               |')
		print(' |                                                  |')
		print(' | [options] name                                   |')
		print(' |   generates picture                              |')
		print(' |                                                  |')
		print(' | -list                                            |')
		print(' |   print the list of pictures                     |')
		print(' |                                                  |')
		print(' | options:                                         |')
		print(' |  -w show                                         |')
		print(' |  -n save as png                                  |')
		print(' |  -d save as pdf                                  |')
		print(' |  -s save as swg                                  |')
		print(' |  -v verbose mode                                 |')
		print(' |                                                  |')
		print(' |  short form of options as -wndsv is possible     |')
		print(' +--------------------------------------------------+')
	else:
		from time import monotonic
		t0 = monotonic()
		arguments = []
		commands = 0
		options = set()
		list_commands = ['list']
		for arg in argv:
			if arg[0] == '-':
				if arg[1:] in list_commands:
					options.add(arg[1:])
				else:
					#every others are options or one-character command
					for c in arg[1:]:
						options.add(c)
			else:
				arguments.append(arg)
		pictures_list = (
		        'MercuryTube',
		        'SurfaceSin',
		        'sin1overX',
		        'RandomScatter',
		        'Lines',
		        'Rectangle'
		        )
		if 'list' in arg:
			for name in pictures_list:
				print(name)
		else:
			if arguments[1] in pictures_list:
				PlotScheme(arguments[1], options)
			else:
				print('Sorry, no such picture, set -list for list of pictures')
