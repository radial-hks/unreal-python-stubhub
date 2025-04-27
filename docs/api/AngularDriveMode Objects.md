## AngularDriveMode Objects

```python
class AngularDriveMode(EnumBase)
```

EAngular Drive Mode

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintDrives.h

<a id="unreal.AngularDriveMode.SLERP"></a>

#### SLERP

0: Spherical lerp between the current orientation/velocity and the target orientation/velocity. NOTE: This will NOT work if any angular constraints are set to Locked.

<a id="unreal.AngularDriveMode.TWIST_AND_SWING"></a>

#### TWIST_AND_SWING

1: Path is decomposed into twist (roll constraint) and swing (cone constraint). Doesn't follow shortest arc and may experience gimbal lock. Does work with locked angular constraints.

<a id="unreal.PhysicsAssetSolverType"></a>