## FeatureTableDescription Objects

```python
class FeatureTableDescription(StructBase)
```

brief: Description of a feature table containing properties to be encoded for access on the GPU.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEncodedMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``access_type`` (CesiumFeatureTableAccessType_DEPRECATED):  [Read-Write]
  brief: Describes how this feature table is accessed. Either through feature id textures, feature id attributes, mixed, or neither.
- ``channel`` (str):  [Read-Write]
  brief: If the AccessType==Texture, this string represents the channel of the feature id texture that will be used to index into this feature table.
- ``name`` (str):  [Read-Write]
  brief: The name of this feature table.
- ``properties`` (Array[PropertyDescription]):  [Read-Write]
  brief: Descriptions of the properties to upload to the GPU.

<a id="unreal.FeatureTableDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.FeatureTextureDescription"></a>