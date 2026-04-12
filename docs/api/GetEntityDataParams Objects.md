## GetEntityDataParams Objects

```python
class GetEntityDataParams(ParamsBase)
```

Get Entity Data Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GetEntityDataParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = []) -> None
```

<a id="unreal.GetEntityDataParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.GetEntityDataParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.RemoveEntityParams"></a>