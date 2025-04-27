## RBFSolverType Objects

```python
class RBFSolverType(EnumBase)
```

The solver type to use. The two solvers have different requirements.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: RBFSolver.h

<a id="unreal.RBFSolverType.ADDITIVE"></a>

#### ADDITIVE

0: The additive solver sums up contributions from each target. It's faster
          but may require more targets for a good coverage, and requires the
              normalization step to be performed for smooth results.

<a id="unreal.RBFSolverType.INTERPOLATIVE"></a>

#### INTERPOLATIVE

1: The interpolative solver interpolates the values from each target based
              on distance. As long as the input values are within the area bounded by
              the targets, the interpolation is well-behaved and return weight values
              within the 0% - 100% limit with no normalization required.
              Interpolation also gives smoother results, with fewer targets, than additive
              but at a higher computational cost.

<a id="unreal.RBFFunctionType"></a>