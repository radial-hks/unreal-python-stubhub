## ParticleAllocationMode Objects

```python
class ParticleAllocationMode(EnumBase)
```

EParticle Allocation Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEmitter.h

<a id="unreal.ParticleAllocationMode.AUTOMATIC_ESTIMATE"></a>

#### AUTOMATIC_ESTIMATE

0: This mode tries to estimate the max particle count at runtime by using previous simulations as reference.

<a id="unreal.ParticleAllocationMode.MANUAL_ESTIMATE"></a>

#### MANUAL_ESTIMATE

1: This mode is useful if the particle count can vary wildly at runtime (e.g. due to user parameters) and a lot of reallocations happen.

<a id="unreal.ParticleAllocationMode.FIXED_COUNT"></a>

#### FIXED_COUNT

2: This mode defines an upper limit on the number of particles that will be simulated.  Useful for rejection sampling where we expect many spawned particles to get killed.

<a id="unreal.NiagaraEmitterDefaultSummaryState"></a>