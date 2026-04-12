## CreatePathParams\_Batch Objects

```python
class CreatePathParams_Batch(ParamsBase)
```

Create Path Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PathAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreatePathsParams]):  [Read-Write]
- ``default_param`` (CreatePathsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreatePathParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreatePathsParams = [
    "", ["arrow", 10.000000, "aaff00ff", "00FBFFFF"], 0
],
             batch_params: Array[CreatePathsParams] = []) -> None
```

<a id="unreal.CreatePathParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreatePathsParams
```

(CreatePathsParams):  [Read-Write]

<a id="unreal.CreatePathParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreatePathsParams) -> None
```

<a id="unreal.CreatePathParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreatePathsParams]
```

(Array[CreatePathsParams]):  [Read-Write]

<a id="unreal.CreatePathParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreatePathsParams]) -> None
```

<a id="unreal.UpdatePathParams"></a>