## WdpPickFilter Objects

```python
class WdpPickFilter(StructBase)
```

Wdp Pick Filter

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpPicker
- **File**: WdpPickFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exclude_entities`` (Set[int64]):  [Read-Write]
- ``filter_entity_types`` (Set[Name]):  [Read-Write]
- ``filter_for_exclude`` (bool):  [Read-Write] true: Exclude Entity Types, false : Include Entity Types

<a id="unreal.WdpPickFilter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filter_entity_types: Set[Name] = [],
             filter_for_exclude: bool = False,
             exclude_entities: Set[int] = []) -> None
```

<a id="unreal.WdpPickFilter.filter_entity_types"></a>

#### filter\_entity\_types

```python
@property
def filter_entity_types() -> Set[Name]
```

(Set[Name]):  [Read-Only]

<a id="unreal.WdpPickFilter.filter_for_exclude"></a>

#### filter\_for\_exclude

```python
@property
def filter_for_exclude() -> bool
```

(bool):  [Read-Only] true: Exclude Entity Types, false : Include Entity Types

<a id="unreal.WdpPickFilter.exclude_entities"></a>

#### exclude\_entities

```python
@property
def exclude_entities() -> Set[int]
```

(Set[int64]):  [Read-Only]

<a id="unreal.WdpPickResult"></a>