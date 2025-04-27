## PCGMatchAndSetByAttribute Objects

```python
class PCGMatchAndSetByAttribute(PCGMatchAndSetBase)
```

This Match & Set object looks up an attribute on a given point,
then looks up its entries to find a match; if there is one, then it sets it value.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetByAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[PCGMatchAndSetByAttributeEntry]):  [Read-Write] Lookup entries (key-value pairs)
- ``match_source_attribute`` (Name):  [Read-Write] Attribute to match on the data
- ``match_source_type`` (PCGMetadataTypes):  [Read-Write] Type of the attribute to match against.

<a id="unreal.PCGMatchAndSetByAttribute.match_source_attribute"></a>

#### match_source_attribute

```python
@property
def match_source_attribute() -> Name
```

(Name):  [Read-Write] Attribute to match on the data

<a id="unreal.PCGMatchAndSetByAttribute.match_source_attribute"></a>

#### match_source_attribute

```python
@match_source_attribute.setter
def match_source_attribute(value: Name) -> None
```

<a id="unreal.PCGMatchAndSetByAttribute.match_source_type"></a>

#### match_source_type

```python
@property
def match_source_type() -> PCGMetadataTypes
```

(PCGMetadataTypes):  [Read-Write] Type of the attribute to match against.

<a id="unreal.PCGMatchAndSetByAttribute.match_source_type"></a>

#### match_source_type

```python
@match_source_type.setter
def match_source_type(value: PCGMetadataTypes) -> None
```

<a id="unreal.PCGMatchAndSetByAttribute.entries"></a>

#### entries

```python
@property
def entries() -> Array[PCGMatchAndSetByAttributeEntry]
```

(Array[PCGMatchAndSetByAttributeEntry]):  [Read-Write] Lookup entries (key-value pairs)

<a id="unreal.PCGMatchAndSetByAttribute.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[PCGMatchAndSetByAttributeEntry]) -> None
```

<a id="unreal.PCGMatchAndSetWeighted"></a>