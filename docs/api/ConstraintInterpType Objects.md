## ConstraintInterpType Objects

```python
class ConstraintInterpType(EnumBase)
```

Options for interpolating rotations

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

<a id="unreal.ConstraintInterpType.AVERAGE"></a>

#### AVERAGE

0: Weighted Average of Quaternions by their X,Y,Z,W values, The Shortest Route is Respected. The Order of Parents Doesn't Matter

<a id="unreal.ConstraintInterpType.SHORTEST"></a>

#### SHORTEST

1: Perform Quaternion Slerp in Sequence, Different Orders of Parents can Produce Different Results

<a id="unreal.RigMetaDataNameSpace"></a>