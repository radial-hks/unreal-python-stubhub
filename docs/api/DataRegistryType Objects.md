## DataRegistryType Objects

```python
class DataRegistryType(StructBase)
```

Wrapper struct to represent a global data registry, represented as an FName internally and implicitly convertible back and forth.
This exists so the blueprint API can understand it's not a normal FName.

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: DataRegistryId.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] The FName representing this type

<a id="unreal.DataRegistryType.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None") -> None
```

<a id="unreal.DataRegistryType.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The FName representing this type

<a id="unreal.DataRegistryType.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.DataRegistryType.is_valid"></a>

#### is\_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Returns true if this is a non-empty type, does not check if it is currently registered

Returns:
    bool:

<a id="unreal.DataRegistryType.to_string"></a>

#### to\_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts a Data Registry Type to a string. The other direction is not provided because it cannot be validated

Returns:
    str:

<a id="unreal.DataRegistryType.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

Returns true if this is a non-empty type, does not check if it is currently registered

<a id="unreal.DataRegistryType.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``DataRegistryType`` Returns true if the values are equal (A == B)

<a id="unreal.DataRegistryType.__ne__"></a>

#### \_\_ne\_\_

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``DataRegistryType`` Returns true if the values are not equal (A != B)

<a id="unreal.DataRegistryCachePolicy"></a>