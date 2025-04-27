## MaterialOverrideNanite Objects

```python
class MaterialOverrideNanite(StructBase)
```

Storage for nanite material override.
An override material can be selected, and the override material can be used according to the current settings.
We handle removing the override material and its dependencies from the cook on platforms where we can determine
that the override material can never be used.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialOverrideNanite.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_material_editor`` (MaterialInterface):  [Read-Write] EditorOnly version of the OverrideMaterial reference.
  This is a hard reference, but is editoronly. We rely on -skiponlyeditoronly to avoid pulling this editoronly hard reference into the cook.

<a id="unreal.MaterialOverrideNanite.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ParameterGroupData"></a>