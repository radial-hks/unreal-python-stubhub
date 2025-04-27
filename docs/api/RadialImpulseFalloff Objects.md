## RadialImpulseFalloff Objects

```python
class RadialImpulseFalloff(EnumBase)
```

Enum for controlling the falloff of strength of a radial impulse as a function of distance from Origin.

**C++ Source:**

- **Module**: PhysicsCore
- **File**: ChaosEngineInterface.h

<a id="unreal.RadialImpulseFalloff.RIF_CONSTANT"></a>

#### RIF_CONSTANT

0: Impulse is a constant strength, up to the limit of its range.

<a id="unreal.RadialImpulseFalloff.RIF_LINEAR"></a>

#### RIF_LINEAR

1: Impulse should get linearly weaker the further from origin.

<a id="unreal.ViewportInteractionDraggingMode"></a>