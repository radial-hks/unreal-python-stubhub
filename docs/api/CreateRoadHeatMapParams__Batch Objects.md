## CreateRoadHeatMapParams\_Batch Objects

```python
class CreateRoadHeatMapParams_Batch(ParamsBase)
```

Create Road Heat Map Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateRoadHeatMapsParams]):  [Read-Write]
- ``default_param`` (CreateRoadHeatMapsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateRoadHeatMapParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateRoadHeatMapsParams = [
    0,
    [
        "fit", 30.000000, [1.000000, 100.000000],
        ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"], ["water"]
    ], [["", 40.000000]]
],
             batch_params: Array[CreateRoadHeatMapsParams] = []) -> None
```

<a id="unreal.CreateRoadHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateRoadHeatMapsParams
```

(CreateRoadHeatMapsParams):  [Read-Write]

<a id="unreal.CreateRoadHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateRoadHeatMapsParams) -> None
```

<a id="unreal.CreateRoadHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateRoadHeatMapsParams]
```

(Array[CreateRoadHeatMapsParams]):  [Read-Write]

<a id="unreal.CreateRoadHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateRoadHeatMapsParams]) -> None
```

<a id="unreal.UpdateRoadHeatMapParams"></a>