## ParticleSystemInsignificanceReaction Objects

```python
class ParticleSystemInsignificanceReaction(EnumBase)
```

Determines what a particle system will do when all of it's emitters become insignificant.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleHelper.h

<a id="unreal.ParticleSystemInsignificanceReaction.AUTO"></a>

#### AUTO

0: Looping systems will DisableTick. Non-looping systems will Complete.

<a id="unreal.ParticleSystemInsignificanceReaction.COMPLETE"></a>

#### COMPLETE

1: The system will be considered complete and will auto destroy if desired etc.

<a id="unreal.ParticleSystemInsignificanceReaction.DISABLE_TICK"></a>

#### DISABLE_TICK

2: The system will simply stop ticking. Tick will be re-enabled when any emitters become significant again. This is useful for persistent fx such as environmental fx.

<a id="unreal.ParticleSystemOcclusionBoundsMethod"></a>