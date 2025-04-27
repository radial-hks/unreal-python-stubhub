## PropertyAnimatorCorePresetBase Objects

```python
class PropertyAnimatorCorePresetBase(Object)
```

Abstract Base class to define preset for animators with custom properties and options
Will get registered automatically by the subsystem
Should remain transient and stateless

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: PropertyAnimatorCorePresetBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``preset_content`` (str):  [Read-Only] Preset stringify content
- ``preset_format`` (Name):  [Read-Only] Format used for the preset content
- ``preset_name`` (Name):  [Read-Only] Name used to display this preset to the user
- ``preset_version`` (int32):  [Read-Only] Version of this preset for diffs

<a id="unreal.PropertyAnimatorCoreAnimatorPreset"></a>