## MeDIL
This package is for causal inference using the Measurement Dependence Inducing Latent (MeDIL) Causal Model framework[^fn1]. 
This package is a work in progress, and there are many features I plan but have yet to implement, but doing so will take some time, especially considering I am primarily a theoritician and not a software engineer.
More information can be found in the [documentation](https://medil.causal.dev) or on the [project web page](https://causal.dev/projects/medil)

---
- [1. Installation](#1-installation)
- [2. Basic usage](#2-basic-usage)
- [3. Support](#3-support)
- [4. Contributing](#4-contributing)
- [5. License](#5-license)
- [6. Changelog](#6-changelog)
- [7. References](#7-references)
---


### 1. Installation

### 2. Basic usage


```python
>>> import numpy as np
>>> from medil.independence_test import hypothesis_test
>>> from medil.independence_test import dependencies
>>> from medil.ecc_algorithms import find_clique_min_cover as find_cm
```

Simulate 1000 samples of data for 6 measurement variables with dependencies induced by 3 latent variables
```python
>>> num_samps = 1000
>>> m_noise = np.random.standard_normal((6, num_samps))
>>> l_noise = np.random.standard_normal((3, num_samps))
>>> 
>>> m_samps = np.empty((6, num_samps))
>>> m_samps[0] = l_noise[0] + .2 * m_noise[0]
>>> m_samps[1] = 2 * l_noise[0] - 3 *l_noise[1]  + m_noise[1]
>>> m_samps[2] = 5 * l_noise[2] +  m_noise[2] - 10 * l_noise[0]
>>> m_samps[3] = 4 * l_noise[1] + .5 * m_noise[3]
>>> m_samps[4] = l_noise[2] * 3 + l_noise[1] * 3 + m_noise[4]
>>> m_samps[5] = -7 * l_noise[2] + m_noise[5] * 2
>>> m_samps
array([[ -1.09618589,   0.36562761,   0.1821539 , ...,  -1.15422013,   -0.47157367,   0.86087563],
       [  3.58650565,   1.01922667,   3.038765  , ...,  -2.30804292,    5.83232892,   2.08316629],
       [ 14.13299282,   3.21167764, -17.29291657, ...,  14.83832827,   -6.53695807,  -9.48083731],
       [ -6.62993973,   1.34280329,  -2.1832981 , ...,  -0.35295787,   -5.6925398 ,   0.531198  ],
       [ -0.96126815,   2.93188441, -11.50689577, ...,   0.98983901,   -8.5647367 ,  -0.14181254],
       [-12.74328352,  -4.95887306,  20.20499673, ...,  -0.49624485,    6.5901562 ,   0.08445142]])

```

Use distance correlation as a non-linear measure of dependence for permutation based hypothesis testing (could take a few minutes, depending on your machine)
```python
>>> p_vals, null_corr = hypothesis_test(m_samps, 100)
>>> dep_graph = dependencies(null_corr, .1, p_vals, .05)
>>> dep_graph
array([[ True,  True,  True, False, False, False],
       [ True,  True,  True,  True,  True, False],
       [ True,  True,  True, False,  True,  True],
       [False,  True, False,  True,  True, False],
       [False,  True,  True,  True,  True,  True],
       [False, False,  True, False,  True,  True]])
```

find the edges of a MeDIL causal model with the fewest number of latent variables
```python
>>> min_mcm = find_cm(dep_graph)
>>> min_mcm
array([[0, 0, 1, 0, 1, 1],
       [0, 1, 0, 1, 1, 0],
       [1, 1, 1, 0, 0, 0]])
```
The result is a directed biadjacency matrix, where rows are latents variables, columns are measurement variables, and each 1 indicates a directed edge from the latent to measurement variable.

### 3. Support
If you have any questions, suggestions, feedback, or bugs to report, please [contact me](https://causal.dev/#contact) or [open an issue](https://gitlab.com/alex-markham/medil/issues).
Additionally, if you would like to use this package or any of its code in a project, feel free (but not obliged) to contact me.

### 4. Contributing
If you would like to contribute, you can [contact me](https://causal.dev/#contact) and fork this repo on GitLab (or see [this discussion](https://gist.github.com/DavideMontersino/810ebaa170a2aa2d2cad) for information on forking to GitHub).

### 5. License
Refer to [LICENSE](https://gitlab.com/alex-markham/medil/blob/master/LICENSE), which is the [GNU General Public License v3 (GPLv3)](https://choosealicense.com/licenses/gpl-3.0/).

### 6. Changelog
Refer to [CHANGELOG](https://gitlab.com/alex-markham/medil/blob/master/CHANGELOG.md) to see planned features and history of the already implemented features. 

### 7. References
[^fn1]: Alex Markham and Moritz Grosse-Wentrup (2019). *Measurement Dependence Inducing Latent Causal Models*. arXiv:1910.08778 [stat.ML]. ([link](https://arxiv.org/abs/1910.08778))
