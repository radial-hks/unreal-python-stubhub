## SubsurfaceProfile Objects

```python
class SubsurfaceProfile(Object)
```

Subsurface Scattering profile asset, can be specified at the material. Only for "Subsurface Profile" materials, is use during Screenspace Subsurface Scattering
Don't change at runtime. All properties in here are per material - texture like variations need to come from properties that are in the GBuffer.

**C++ Source:**

- **Module**: Engine
- **File**: SubsurfaceProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (SubsurfaceProfileStruct):  [Read-Write]

<a id="unreal.MaterialInterfaceEditorOnlyData"></a>