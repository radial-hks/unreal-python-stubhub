## FeatureTexturePropertyDescription Objects

```python
class FeatureTexturePropertyDescription(StructBase)
```

brief: Description of a feature texture property that should be uploaded to the GPU.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEncodedMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
  brief: The name of this property as it will be referenced in the material.
- ``normalized`` (bool):  [Read-Write]
  brief: If ComponentType==Uint8, this indicates whether to normalize into a [0-1] range before accessing on the GPU.
- ``swizzle`` (str):  [Read-Write]
  brief: This string describes the channel order of the incoming feature texture property (e.g., "rgb", "bgra", etc.). This helps us fix the channel order when accessing on the GPU.
- ``type`` (CesiumPropertyType_DEPRECATED):  [Read-Write]
  brief: The property type.

<a id="unreal.FeatureTexturePropertyDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumPropertyTablePropertyDescription"></a>