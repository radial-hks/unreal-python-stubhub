## CesiumPropertyTablePropertyDescription Objects

```python
class CesiumPropertyTablePropertyDescription(StructBase)
```

brief: Description of a property table property that should be encoded for access on the GPU.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``encoding_details`` (CesiumMetadataEncodingDetails):  [Read-Write] Describes how the property will be encoded as data on the GPU, if possible.
- ``name`` (str):  [Read-Write] The name of this property. This will be how it is referenced in the
  material.
- ``property_details`` (CesiumMetadataPropertyDetails):  [Read-Write] Describes the underlying type of this property and other relevant
  information from its EXT_structural_metadata definition. Not all types of
  properties can be encoded to the GPU, or coerced to GPU-compatible types.

<a id="unreal.CesiumPropertyTablePropertyDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumPropertyTexturePropertyDescription"></a>