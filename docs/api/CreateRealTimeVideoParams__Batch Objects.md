## CreateRealTimeVideoParams\_Batch Objects

```python
class CreateRealTimeVideoParams_Batch(ParamsBase)
```

Create Real Time Video Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RealTimeVideoParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateRealTimeVideosParams]):  [Read-Write]
- ``default_param`` (CreateRealTimeVideosParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateRealTimeVideoParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateRealTimeVideosParams = [
    "",
    [
        "", [600.000000, 510.000000], [0.000000, 0.000000], 0.000000,
        [[0.000000, 0.000000], [0.000000, 0.000000], [0.000000, 0.000000],
         [0.000000, 0.000000]]
    ], 0
],
             batch_params: Array[CreateRealTimeVideosParams] = []) -> None
```

<a id="unreal.CreateRealTimeVideoParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateRealTimeVideosParams
```

(CreateRealTimeVideosParams):  [Read-Write]

<a id="unreal.CreateRealTimeVideoParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateRealTimeVideosParams) -> None
```

<a id="unreal.CreateRealTimeVideoParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateRealTimeVideosParams]
```

(Array[CreateRealTimeVideosParams]):  [Read-Write]

<a id="unreal.CreateRealTimeVideoParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateRealTimeVideosParams]) -> None
```

<a id="unreal.UpdateRealTimeVideoParams"></a>