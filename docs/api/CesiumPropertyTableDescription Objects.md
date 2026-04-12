## CesiumPropertyTableDescription Objects

```python
class CesiumPropertyTableDescription(StructBase)
```

brief: Description of a property table containing properties to be encoded for access in Unreal materials.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
  brief: The name of this property table. If this property table has no name in the EXT_structural_metadata extension, then its class name is used instead.
- ``properties`` (Array[CesiumPropertyTablePropertyDescription]):  [Read-Write]
  brief: Descriptions of the properties to upload to the GPU.

<a id="unreal.CesiumPropertyTableDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumPropertyTextureDescription"></a>