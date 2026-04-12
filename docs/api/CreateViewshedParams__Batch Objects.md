## CreateViewshedParams\_Batch Objects

```python
class CreateViewshedParams_Batch(ParamsBase)
```

Create Viewshed Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ViewShedAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateViewshedsParams]):  [Read-Write]
- ``default_param`` (CreateViewshedsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateViewshedParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateViewshedsParams = [
    "", 0, ["00FF00FF", "FF0000FF", True, 70.000000, 100.000000]
],
             batch_params: Array[CreateViewshedsParams] = []) -> None
```

<a id="unreal.CreateViewshedParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateViewshedsParams
```

(CreateViewshedsParams):  [Read-Write]

<a id="unreal.CreateViewshedParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateViewshedsParams) -> None
```

<a id="unreal.CreateViewshedParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateViewshedsParams]
```

(Array[CreateViewshedsParams]):  [Read-Write]

<a id="unreal.CreateViewshedParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateViewshedsParams]) -> None
```

<a id="unreal.UpdateViewshedParams"></a>