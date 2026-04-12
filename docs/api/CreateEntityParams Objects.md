## CreateEntityParams Objects

```python
class CreateEntityParams(ParamsBase)
```

Create Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``create_entity_params`` (Array[WdpJsonObjectWrapper]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``operations`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.CreateEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(create_entity_params: Array[WdpJsonObjectWrapper] = [],
             operations: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.CreateEntityParams.create_entity_params"></a>

#### create\_entity\_params

```python
@property
def create_entity_params() -> Array[WdpJsonObjectWrapper]
```

(Array[WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.CreateEntityParams.create_entity_params"></a>

#### create\_entity\_params

```python
@create_entity_params.setter
def create_entity_params(value: Array[WdpJsonObjectWrapper]) -> None
```

<a id="unreal.CreateEntityParams.operations"></a>

#### operations

```python
@property
def operations() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.CreateEntityParams.operations"></a>

#### operations

```python
@operations.setter
def operations(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.CreateEntityParamsWithTemplate"></a>