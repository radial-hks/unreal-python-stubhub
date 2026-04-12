## CesiumFeatureIdSetDescription Objects

```python
class CesiumFeatureIdSetDescription(StructBase)
```

brief: Description of a feature ID set from EXT_mesh_features.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has_khr_texture_transform`` (bool):  [Read-Write] Whether this feature ID set contains a KHR_texture_transform glTF
  extension. Only applicable if the feature ID set is a feature ID texture.
- ``has_null_feature_id`` (bool):  [Read-Write] The null feature ID for the feature ID set. This value indicates that no
  feature is associated with the vertex or texel containing the value. If no
  such value is specified, this defaults to -1, which prevents it from being
  unnecessarily included in the generated material.
- ``name`` (str):  [Read-Write] The display name of the feature ID set. If the feature ID set already has a
  label, this will use the label. Otherwise, if the feature ID set is
  unlabeled, a name will be generated like so:

  - If the feature ID set is an attribute, this will appear as
  "_FEATURE_ID_<index>", where <index> is the set index specified in
  the attribute.
  - If the feature ID set is a texture, this will appear as
  "_FEATURE_ID_TEXTURE_<index>", where <index> increments with the number of
  feature ID textures seen in an individual primitive.
  - If the feature ID set is an implicit set, this will appear as
  "_IMPLICIT_FEATURE_ID". Implicit feature ID sets don't vary in definition,
  so any additional implicit feature ID sets across the primitives are
  counted by this one.

  This name will also be used to represent the feature ID set in the
  generated material.
- ``property_table_name`` (str):  [Read-Write] The name of the property table that this feature ID set corresponds to.
- ``type`` (CesiumFeatureIdSetType):  [Read-Write] The type of the feature ID set.

<a id="unreal.CesiumFeatureIdSetDescription.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumPropertyTableDescription"></a>