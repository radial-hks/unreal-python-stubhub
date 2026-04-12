## CesiumMetadataEncodingDetails Objects

```python
class CesiumMetadataEncodingDetails(StructBase)
```

Describes how a property from EXT_structural_metadata will be encoded for
access in Unreal materials.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataEncodingDetails.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_type`` (CesiumEncodedMetadataComponentType):  [Read-Write] The GPU-compatible component type that this property's values will be
  encoded as. These correspond to the pixel component types that are
  supported in Unreal textures.
- ``conversion`` (CesiumEncodedMetadataConversion):  [Read-Write] The method of conversion used for this property. This describes how the
  values will be converted for access in Unreal materials. Note that not all
  property types are compatible with the methods of conversion.
- ``type`` (CesiumEncodedMetadataType):  [Read-Write] The GPU-compatible type that this property's values will be encoded as.

<a id="unreal.CesiumMetadataEncodingDetails.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.AnimationSetup"></a>