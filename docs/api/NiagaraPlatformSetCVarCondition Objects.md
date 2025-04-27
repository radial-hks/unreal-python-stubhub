## NiagaraPlatformSetCVarCondition Objects

```python
class NiagaraPlatformSetCVarCondition(StructBase)
```

Imposes a condition that a CVar must contain a set value or range of values for a platform set to be enabled.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPlatformSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``c_var_name`` (Name):  [Read-Write] The name of the CVar we're testing the value of.
- ``fail_response`` (NiagaraCVarConditionResponse):  [Read-Write] If this CVar condition fails, how should this affect the state of the Platform Set?
- ``max_float`` (float):  [Read-Write] If the value of the CVar is greater than this maximum then the PlatformSet will not be enabled.
- ``max_int`` (int32):  [Read-Write] If the value of the CVar is greater than this maximum then the PlatformSet will not be enabled.
- ``min_float`` (float):  [Read-Write] If the value of the CVar is less than this minimum then the PlatformSet will not be enabled.
- ``min_int`` (int32):  [Read-Write] If the value of the CVar is less than this minimum then the PlatformSet will not be enabled.
- ``pass_response`` (NiagaraCVarConditionResponse):  [Read-Write] If this CVar condition passes, how should this affect the state of the Platform Set?
- ``use_max_float`` (bool):  [Read-Write] True if we should apply the maximum restriction for float CVars.
- ``use_max_int`` (bool):  [Read-Write] True if we should apply the maximum restriction for int CVars.
- ``use_min_float`` (bool):  [Read-Write] True if we should apply the minimum restriction for float CVars.
- ``use_min_int`` (bool):  [Read-Write] True if we should apply the minimum restriction for int CVars.
- ``value`` (bool):  [Read-Write] The value this CVar must contain for this platform set to be enabled.

<a id="unreal.NiagaraPlatformSetCVarCondition.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraEmitterScalabilitySettings"></a>