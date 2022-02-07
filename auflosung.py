import numpy as np
def sim_mt(filename):
    path = filename
    w0_3_00_path = "./" + path + "/w000_w100_w200_w300"
    w102_path = "./" + path + "/w102"
    w202_path = "./" + path + "/w202"
    # Tensoren einlesen
    with open(w0_3_00_path, 'r') as f:
        a = f.readline()
        w000 = f.readline()
        w000 = abs(float(w000.split()[1]))
        w100 = f.readline()
        w100 = abs(float(w100.split()[1]))
        w200 = f.readline()
        w200 = abs(float(w200.split()[1]))
    with open(w102_path, 'r') as f:
        a = f.readline()
        b = f.readline()
        b = b.split()
        w102 = np.asarray([abs(float(b[1])), abs(float(b[5])), abs(float(b[9]))])
    with open(w202_path, 'r') as f:
        a = f.readline()
        b = f.readline()
        b = b.split()
        w202 = np.asarray([abs(float(b[1])), abs(float(b[5])), abs(float(b[9]))])
    simMT = [w000, w100, w200, w102, w202]
    return simMT
def Precision(sim):
    #frobenius
    sim_w000 = sim[0]
    sim_w100 = sim[1]
    sim_w200 = sim[2]
    sim_w102 = sim[3]
    sim_w202 = sim[4]
    theo_w000=np.loadtxt("w000.txt")
    theo_w100=np.loadtxt("w100.txt")
    theo_w200=np.loadtxt("w200.txt")
    theo_w102 = np.loadtxt("w102.txt")
    theo_w202 = np.loadtxt("w202.txt")
    w000_pre= np.sqrt(np.square(sim_w000-theo_w000)) / np.sqrt(np.square(theo_w000))*100
    w100_pre = np.sqrt(np.square(sim_w100 - theo_w100)) / np.sqrt(np.square(theo_w100))*100
    w200_pre = np.sqrt(np.square(sim_w200 - theo_w200)) / np.sqrt(np.square(theo_w200))*100
    w102_pre= np.sqrt(np.square(sim_w102-theo_w102).sum()) / np.sqrt(np.square(theo_w102).sum())*100
    w202_pre = np.sqrt(np.square(sim_w202 - theo_w202).sum()) / np.sqrt(np.square(theo_w202).sum())*100
    with open("sim_Aufloesung.txt","w") as m:
        m.write("w000:"+ str(w000_pre) + "%"+ "\n")
        m.write("w100:"+ str(w100_pre) + "%"+ "\n")
        m.write("w200:" + str(w200_pre) + "%"+ "\n")
        m.write("w102:" + str(w102_pre) + "%"+ "\n")
        m.write("w202:" + str(w202_pre) + "%"+ "\n")

filename = input("Please input the MT-Foldername (with _mink_val):")
sim = sim_mt(filename)
Precision(sim)
print("The Sim-Precision ist calculated!")