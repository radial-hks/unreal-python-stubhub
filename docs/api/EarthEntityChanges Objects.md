## EarthEntityChanges Objects

```python
class EarthEntityChanges(StructBase)
```

Earth Entity Changes

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthTransactionMgr.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atom_class_to_changes`` (Map[type(Class), EarthJsonObjectWrapper]):  [Read-Write]

<a id="unreal.EarthEntityChanges.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        atom_class_to_changes: Map[Class,
                                   EarthJsonObjectWrapper] = {}) -> None
```

<a id="unreal.EarthEntityChanges.atom_class_to_changes"></a>

#### atom\_class\_to\_changes

```python
@property
def atom_class_to_changes() -> Map[Class, EarthJsonObjectWrapper]
```

(Map[type(Class), EarthJsonObjectWrapper]):  [Read-Write]

<a id="unreal.EarthEntityChanges.atom_class_to_changes"></a>

#### atom\_class\_to\_changes

```python
@atom_class_to_changes.setter
def atom_class_to_changes(value: Map[Class, EarthJsonObjectWrapper]) -> None
```

<a id="unreal.EarthJsonObjectWrapper"></a>