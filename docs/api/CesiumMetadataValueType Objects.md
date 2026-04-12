## CesiumMetadataValueType Objects

```python
class CesiumMetadataValueType(StructBase)
```

Represents the true value type of a metadata value, akin to the property
types in EXT_structural_metadata.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataValueType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_type`` (CesiumMetadataComponentType):  [Read-Write] The component of the metadata property or value. Only applies when the type
  is a Scalar, VecN, or MatN type.
- ``is_array`` (bool):  [Read-Write] Whether or not this represents an array containing elements of the
  specified types.
- ``type`` (CesiumMetadataType):  [Read-Write] The type of the metadata property or value.

<a id="unreal.CesiumMetadataValueType.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: CesiumMetadataType = CesiumMetadataType.INVALID,
             component_type:
             CesiumMetadataComponentType = CesiumMetadataComponentType.NONE,
             is_array: bool = False) -> None
```

<a id="unreal.CesiumMetadataValueType.type"></a>

#### type

```python
@property
def type() -> CesiumMetadataType
```

(CesiumMetadataType):  [Read-Write] The type of the metadata property or value.

<a id="unreal.CesiumMetadataValueType.type"></a>

#### type

```python
@type.setter
def type(value: CesiumMetadataType) -> None
```

<a id="unreal.CesiumMetadataValueType.component_type"></a>

#### component\_type

```python
@property
def component_type() -> CesiumMetadataComponentType
```

(CesiumMetadataComponentType):  [Read-Write] The component of the metadata property or value. Only applies when the type
is a Scalar, VecN, or MatN type.

<a id="unreal.CesiumMetadataValueType.component_type"></a>

#### component\_type

```python
@component_type.setter
def component_type(value: CesiumMetadataComponentType) -> None
```

<a id="unreal.CesiumMetadataValueType.is_array"></a>

#### is\_array

```python
@property
def is_array() -> bool
```

(bool):  [Read-Write] Whether or not this represents an array containing elements of the
specified types.

<a id="unreal.CesiumMetadataValueType.is_array"></a>

#### is\_array

```python
@is_array.setter
def is_array(value: bool) -> None
```

<a id="unreal.CesiumModelMetadata"></a>