# Vicsek GNN

#### Trying to uncover pairwise potentials symbolically of birds flights using GNNs


### Real flight data projected into 2D space.
![](./animations/flight_ff2.gif)


### Vicsek model for 10 birds moving at 3m/s in 3d space projected into 2D space.
## 3D Model (mathematical description)
![](./images/v2.png)
![](./images/v1.png)
## Visulasation:  
![](./animations/vicsek.gif)

### Perameters: 
- Noise = 0.5 
- Velocity = 10 (m/s)
- theta0 = 40
- theta0 = 40

### Lenored Jones Potential to model the birds with a pairwise potential:  
![](./images/ljp.png)


![](./animations/lj.gif)

### Perameters: 
- epsilon 
- sigma 


# Extension:

### Apply this to real flight data to try to uncover some symbolic model.

##### We assume that there is some potential between pairs of birds in the flock related to their hierarcical value difference.

# References:

- Nagy, Máté, et al. "Hierarchical group dynamics in pigeon flocks." Nature 464.7290 (2010): 890-893.

- Cranmer, Miles, et al. "Discovering symbolic models from deep learning with inductive biases." Advances in Neural Information Processing Systems 33 (2020): 17429-17442.

- https://arxiv.org/pdf/1904.09584.pdf