## PhysicalMaterialSoftCollisionMode Objects

```python
class PhysicalMaterialSoftCollisionMode(EnumBase)
```

Soft collision mode for a physical material.

NOTE: Must match EChaosPhysicsMaterialSoftCollisionMode

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicalMaterial.h

<a id="unreal.PhysicalMaterialSoftCollisionMode.NONE"></a>

#### NONE

0: No soft collisionss

<a id="unreal.PhysicalMaterialSoftCollisionMode.RELATIVE_THICKNESS"></a>

#### RELATIVE_THICKNESS

1: SoftCollisionThickess is a fraction of the bounds (minimum axis). Should be less than 0.5

<a id="unreal.PhysicalMaterialSoftCollisionMode.ABSOLUTE_THICKESS"></a>

#### ABSOLUTE_THICKESS

2: SoftCollisionThickess is an absolute value in cm

<a id="unreal.ReimportStrategyFlags"></a>