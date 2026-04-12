## CesiumPropertyTexturePropertyDescription Objects

```python
class CesiumPropertyTexturePropertyDescription(StructBase)
```

brief: Description of a property texture property that should be made accessible to Unreal materials. A property texture property's data is already available through a texture, so no additional encoding details need to be specified.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has_khr_texture_transform`` (bool):  [Read-Write] Whether this property texture property contains a KHR_texture_transform
  glTF extension.
- ``name`` (str):  [Read-Write] The name of this property. This will be how it is referenced in the
  material.
- ``property_details`` (CesiumMetadataPropertyDetails):  [Read-Write] Describes the underlying type of this property and other relevant
  information from its EXT_structural_metadata definition.

<a id="unreal.CesiumPropertyTexturePropertyDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.AnimationStateEntry"></a>