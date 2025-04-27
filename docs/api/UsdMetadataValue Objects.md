## UsdMetadataValue Objects

```python
class UsdMetadataValue(StructBase)
```

Describes a single metadata value collected from USD

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDMetadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``stringified_value`` (str):  [Read-Write] A stringified value that should match the type in TypeName (e.g. "[(1.0, 1.0, 0.5), (1.0, 1.0, 0.5)]" if
  TypeName is "double3[]").
  You can use the functions on UsdConversionLibrary (USDConversionLibrary.h) and UsdUtils namespace
  (USDValueConversion.h) to help stringify/unstringify these types according to USD rules, from C++,
  Blueprint and Python
- ``type_name`` (str):  [Read-Write] USD typename. Anything from the "Value type token" column on the Basic data types tables from
  https:openusd.org/release/api/_usd__page__datatypes.html is allowed, including
  the array types (e.g. "uchar", "timecode", "matrix3d[]" and "half[]").
  Exceptions are the "opaque" typeName that we don't support, and the "SdfListOp<Token>" typeName,
  that we *do* support (it's the typeName for list-editable attributes like "apiSchemas")

<a id="unreal.UsdMetadataValue.__init__"></a>

#### __init__

```python
def __init__(type_name: str = "", stringified_value: str = "") -> None
```

<a id="unreal.UsdMetadataValue.type_name"></a>

#### type_name

```python
@property
def type_name() -> str
```

(str):  [Read-Write] USD typename. Anything from the "Value type token" column on the Basic data types tables from
https:openusd.org/release/api/_usd__page__datatypes.html is allowed, including
the array types (e.g. "uchar", "timecode", "matrix3d[]" and "half[]").
Exceptions are the "opaque" typeName that we don't support, and the "SdfListOp<Token>" typeName,
that we *do* support (it's the typeName for list-editable attributes like "apiSchemas")

<a id="unreal.UsdMetadataValue.type_name"></a>

#### type_name

```python
@type_name.setter
def type_name(value: str) -> None
```

<a id="unreal.UsdMetadataValue.stringified_value"></a>

#### stringified_value

```python
@property
def stringified_value() -> str
```

(str):  [Read-Write] A stringified value that should match the type in TypeName (e.g. "[(1.0, 1.0, 0.5), (1.0, 1.0, 0.5)]" if
TypeName is "double3[]").
You can use the functions on UsdConversionLibrary (USDConversionLibrary.h) and UsdUtils namespace
(USDValueConversion.h) to help stringify/unstringify these types according to USD rules, from C++,
Blueprint and Python

<a id="unreal.UsdMetadataValue.stringified_value"></a>

#### stringified_value

```python
@stringified_value.setter
def stringified_value(value: str) -> None
```

<a id="unreal.UsdPrimMetadata"></a>