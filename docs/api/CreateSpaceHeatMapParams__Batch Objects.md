## CreateSpaceHeatMapParams\_Batch Objects

```python
class CreateSpaceHeatMapParams_Batch(ParamsBase)
```

Create Space Heat Map Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SpaceHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateSpaceHeatMapsParams]):  [Read-Write]
- ``default_param`` (CreateSpaceHeatMapsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateSpaceHeatMapParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateSpaceHeatMapsParams = [
    0,
    [
        30.000000, [1.000000, 100.000000],
        ["000000", "000303", "051900", "593A00", "FF0000"]
    ], [["", 40.000000]]
],
             batch_params: Array[CreateSpaceHeatMapsParams] = []) -> None
```

<a id="unreal.CreateSpaceHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateSpaceHeatMapsParams
```

(CreateSpaceHeatMapsParams):  [Read-Write]

<a id="unreal.CreateSpaceHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateSpaceHeatMapsParams) -> None
```

<a id="unreal.CreateSpaceHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateSpaceHeatMapsParams]
```

(Array[CreateSpaceHeatMapsParams]):  [Read-Write]

<a id="unreal.CreateSpaceHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateSpaceHeatMapsParams]) -> None
```

<a id="unreal.UpdateSpaceHeatMapParams"></a>