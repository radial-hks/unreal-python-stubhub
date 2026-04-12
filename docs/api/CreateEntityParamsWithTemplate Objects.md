## CreateEntityParamsWithTemplate Objects

```python
class CreateEntityParamsWithTemplate(ParamsBase)
```

Create Entity Params with Template

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpSceneAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[WdpJsonObjectWrapper]):  [Read-Write]
- ``default_param`` (WdpJsonObjectWrapper):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``operations`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.CreateEntityParamsWithTemplate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: WdpJsonObjectWrapper = [],
             batch_params: Array[WdpJsonObjectWrapper] = [],
             operations: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.CreateEntityParamsWithTemplate.default_param"></a>

#### default\_param

```python
@property
def default_param() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.CreateEntityParamsWithTemplate.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.CreateEntityParamsWithTemplate.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[WdpJsonObjectWrapper]
```

(Array[WdpJsonObjectWrapper]):  [Read-Write]

<a id="unreal.CreateEntityParamsWithTemplate.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[WdpJsonObjectWrapper]) -> None
```

<a id="unreal.CreateEntityParamsWithTemplate.operations"></a>

#### operations

```python
@property
def operations() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.CreateEntityParamsWithTemplate.operations"></a>

#### operations

```python
@operations.setter
def operations(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.UpdateEntityParams"></a>