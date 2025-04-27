## PhysicsThreadLibrary Objects

```python
class PhysicsThreadLibrary(BlueprintFunctionLibrary)
```

Physics Thread Library

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsThreadLibrary.h

<a id="unreal.PhysicsThreadLibrary.add_force"></a>

#### add_force

```python
@classmethod
def add_force(cls,
              handle: BodyInstanceAsyncPhysicsTickHandle,
              force: Vector,
              accel_change: bool = False) -> None
```

X.add_force(handle, force, accel_change=False) -> None
Add a force to a single rigid body.
This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

Args:
    handle (BodyInstanceAsyncPhysicsTickHandle): 
    force (Vector): Force vector to apply. Magnitude indicates strength of force.
    accel_change (bool): If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no effect).

<a id="unreal.PhysicsThrusterComponent"></a>