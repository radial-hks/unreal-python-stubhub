## GetAllEntityParams Objects

```python
class GetAllEntityParams(ParamsBase)
```

Get All Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_types`` (Array[Name]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GetAllEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_types: Array[Name] = []) -> None
```

<a id="unreal.GetAllEntityParams.entity_types"></a>

#### entity\_types

```python
@property
def entity_types() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.GetAllEntityParams.entity_types"></a>

#### entity\_types

```python
@entity_types.setter
def entity_types(value: Array[Name]) -> None
```

<a id="unreal.GetEntityDataParams"></a>