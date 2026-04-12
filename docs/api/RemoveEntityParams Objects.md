## RemoveEntityParams Objects

```python
class RemoveEntityParams(ParamsBase)
```

Remove Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.RemoveEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[str] = []) -> None
```

<a id="unreal.RemoveEntityParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RemoveEntityParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.RemoveEntityByTypesParams"></a>