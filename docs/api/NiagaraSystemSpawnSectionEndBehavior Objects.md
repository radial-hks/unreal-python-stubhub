## NiagaraSystemSpawnSectionEndBehavior Objects

```python
class NiagaraSystemSpawnSectionEndBehavior(EnumBase)
```

Defines options for system life cycle for the time after the section.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: MovieSceneNiagaraSystemSpawnSection.h

<a id="unreal.NiagaraSystemSpawnSectionEndBehavior.SET_SYSTEM_INACTIVE"></a>

#### SET_SYSTEM_INACTIVE

0: / When the section ends the system is set to inactive which stops spawning but lets existing particles simulate until death.

<a id="unreal.NiagaraSystemSpawnSectionEndBehavior.DEACTIVATE"></a>

#### DEACTIVATE

1: / When the section ends the system's component is deactivated which will kill all existing particles.

<a id="unreal.NiagaraSystemSpawnSectionEndBehavior.NONE"></a>

#### NONE

2: / Does nothing when the section ends and allows the system to continue to run as normal.

<a id="unreal.NiagaraAgeUpdateMode"></a>