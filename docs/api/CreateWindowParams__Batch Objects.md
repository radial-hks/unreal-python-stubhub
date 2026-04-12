## CreateWindowParams\_Batch Objects

```python
class CreateWindowParams_Batch(ParamsBase)
```

Create Window Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: WindowAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateWindowsParams]):  [Read-Write]
- ``default_param`` (CreateWindowsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateWindowParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateWindowsParams = [
    "", ["", [600.000000, 510.000000], [0.000000, 0.000000]], 0
],
             batch_params: Array[CreateWindowsParams] = []) -> None
```

<a id="unreal.CreateWindowParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateWindowsParams
```

(CreateWindowsParams):  [Read-Write]

<a id="unreal.CreateWindowParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateWindowsParams) -> None
```

<a id="unreal.CreateWindowParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateWindowsParams]
```

(Array[CreateWindowsParams]):  [Read-Write]

<a id="unreal.CreateWindowParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateWindowsParams]) -> None
```

<a id="unreal.UpdateWindowParams"></a>