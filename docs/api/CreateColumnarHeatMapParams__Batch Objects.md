## CreateColumnarHeatMapParams\_Batch Objects

```python
class CreateColumnarHeatMapParams_Batch(ParamsBase)
```

Create Columnar Heat Map Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateColumnarHeatMapsParams]):  [Read-Write]
- ``default_param`` (CreateColumnarHeatMapsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateColumnarHeatMapParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateColumnarHeatMapsParams = [
    0, 0.000000,
    [
        "cube", 30.000000, [1.000000, 100.000000], 10.000000,
        [1.000000, 100.000000], False,
        ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
    ], [["", 40.000000]]
],
             batch_params: Array[CreateColumnarHeatMapsParams] = []) -> None
```

<a id="unreal.CreateColumnarHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateColumnarHeatMapsParams
```

(CreateColumnarHeatMapsParams):  [Read-Write]

<a id="unreal.CreateColumnarHeatMapParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateColumnarHeatMapsParams) -> None
```

<a id="unreal.CreateColumnarHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateColumnarHeatMapsParams]
```

(Array[CreateColumnarHeatMapsParams]):  [Read-Write]

<a id="unreal.CreateColumnarHeatMapParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateColumnarHeatMapsParams]) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams"></a>