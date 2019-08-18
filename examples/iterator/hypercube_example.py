from hypercube import HyperCube
import numpy as np
cube = HyperCube()
cube.register_dimension("ntime", 10,
    description="Timesteps")
cube.register_dimension("nbl", 20,
    description="Baselines")
cube.register_dimension("nchan", 16,
    description="Channels")

cube.register_array("uvw", ("ntime", "nbl", 3), np.float64)
cube.register_array("frequency", ("nchan",), np.float64)
cube.register_array("model_vis", ("ntime", "nbl", "nchan", 4),
    np.complex128)
print(cube)

for (lt, ut), (lc, uc) in cube.extent_iter(("ntime", 1), ("nchan", 1)):
    print ("lower time {} upper time {} "
            "lower channel {} upper channel{}".format(lt, ut, lc, uc))