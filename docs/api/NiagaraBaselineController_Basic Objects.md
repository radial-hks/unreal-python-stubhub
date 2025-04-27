## NiagaraBaselineController_Basic Objects

```python
class NiagaraBaselineController_Basic(NiagaraBaselineController)
```

Simple controller that will just spawn the given system N times. If any instance completes, it will spawn a new one to replace it.
Can handle simple burst or looping systems.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPerfBaseline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effect_type`` (NiagaraEffectType):  [Read-Write] The effect type this controller is in use by.
- ``num_instances`` (int32):  [Read-Write]
- ``owner`` (NiagaraPerfBaselineActor):  [Read-Write] The owning actor for this baseline controller.
- ``system`` (NiagaraSystem):  [Read-Write] The baseline system to spawn.
- ``test_duration`` (float):  [Read-Write] Duration to gather performance stats for the given system.

<a id="unreal.NiagaraPerfBaselineActor"></a>