import os
import tifffile as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure
from skimage.draw import ellipsoid

def marching_cubes():
    np.set_printoptions(threshold=20000)
    filename = input("Der Tiff-Filename(ohne Nachsilbe):")
    data = tf.imread(filename + ".tif")
    print("Voxel_size einstellen (Voxel ist Kubus)")
    step_size = int(input("Die Kantenlänge(minimal 1 und ganzzahlig): "))
    verts, faces, normals, values = measure.marching_cubes_lewiner(data, 0, step_size=step_size, allow_degenerate=False)
    with open(filename + ".poly", "w+") as polyfile:
        polyfile.write("POINTS\n")
        for i, vertex in enumerate(verts, start=1):
            line = str(i) + ":" + " " + str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2]) + "\n"
            polyfile.write(line)
        polyfile.write('POLYS\n')

        for i, face in enumerate(faces, start=1):
            line = str(i) + ": " + str(face[0] + 1) + " " + str(face[1] + 1) + " " + str(
                face[2] + 1) + " < c(0, 0, 0, 1)" + "\n"
            polyfile.write(line)
        polyfile.write("END")

def benchmark_ellipsoid(res):
    side = np.int_(res*np.ones(3))
    side[np.mod(side, 2) == 0] += 1
    midVoxel = (side - 1)//2
    axes = np.int_(0.9*np.array([1, 0.75, 0.5])*midVoxel)
    l, h, w = side

    voxel = np.empty(side)


    white = 2**16-1
    black = 0
    def inEllipsoid(pos):
        dist = (1/axes**2)@(pos - midVoxel)**2
        if dist > 1.0:
            return black
        else:
            return white

    for i in range(l):
        for j in range(h):
            for k in range(w):
                voxel[i,j,k] = inEllipsoid(np.array([i,j,k]))
    voxel = np.uint16(voxel)
    tf.imwrite("ellipsoid_"+str(l)+".tif", voxel, photometric='minisblack')
    filename = "ellipsoid_"+str(l)+".tif"
    return filename




flag1 = input("Do you want to creat artificial Ellipsoid? (Y/N): ")
if flag1 == "Y":
    res = input("please input the resolution for Ellipsoid (Example:51, 101 or 151): ")
    res = int(res)
    tifffile =benchmark_ellipsoid(res)
    print("create Ellipsoid successfully!")
    print("Tiff-File name is :",tifffile)
flag2 = input("Do you want to use marchingcubes to convert tiff-file to poly-file? (Y/N) ")
if flag2 == "Y":
    print("marching-cubes running......")
    marching_cubes()
