## CreateMoveAlongPathParams\_Batch Objects

```python
class CreateMoveAlongPathParams_Batch(ParamsBase)
```

Create Move Along Path Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateMoveAlongPathParams]):  [Read-Write]
- ``default_param`` (CreateMoveAlongPathParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateMoveAlongPathParams = [
    "", "", 5.000000, True, False
],
             batch_params: Array[CreateMoveAlongPathParams] = []) -> None
```

<a id="unreal.CreateMoveAlongPathParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateMoveAlongPathParams
```

(CreateMoveAlongPathParams):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateMoveAlongPathParams) -> None
```

<a id="unreal.CreateMoveAlongPathParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateMoveAlongPathParams]
```

(Array[CreateMoveAlongPathParams]):  [Read-Write]

<a id="unreal.CreateMoveAlongPathParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateMoveAlongPathParams]) -> None
```

<a id="unreal.UpdateMoveAlongPathParams"></a>