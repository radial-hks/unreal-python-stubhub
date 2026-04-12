## CreateParabolaParams\_Batch Objects

```python
class CreateParabolaParams_Batch(ParamsBase)
```

Create Parabola Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ParabolaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateParabolasParams]):  [Read-Write]
- ``default_param`` (CreateParabolasParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateParabolaParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateParabolasParams = [
    "", "", ["arrow", 10.000000, 0.300000, 10.000000, "aaff00ff", False], 0
],
             batch_params: Array[CreateParabolasParams] = []) -> None
```

<a id="unreal.CreateParabolaParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateParabolasParams
```

(CreateParabolasParams):  [Read-Write]

<a id="unreal.CreateParabolaParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateParabolasParams) -> None
```

<a id="unreal.CreateParabolaParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateParabolasParams]
```

(Array[CreateParabolasParams]):  [Read-Write]

<a id="unreal.CreateParabolaParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateParabolasParams]) -> None
```

<a id="unreal.UpdateParabolaParams"></a>