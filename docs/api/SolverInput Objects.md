## SolverInput Objects

```python
class SolverInput(StructBase)
```

Solver Input

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: FullBodyIK
- **File**: FBIKShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_motion_strength`` (float):  [Read-Write] * This value is applied to the target information for effectors, which influence back to
  * Joint's motion that are affected by the end effector
  * The reason min/max is used when we apply the depth through the chain that are affected
- ``damping`` (float):  [Read-Write] The precision to use for the fabrik solver
- ``default_target_clamp`` (float):  [Read-Write] This is a scale value (range from 0-0.7) that is used to stablize the target vector. If less, it's more stable, but it can reduce speed of converge.
- ``linear_motion_strength`` (float):  [Read-Write] * This value is applied to the target information for effectors, which influence back to
  * Joint's motion that are affected by the end effector
  * The reason min/max is used when we apply the depth through the chain that are affected
- ``max_iterations`` (int32):  [Read-Write] The maximum number of iterations. Values between 4 and 16 are common.
- ``min_angular_motion_strength`` (float):  [Read-Write]
- ``min_linear_motion_strength`` (float):  [Read-Write]
- ``precision`` (float):  [Read-Write] The precision to use for the solver
- ``use_jacobian_transpose`` (bool):  [Read-Write] Cheaper solution than default Jacobian Pseudo Inverse Damped Least Square

<a id="unreal.SolverInput.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.FBIKEndEffector"></a>