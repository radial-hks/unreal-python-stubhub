## FeatureTextureDescription Objects

```python
class FeatureTextureDescription(StructBase)
```

brief: Description of a feature texture with properties that should be uploaded to the GPU.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEncodedMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
  brief: The name of this feature texture.
- ``properties`` (Array[FeatureTexturePropertyDescription]):  [Read-Write]
  brief: Descriptions of the properties to upload to the GPU.

<a id="unreal.FeatureTextureDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumFeatureIdSetDescription"></a>