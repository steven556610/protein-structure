def read_pdb_xyz_ligand(pdb_name):
    xyz = []
    HeadOfLigandDomin = []
    ForSecond=[]
    ForThird = []
    pdb_file = open(pdb_name, 'r')
    for line in pdb_file:
        if line.startswith("ATOM"):
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip()) 
            if line[21:22].strip() == "C"  :
                if line[12:16].strip() == "CA":
                    ddd = line[23:26].strip()
                    kkk = line[7:11].strip()
                    xyz.append([x,y,z])
                    if int(kkk)==2828:
                        HeadOfLigandDomin.append(x)
                        HeadOfLigandDomin.append(y)
                        HeadOfLigandDomin.append(z)
                    if int(kkk)==3143:
                        ForSecond.append(x)
                        ForSecond.append(y)
                        ForSecond.append(z)
                    if int(kkk)==2981:
                        ForThird.append(x)
                        ForThird.append(y)
                        ForThird.append(z)
    pdb_file.close()
    return xyz,HeadOfLigandDomin,ForSecond,ForThird

def read_pdb_xyz_domin2(pdb_name):
    xyz2 = []
    pdb_file = open(pdb_name, 'r')
    for line in pdb_file:
        if line.startswith("ATOM"):
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            if line[12:16].strip() == "CA":
               if line[21:22].strip() == "A":
                  domin2 = line[23:26].strip()
                  if (int(domin2)>=115) and (int(domin2)<=207):
                     xyz2.append([x, y, z])
                  
    pdb_file.close()
    return xyz2

def read_pdb_xyz_domin3(pdb_name):
    xyz3 = []
    pdb_file = open(pdb_name, 'r')
    for line in pdb_file:
        if line.startswith("ATOM"):
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            if line[12:16].strip() == "CA":
               if line[21:22].strip() == "A":
                  domin2 = line[23:26].strip()
                  if (int(domin2)>=208) and (int(domin2)<=311):
                     xyz3.append([x, y, z])
    pdb_file.close()
    return xyz3
