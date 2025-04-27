## NiagaraPlatformSetRedirect Objects

```python
class NiagaraPlatformSetRedirect(StructBase)
```

Allows us to replace a specific device profile usage condition in all NiagaraPlatformSets.
Helpful when dealing with changes to device profile structure.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPlatformSet.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``c_var_condition_disabled`` (NiagaraPlatformSetCVarCondition):  [Read-Write] When in CVar mode, the CVar condition to replace this device profile entry with when the profile entry is in the Disabled state.
- ``c_var_condition_enabled`` (NiagaraPlatformSetCVarCondition):  [Read-Write] When in CVar mode, the CVar condition to replace this device profile entry with when the profile entry is in the Enabled state.
- ``mode`` (NiagaraDeviceProfileRedirectMode):  [Read-Write]
- ``profile_names`` (Array[Name]):  [Read-Write] The names of any device profile entry that will apply this redirect.
- ``redirect_profile_name`` (Name):  [Read-Write] When in Device Profile mode, the name of the device profile to redirect to.

<a id="unreal.NiagaraPlatformSetRedirect.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraUserParameterBinding"></a>