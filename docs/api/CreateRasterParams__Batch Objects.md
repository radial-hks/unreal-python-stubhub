## CreateRasterParams\_Batch Objects

```python
class CreateRasterParams_Batch(ParamsBase)
```

Create Raster Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RasterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateRastersParams]):  [Read-Write]
- ``default_param`` (CreateRastersParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateRasterParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateRastersParams = [
    0, 0.000000,
    [
        "http://superapi.51hitech.com/doc-static/images/static/raster/raster.tif",
        "fit", ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
    ]
],
             batch_params: Array[CreateRastersParams] = []) -> None
```

<a id="unreal.CreateRasterParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateRastersParams
```

(CreateRastersParams):  [Read-Write]

<a id="unreal.CreateRasterParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateRastersParams) -> None
```

<a id="unreal.CreateRasterParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateRastersParams]
```

(Array[CreateRastersParams]):  [Read-Write]

<a id="unreal.CreateRasterParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateRastersParams]) -> None
```

<a id="unreal.UpdateRasterParams"></a>