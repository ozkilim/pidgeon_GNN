# Vicsek GNN

#### We first create a 3D simulation of 10 particles and tune perameters by eye so the simulation resembles the real bird data

## 3D Model (mathematical description)
<p align="center">
    <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20%5Ctheta_i%28t&plus;%5CDelta%20t%29%5C%5C%20%5Calpha_i%28t&plus;%5CDelta%20t%29%20%5Cend%7Bpmatrix%7D%20%3D%20%5Cbegin%7Bpmatrix%7D%20%3C%5Ctheta_i%28t%29%3E_%7B%7Cr_i-r_j%7C%3Cr%7D%5C%5C%20%3C%5Calpha_i%28t%29%3E_%7B%7Cr_i-r_j%7C%3Cr%7D%20%5Cend%7Bpmatrix%7D%20&plus;%20%5Cbegin%7Bpmatrix%7D%20%5Ceta_i%28t%29%5C%5C%20%5Cdelta_i%28t%29%20%5Cend%7Bpmatrix%7D" alt="angles vicsek equation"/>
</p>

<p align="center">
    <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20v_i_x%28t&plus;%5CDelta%20t%29%5C%5C%20v_i_y%28t&plus;%5CDelta%20t%29%5C%5C%20v_i_z%28t&plus;%5CDelta%20t%29%20%5Cend%7Bpmatrix%7D%20%3D%20%5Cbegin%7Bpmatrix%7D%20%5Ccos%28%5Ctheta_i%28t&plus;%5CDelta%20t%29%29%5Ccdot%5Csin%28%5Calpha_i%28t&plus;%5CDelta%20t%29%29%5C%5C%20%5Csin%28%5Ctheta_i%28t&plus;%5CDelta%20t%29%29%5Ccdot%5Csin%28%5Calpha_i%28t&plus;%5CDelta%20t%29%29%5C%5C%20%5Ccos%28%5Calpha_i%28t&plus;%5CDelta%20t%29%29%20%5Cend%7Bpmatrix%7D" alt="velocity vicsek equation"/>
</p>

<p align="center">
    <img src="https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20r_i_x%28t&plus;%5CDelta%20t%29%5C%5C%20r_i_y%28t&plus;%5CDelta%20t%29%5C%5C%20r_i_z%28t&plus;%5CDelta%20t%29%20%5Cend%7Bpmatrix%7D%20%3D%20%5Cbegin%7Bpmatrix%7D%20r_i_x%28t%29%5C%5C%20r_i_y%28t%29%5C%5C%20r_i_z%28t%29%20%5Cend%7Bpmatrix%7D%20&plus;%20%5Cbegin%7Bpmatrix%7D%20v_i_x%28t&plus;%5CDelta%20t%29%5C%5C%20v_i_y%28t&plus;%5CDelta%20t%29%5C%5C%20v_i_z%28t&plus;%5CDelta%20t%29%20%5Cend%7Bpmatrix%7D%20%5Ccdot%20%5CDelta%20t" alt="position vicsek equation"/>
</p>


# Project roadmap:

1. Build Vicsek model simulation.

### Real flight data projected into 2D space.

![](./animations/flight_ff2.gif)

### Vicsek model for 10 birds moving at 3m/s in 3d space projected into 2D space.

![](./animations/vicsek.gif)

### Lenored Jones Potential to model the birds with a pairwise potential: 

![](./animations/lj.gif)


2. Visualise
3. Turn into GNN
4. Train GNN
5. Perform symbolic regression on messages to try to recover Vicsek model.

# Extension:

### Apply this to real flight data to try to uncover some symbolic model.

##### We assume that there is some potential between pairs of birds in the flock related to their hierarcical value difference.

# References:

- Nagy, Máté, et al. "Hierarchical group dynamics in pigeon flocks." Nature 464.7290 (2010): 890-893.

- Cranmer, Miles, et al. "Discovering symbolic models from deep learning with inductive biases." Advances in Neural Information Processing Systems 33 (2020): 17429-17442.

- https://arxiv.org/pdf/1904.09584.pdf