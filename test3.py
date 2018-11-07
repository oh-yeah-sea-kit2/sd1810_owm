nit = 100
u, v, velocity = doSimulation(nx, ny, wind, lowMask, 'withOutUVMap')

pyplot.imshow(mapImg)
plotX, plotY = numpy.meshgrid(numpy.linspace(0, nx * ratio, nx), numpy.linspace(0, ny * ratio, ny))
pyplot.contourf(plotX, plotY, velocity, alpha = 0.2, cmap = cm.jet)
pyplot.colorbar()
pyplot.quiver(plotX, plotY, u, v)
pyplot.streamplot(plotX, plotY, u, -v)
pyplot.xlabel('X')
pyplot.ylabel('Y')
