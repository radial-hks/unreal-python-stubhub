## ParticleSignificanceLevel Objects

```python
class ParticleSignificanceLevel(EnumBase)
```

A level of significance for a particle system. Used by game code to enable/disable emitters progressively as they move away from the camera or are occluded/off screen.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleHelper.h

<a id="unreal.ParticleSignificanceLevel.LOW"></a>

#### LOW

0: Low significance emitter. Culled first.

<a id="unreal.ParticleSignificanceLevel.MEDIUM"></a>

#### MEDIUM

1: Medium significance emitter.

<a id="unreal.ParticleSignificanceLevel.HIGH"></a>

#### HIGH

2: High significance emitter. Culled last.

<a id="unreal.ParticleSignificanceLevel.CRITICAL"></a>

#### CRITICAL

3: Critical emitter. Never culled.

<a id="unreal.TrailWidthMode"></a>