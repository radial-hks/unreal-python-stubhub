## PrimaryAssetType Objects

```python
class PrimaryAssetType(StructBase)
```

A type of primary asset, used by the Asset Manager system.
note: The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\PrimaryAssetId.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] The Type of this object, by default its base class's name

<a id="unreal.PrimaryAssetType.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None") -> None
```

<a id="unreal.PrimaryAssetType.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The Type of this object, by default its base class's name

<a id="unreal.PrimaryAssetType.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.PrimaryAssetType.is_valid"></a>

#### is\_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Returns list of Primary Asset Ids for a PrimaryAssetType

Returns:
    bool:

<a id="unreal.PrimaryAssetType.get_primary_asset_id_list"></a>

#### get\_primary\_asset\_id\_list

```python
def get_primary_asset_id_list() -> Array[PrimaryAssetId]
```

x.get_primary_asset_id_list() -> Array[PrimaryAssetId]
Returns list of PrimaryAssetIds for a PrimaryAssetType

Returns:
    Array[PrimaryAssetId]: 

    out_primary_asset_id_list (Array[PrimaryAssetId]):

<a id="unreal.PrimaryAssetType.to_string"></a>

#### to\_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

Returns:
    str:

<a id="unreal.PrimaryAssetType.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

Returns list of Primary Asset Ids for a PrimaryAssetType

<a id="unreal.PrimaryAssetType.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``PrimaryAssetType`` Returns true if the values are equal (A == B)

<a id="unreal.PrimaryAssetType.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``PrimaryAssetType`` Returns true if the values are not equal (A != B)

<a id="unreal.QualifiedTime"></a>