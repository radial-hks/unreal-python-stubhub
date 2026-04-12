## UpdateEntityParams Objects

```python
class UpdateEntityParams(ParamsBase)
```

Update Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid_to_new_entity_params`` (Map[int64, WdpJsonObjectWrapper]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``operations`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.UpdateEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid_to_new_entity_params: Map[int, WdpJsonObjectWrapper] = {},
             operations: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.UpdateEntityParams.eid_to_new_entity_params"></a>

#### eid\_to\_new\_entity\_params

```python
@property
def eid_to_new_entity_params() -> Map[int, WdpJsonObjectWrapper]
```

(Map[int64, WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.UpdateEntityParams.eid_to_new_entity_params"></a>

#### eid\_to\_new\_entity\_params

```python
@eid_to_new_entity_params.setter
def eid_to_new_entity_params(value: Map[int, WdpJsonObjectWrapper]) -> None
```

<a id="unreal.UpdateEntityParams.operations"></a>

#### operations

```python
@property
def operations() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.UpdateEntityParams.operations"></a>

#### operations

```python
@operations.setter
def operations(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.ClearSceneParams"></a>