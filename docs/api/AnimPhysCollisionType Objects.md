## AnimPhysCollisionType Objects

```python
class AnimPhysCollisionType(EnumBase)
```

Anim Phys Collision Type

**C++ Source:**

- **Module**: Engine
- **File**: AnimPhysicsSolver.h

<a id="unreal.AnimPhysCollisionType.CO_M"></a>

#### CO_M

0: Only limit the center of mass from crossing planes.

<a id="unreal.AnimPhysCollisionType.CUSTOM_SPHERE"></a>

#### CUSTOM_SPHERE

1: Use the specified sphere radius to collide with planes.

<a id="unreal.AnimPhysCollisionType.INNER_SPHERE"></a>

#### INNER_SPHERE

2: Use the largest sphere that fits entirely within the body extents to collide with planes.

<a id="unreal.AnimPhysCollisionType.OUTER_SPHERE"></a>

#### OUTER_SPHERE

3: Use the smallest sphere that wholely contains the body extents to collide with planes.

<a id="unreal.SphericalLimitType"></a>