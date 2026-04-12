## ClearSceneParams Objects

```python
class ClearSceneParams(ParamsBase)
```

Clear Scene Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_types_to_ignore`` (Set[Name]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.ClearSceneParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_types_to_ignore: Set[Name] = []) -> None
```

<a id="unreal.ClearSceneParams.entity_types_to_ignore"></a>

#### entity\_types\_to\_ignore

```python
@property
def entity_types_to_ignore() -> Set[Name]
```

(Set[Name]):  [Read-Write]

<a id="unreal.ClearSceneParams.entity_types_to_ignore"></a>

#### entity\_types\_to\_ignore

```python
@entity_types_to_ignore.setter
def entity_types_to_ignore(value: Set[Name]) -> None
```

<a id="unreal.TransactionParams"></a>