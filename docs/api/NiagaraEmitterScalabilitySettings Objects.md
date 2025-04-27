## NiagaraEmitterScalabilitySettings Objects

```python
class NiagaraEmitterScalabilitySettings(StructBase)
```

Scalability settings for Niagara Emitters on a particular platform set.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``platforms`` (NiagaraPlatformSet):  [Read-Write] The platforms on which these settings are active (unless overridden).
- ``scale_spawn_count`` (bool):  [Read-Write] Enable spawn count scaling
- ``spawn_count_scale`` (float):  [Read-Write] Scale factor applied to spawn counts for this emitter.

<a id="unreal.NiagaraEmitterScalabilitySettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraEmitterScalabilityOverride"></a>