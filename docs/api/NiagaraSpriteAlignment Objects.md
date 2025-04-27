## NiagaraSpriteAlignment Objects

```python
class NiagaraSpriteAlignment(EnumBase)
```

This enum decides how a sprite particle will orient its "up" axis. Must keep these in sync with NiagaraSpriteVertexFactory.ush

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSpriteRendererProperties.h

<a id="unreal.NiagaraSpriteAlignment.UNALIGNED"></a>

#### UNALIGNED

0: Only Particles.SpriteRotation and FacingMode impact the alignment of the particle.

<a id="unreal.NiagaraSpriteAlignment.VELOCITY_ALIGNED"></a>

#### VELOCITY_ALIGNED

1: Imagine the particle texture having an arrow pointing up, this mode makes the arrow point in the direction of the Particles.Velocity attribute. FacingMode is ignored unless CustomFacingVector is set.

<a id="unreal.NiagaraSpriteAlignment.CUSTOM_ALIGNMENT"></a>

#### CUSTOM_ALIGNMENT

2: Imagine the particle texture having an arrow pointing up, this mode makes the arrow point towards the axis defined by the "Particles.SpriteAlignment" attribute. FacingMode is ignored unless CustomFacingVector is set. If the "Particles.SpriteAlignment" attribute is missing, this falls back to Unaligned mode.

<a id="unreal.NiagaraSpriteAlignment.AUTOMATIC"></a>

#### AUTOMATIC

3: Automatically select between Unaligned & CustomAlignment depending on if SpriteAlignment Binding is valid.

<a id="unreal.NiagaraSpriteFacingMode"></a>