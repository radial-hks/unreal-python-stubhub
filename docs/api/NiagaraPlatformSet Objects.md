## NiagaraPlatformSet Objects

```python
class NiagaraPlatformSet(StructBase)
```

Niagara Platform Set

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPlatformSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``c_var_conditions`` (Array[NiagaraPlatformSetCVarCondition]):  [Read-Write] Set of CVars values we require for this platform set to be enabled. If any of the linked CVars don't have the required values then this platform set will not be enabled.
- ``device_profile_states`` (Array[NiagaraDeviceProfileStateEntry]):  [Read-Write] States of specific device profiles we've set.
- ``quality_level_mask`` (int32):  [Read-Write] Mask defining which effects qualities this set matches.

<a id="unreal.NiagaraPlatformSet.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraEmitterScalabilityOverrides"></a>