## InterchangeFbxTranslatorSettings Objects

```python
class InterchangeFbxTranslatorSettings(InterchangeTranslatorSettings)
```

Fbx translator class support import of texture, material, static mesh, skeletal mesh,

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: InterchangeFbxTranslator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convert_scene`` (bool):  [Read-Write] Whether to convert FBX scene axis system to Unreal axis system.
- ``convert_scene_unit`` (bool):  [Read-Write] Whether to convert the scene from FBX unit to UE unit (centimeter).
- ``force_front_x_axis`` (bool):  [Read-Write] Whether to force the front axis to be align with X instead of -Y default.
- ``keep_fbx_namespace`` (bool):  [Read-Write] Whether to keep the name space from FBX name.

<a id="unreal.InterchangeFbxTranslator"></a>