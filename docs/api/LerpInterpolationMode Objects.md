## LerpInterpolationMode Objects

```python
class LerpInterpolationMode(EnumBase)
```

Different methods for interpolating rotation between transforms

**C++ Source:**

- **Module**: Engine
- **File**: KismetMathLibrary.h

<a id="unreal.LerpInterpolationMode.QUAT_INTERP"></a>

#### QUAT_INTERP

0: Shortest Path or Quaternion interpolation for the rotation.

<a id="unreal.LerpInterpolationMode.EULER_INTERP"></a>

#### EULER_INTERP

1: Rotor or Euler Angle interpolation.

<a id="unreal.LerpInterpolationMode.DUAL_QUAT_INTERP"></a>

#### DUAL_QUAT_INTERP

2: Dual quaternion interpolation, follows helix or screw-motion path between keyframes.

<a id="unreal.MatrixColumns"></a>