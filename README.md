# CT2MT

本程序可基于CT数据计算一个三维体的所有线性独立的Minkowski张量，最高阶数为2。用于计算的CT数据应保存在一个标准的tiff文件中。

安装：

所有程序保存于CT2MT文件夹中。在运行脚本程序前应先解压安装karambola程序（安装方法见karambola-NJP.tar.bz2）

由于在脚本中使用相对路径编译程序，所有文件和子目录的路径都不可更改！该程序通过在CT2MT文件夹中执行shell脚本ct2mt.sh工作。

使用：

Ct2MT是一个交互式程序。用户只需要输入文件名和体素大小。然后计算过程自动运行。

所有的子程序都由Bash编译成一个shell脚本。所以CT2MT运行在Linux环境下。

CT-MinkowskiTensor is a simple program to calculate all linearly independent Minkowski tensors up to rank two of a three-dimensional body from CT-Data. The CT-Data should be saved in a standard tiff-File.

Install:

All files are saved in the CT-MT package. The package is installed by extracting the tar into a subdirectory and installing the program karambola. (see the installation manual in karambola-NJP.tar.bz2)

The program works by executing a shell script ct2mt.sh. Due to compilation of the program in a script by using relative path, the paths of all files and sub-directories should not be changed!

Use:

Ct2mt is a interactive program. The user only needs to input filename and voxel size. Then the calculation process runs automatically.

All subprograms are compiled in a shell script by Bash. So ct2mt works on linux systems.
