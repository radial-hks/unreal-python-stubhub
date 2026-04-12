## CreatePoiParams\_Batch Objects

```python
class CreatePoiParams_Batch(ParamsBase)
```

Create Poi Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreatePoisParams]):  [Read-Write]
- ``default_param`` (CreatePoisParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreatePoiParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreatePoisParams = [
    "",
    [[[0.000000, 0.000000], ["", ""]],
     ["", [0.000000, 0.000000], [0.000000, 0.000000], ["", "", 0]]], 0
],
             batch_params: Array[CreatePoisParams] = []) -> None
```

<a id="unreal.CreatePoiParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreatePoisParams
```

(CreatePoisParams):  [Read-Write]

<a id="unreal.CreatePoiParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreatePoisParams) -> None
```

<a id="unreal.CreatePoiParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreatePoisParams]
```

(Array[CreatePoisParams]):  [Read-Write]

<a id="unreal.CreatePoiParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreatePoisParams]) -> None
```

<a id="unreal.UpdatePoiParams"></a>