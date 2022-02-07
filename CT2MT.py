
tifffile = benchmark_ellipsoid(CT_resolution)

surface = marching_cubes(tifffile, MC_resolution)

surface = (vert, surf, ...)

write_polyfile(surface, polypath)

os.system("karambola polypath outputfile")

minkowski_tensor = read_karambola(outputfile)

minkowski_tensor = (W001, W102)

def frobenious_norm(matrix):
    blablalba

error = frobenius_norm(W001)



