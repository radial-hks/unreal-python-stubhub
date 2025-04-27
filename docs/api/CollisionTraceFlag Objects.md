## CollisionTraceFlag Objects

```python
class CollisionTraceFlag(EnumBase)
```

ECollision Trace Flag

**C++ Source:**

- **Module**: PhysicsCore
- **File**: BodySetupEnums.h

<a id="unreal.CollisionTraceFlag.CTF_USE_DEFAULT"></a>

#### CTF_USE_DEFAULT

0: Use project physics settings (DefaultShapeComplexity)

<a id="unreal.CollisionTraceFlag.CTF_USE_SIMPLE_AND_COMPLEX"></a>

#### CTF_USE_SIMPLE_AND_COMPLEX

1: Create both simple and complex shapes. Simple shapes are used for regular scene queries and collision tests. Complex shape (per poly) is used for complex scene queries.

<a id="unreal.CollisionTraceFlag.CTF_USE_SIMPLE_AS_COMPLEX"></a>

#### CTF_USE_SIMPLE_AS_COMPLEX

2: Create only simple shapes. Use simple shapes for all scene queries and collision tests.

<a id="unreal.CollisionTraceFlag.CTF_USE_COMPLEX_AS_SIMPLE"></a>

#### CTF_USE_COMPLEX_AS_SIMPLE

3: Create only complex shapes (per poly). Use complex shapes for all scene queries and collision tests. Can be used in simulation for static shapes only (i.e can be collided against but not moved through forces or velocity.)

<a id="unreal.PhysicalSurface"></a>