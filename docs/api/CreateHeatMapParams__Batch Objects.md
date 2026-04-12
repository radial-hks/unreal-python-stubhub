## CreateHeatMapParams\_Batch Objects

```python
class CreateHeatMapParams_Batch(ParamsBase)
```

Create Heat Map Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateHeatMapsParams]):  [Read-Write]
- ``default_param`` (CreateHeatMapsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateHeatMapParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateHeatMapsParams = [
    0, 0.000000,
    [
        "fit", 30.000000, [-1000000.000000, 1000000.000000],
        [1.000000, 100.000000],
        ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
    ], [["", 40.000000]]
],
             batch_params: Array[CreateHeatMapsParams] = []) -> None
```

<a id="unreal.CreateHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateHeatMapsParams
```

(CreateHeatMapsParams):  [Read-Write]

<a id="unreal.CreateHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateHeatMapsParams) -> None
```

<a id="unreal.CreateHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateHeatMapsParams]
```

(Array[CreateHeatMapsParams]):  [Read-Write]

<a id="unreal.CreateHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateHeatMapsParams]) -> None
```

<a id="unreal.UpdateHeatMapParams"></a>