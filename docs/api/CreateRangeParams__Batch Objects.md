## CreateRangeParams\_Batch Objects

```python
class CreateRangeParams_Batch(ParamsBase)
```

Create Range Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RangeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateRangesParams]):  [Read-Write]
- ``default_param`` (CreateRangesParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateRangeParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateRangesParams = [
    "", 0, 0.000000, ["stripe", "solid", 10.000000, 1.000000, "6a5acdff"]
],
             batch_params: Array[CreateRangesParams] = []) -> None
```

<a id="unreal.CreateRangeParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateRangesParams
```

(CreateRangesParams):  [Read-Write]

<a id="unreal.CreateRangeParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateRangesParams) -> None
```

<a id="unreal.CreateRangeParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateRangesParams]
```

(Array[CreateRangesParams]):  [Read-Write]

<a id="unreal.CreateRangeParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateRangesParams]) -> None
```

<a id="unreal.UpdateRangeParams"></a>