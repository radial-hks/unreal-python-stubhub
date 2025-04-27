## NiagaraEmitterCalculateBoundMode Objects

```python
class NiagaraEmitterCalculateBoundMode(EnumBase)
```

ENiagara Emitter Calculate Bound Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEmitter.h

<a id="unreal.NiagaraEmitterCalculateBoundMode.DYNAMIC"></a>

#### DYNAMIC

0: Bounds are calculated per frame (Only available for CPU emitters).

<a id="unreal.NiagaraEmitterCalculateBoundMode.FIXED"></a>

#### FIXED

1: Bounds are set from the emitter's fixed bounds.

<a id="unreal.NiagaraEmitterCalculateBoundMode.PROGRAMMABLE"></a>

#### PROGRAMMABLE

2: Bounds will be set from the script using the Emitter Properties Data Interface, or blueprint.  If not set from either source the emitter has no bounds.

<a id="unreal.ParticleAllocationMode"></a>