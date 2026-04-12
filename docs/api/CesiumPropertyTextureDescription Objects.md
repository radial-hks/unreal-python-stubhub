## CesiumPropertyTextureDescription Objects

```python
class CesiumPropertyTextureDescription(StructBase)
```

brief: Description of a property texture with properties that should be made accessible to Unreal materials.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
  brief: The name of this property texture.
- ``properties`` (Array[CesiumPropertyTexturePropertyDescription]):  [Read-Write]
  brief: Descriptions of the properties to upload to the GPU.

<a id="unreal.CesiumPropertyTextureDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumSubLevel"></a>