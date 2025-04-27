## ComponentPhysicsStateChange Objects

```python
class ComponentPhysicsStateChange(EnumBase)
```

TODO: Add sleep and wake state change types to this enum, so that the
OnComponentWake and OnComponentSleep delegates may be deprecated.
Doing so would save a couple bytes per primitive component.

**C++ Source:**

- **Module**: Engine
- **File**: PrimitiveComponent.h

<a id="unreal.ComponentPhysicsStateChange.CREATED"></a>

#### CREATED

0

<a id="unreal.ComponentPhysicsStateChange.DESTROYED"></a>

#### DESTROYED

1

<a id="unreal.LifetimeCondition"></a>