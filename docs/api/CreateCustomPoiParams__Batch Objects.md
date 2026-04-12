## CreateCustomPoiParams\_Batch Objects

```python
class CreateCustomPoiParams_Batch(ParamsBase)
```

Create Custom Poi Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateCustomPoisParams]):  [Read-Write]
- ``default_param`` (CreateCustomPoisParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateCustomPoiParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateCustomPoisParams = [
    "",
    [[[0.000000, 0.000000], ["", ""]],
     ["", [0.000000, 0.000000], [0.000000, 0.000000], ["", "", 0]]], 0
],
             batch_params: Array[CreateCustomPoisParams] = []) -> None
```

<a id="unreal.CreateCustomPoiParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateCustomPoisParams
```

(CreateCustomPoisParams):  [Read-Write]

<a id="unreal.CreateCustomPoiParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateCustomPoisParams) -> None
```

<a id="unreal.CreateCustomPoiParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateCustomPoisParams]
```

(Array[CreateCustomPoisParams]):  [Read-Write]

<a id="unreal.CreateCustomPoiParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateCustomPoisParams]) -> None
```

<a id="unreal.UpdateCustomPoiParams"></a>