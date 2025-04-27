## ComponentHitSignature Objects

```python
class ComponentHitSignature(MulticastDelegateBase)
```

Delegate for notification of blocking collision against a specific component.
NormalImpulse will be filled in for physics-simulating bodies, but will be zero for swept-component blocking collisions.

Args:
    hit_component (PrimitiveComponent): 
    other_actor (Actor): 
    other_comp (PrimitiveComponent): 
    normal_impulse (Vector): 
    hit (HitResult):

**C++ Source:**

- **Module**: Engine
- **File**: PrimitiveComponent.h

<a id="unreal.ComponentHitSignature.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.ComponentOnClickedSignature"></a>