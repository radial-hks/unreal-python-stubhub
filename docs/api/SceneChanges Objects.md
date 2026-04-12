## SceneChanges Objects

```python
class SceneChanges(StructBase)
```

Scene Changes

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: TransactionMgr.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``added_eids`` (Array[int64]):  [Read-Write]
- ``removed_eids`` (Array[int64]):  [Read-Write]
- ``updated_entities`` (Map[int64, EntityChanges]):  [Read-Write]

<a id="unreal.SceneChanges.__init__"></a>

#### \_\_init\_\_

```python
def __init__(added_eids: Array[int] = [],
             removed_eids: Array[int] = [],
             updated_entities: Map[int, EntityChanges] = {}) -> None
```

<a id="unreal.SceneChanges.added_eids"></a>

#### added\_eids

```python
@property
def added_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.SceneChanges.added_eids"></a>

#### added\_eids

```python
@added_eids.setter
def added_eids(value: Array[int]) -> None
```

<a id="unreal.SceneChanges.removed_eids"></a>

#### removed\_eids

```python
@property
def removed_eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.SceneChanges.removed_eids"></a>

#### removed\_eids

```python
@removed_eids.setter
def removed_eids(value: Array[int]) -> None
```

<a id="unreal.SceneChanges.updated_entities"></a>

#### updated\_entities

```python
@property
def updated_entities() -> Map[int, EntityChanges]
```

(Map[int64, EntityChanges]):  [Read-Write]

<a id="unreal.SceneChanges.updated_entities"></a>

#### updated\_entities

```python
@updated_entities.setter
def updated_entities(value: Map[int, EntityChanges]) -> None
```

<a id="unreal.PresetUniqueEntityData"></a>