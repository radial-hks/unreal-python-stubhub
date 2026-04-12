## CesiumMetadataPropertyDetails Objects

```python
class CesiumMetadataPropertyDetails(StructBase)
```

Represents information about a metadata property according to how the
property is defined in EXT_structural_metadata.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataPropertyDetails.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``array_size`` (int64):  [Read-Write] The size of the arrays in the metadata property. If the property contains
  arrays of varying length, this will be zero even though bIsArray will be
  true> If this property does not contain arrays, this is set to zero.
- ``component_type`` (CesiumMetadataComponentType):  [Read-Write] The component of the metadata property. Only applies when the type is a
  Scalar, VecN, or MatN type.
- ``has_default_value`` (bool):  [Read-Write] Whether or not the property specifies a default value. This default value
  is used use when encountering a "no data" value in the property, or when a
  non-required property has been omitted.
- ``has_no_data_value`` (bool):  [Read-Write] Whether or not the property specifies a "no data" value. This value
  functions a sentinel value, indicating missing data wherever it appears.
- ``has_offset`` (bool):  [Read-Write] Whether or not the property is transformed by an offset. This value is
  defined either in the class property, or in the instance of the property
  itself.
- ``has_scale`` (bool):  [Read-Write] Whether or not the property is transformed by a scale. This value is
  defined either in the class property, or in the instance of the property
  itself.
- ``is_array`` (bool):  [Read-Write] Whether or not this represents an array containing elements of the
  specified types.
- ``is_normalized`` (bool):  [Read-Write] Whether or not the values in this property are normalized. Only applicable
  to scalar, vecN, and matN types with integer components.

  For unsigned integer component types, values are normalized between
  [0.0, 1.0]. For signed integer component types, values are normalized
  between [-1.0, 1.0]
- ``type`` (CesiumMetadataType):  [Read-Write] The type of the metadata property.

<a id="unreal.CesiumMetadataPropertyDetails.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CesiumMetadataPrimitive"></a>