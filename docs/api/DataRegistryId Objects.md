## DataRegistryId Objects

```python
class DataRegistryId(StructBase)
```

Identifier for a specific DataRegistryItem, provides the user with a Tag or dropdown-based UI for selecting based on the available index info

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: DataRegistryId.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_name`` (Name):  [Read-Write] The name of this object, may be a leaf gameplay tag or a raw name depending on the type
- ``registry_type`` (DataRegistryType):  [Read-Write] The type of this item, used to look up the correct registry

<a id="unreal.DataRegistryId.__init__"></a>

#### \_\_init\_\_

```python
def __init__(registry_type: DataRegistryType = ["None"],
             item_name: Name = "None") -> None
```

<a id="unreal.DataRegistryId.registry_type"></a>

#### registry\_type

```python
@property
def registry_type() -> DataRegistryType
```

(DataRegistryType):  [Read-Write] The type of this item, used to look up the correct registry

<a id="unreal.DataRegistryId.registry_type"></a>

#### registry\_type

```python
@registry_type.setter
def registry_type(value: DataRegistryType) -> None
```

<a id="unreal.DataRegistryId.item_name"></a>

#### item\_name

```python
@property
def item_name() -> Name
```

(Name):  [Read-Write] The name of this object, may be a leaf gameplay tag or a raw name depending on the type

<a id="unreal.DataRegistryId.item_name"></a>

#### item\_name

```python
@item_name.setter
def item_name(value: Name) -> None
```

<a id="unreal.DataRegistryId.is_valid"></a>

#### is\_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Returns true if this is a non-empty item identifier, does not check if it is currently registered

Returns:
    bool:

<a id="unreal.DataRegistryId.to_string"></a>

#### to\_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts a Data Registry Id to a string. The other direction is not provided because it cannot be validated

Returns:
    str:

<a id="unreal.DataRegistryId.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

Returns true if this is a non-empty item identifier, does not check if it is currently registered

<a id="unreal.DataRegistryId.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``DataRegistryId`` Returns true if the values are equal (A == B)

<a id="unreal.DataRegistryId.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``DataRegistryId`` Returns true if the values are not equal (A != B)

<a id="unreal.DataRegistryType"></a>