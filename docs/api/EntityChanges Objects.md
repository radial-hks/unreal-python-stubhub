## EntityChanges Objects

```python
class EntityChanges(StructBase)
```

Entity Changes

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: TransactionMgr.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atom_class_to_changes`` (Map[type(Class), WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.EntityChanges.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        atom_class_to_changes: Map[Class, WdpJsonObjectWrapper] = {}) -> None
```

<a id="unreal.EntityChanges.atom_class_to_changes"></a>

#### atom\_class\_to\_changes

```python
@property
def atom_class_to_changes() -> Map[Class, WdpJsonObjectWrapper]
```

(Map[type(Class), WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.EntityChanges.atom_class_to_changes"></a>

#### atom\_class\_to\_changes

```python
@atom_class_to_changes.setter
def atom_class_to_changes(value: Map[Class, WdpJsonObjectWrapper]) -> None
```

<a id="unreal.SceneChanges"></a>