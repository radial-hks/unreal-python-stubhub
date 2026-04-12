## PropertyDescription Objects

```python
class PropertyDescription(StructBase)
```

brief: Description of a feature table property that should be encoded for access on the GPU.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEncodedMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_type`` (CesiumPropertyComponentType_DEPRECATED):  [Read-Write]
  brief: The GPU component type to coerce this property to.
- ``name`` (str):  [Read-Write]
  brief: The name of this property as it will be referenced in the material.
- ``normalized`` (bool):  [Read-Write]
  brief: If ComponentType==Uint8, this indicates whether to normalize into a [0-1] range before accessing on the GPU.
- ``type`` (CesiumPropertyType_DEPRECATED):  [Read-Write]
  brief: The property type.

<a id="unreal.PropertyDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.FeatureTexturePropertyDescription"></a>