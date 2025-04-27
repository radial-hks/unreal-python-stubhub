## NiagaraSystemSpawnSectionEvaluateBehavior Objects

```python
class NiagaraSystemSpawnSectionEvaluateBehavior(EnumBase)
```

Defines options for system life cycle for when the section is evaluating from the 2nd frame until the last frame of the section.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: MovieSceneNiagaraSystemSpawnSection.h

<a id="unreal.NiagaraSystemSpawnSectionEvaluateBehavior.ACTIVATE_IF_INACTIVE"></a>

#### ACTIVATE_IF_INACTIVE

0: The system's component will be activated on any frame where it is inactive.  This is useful for continuous emitters, especially if the sequencer will start in the middle of the section.

<a id="unreal.NiagaraSystemSpawnSectionEvaluateBehavior.NONE"></a>

#### NONE

1: There sill be no changes to the system life cycle while the section is evaluating.

<a id="unreal.NiagaraSystemSpawnSectionEndBehavior"></a>