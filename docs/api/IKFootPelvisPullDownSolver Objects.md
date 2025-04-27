## IKFootPelvisPullDownSolver Objects

```python
class IKFootPelvisPullDownSolver(StructBase)
```

IKFoot Pelvis Pull Down Solver

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BoneControllerSolvers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pelvis_adjustment_error_tolerance`` (double):  [Read-Write] Specifies the pelvis adjustment distance error that is tolerated for each iteration of the solver

  When it is detected that the pelvis adjustment distance is incrementing at a value lower or equal
  to this value for each iteration, the solve will halt. Lower values will marginally increase visual
  quality at the cost of performance, but may require a higher PelvisAdjustmentMaxIter to be specified

  The default value of 0.01 specifies 1 centimeter of error
- ``pelvis_adjustment_interp`` (VectorRK4SpringInterpolator):  [Read-Write] Specifies the spring interpolation parameters applied during pelvis adjustment
- ``pelvis_adjustment_interp_alpha`` (double):  [Read-Write] Specifies an alpha between the original and final adjusted pelvis locations
  This is used to retain some degree of the original pelvis motion
- ``pelvis_adjustment_max_distance`` (double):  [Read-Write] Specifies the maximum displacement the pelvis can be adjusted relative to its original location
- ``pelvis_adjustment_max_iter`` (int32):  [Read-Write] Specifies the maximum number of iterations to run for the pelvis adjustment solver
  Higher iterations will guarantee closer PelvisAdjustmentErrorTolerance convergence at the cost of performance

<a id="unreal.IKFootPelvisPullDownSolver.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WarpingVectorValue"></a>