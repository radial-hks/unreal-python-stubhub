## CreateText3DParams\_Batch Objects

```python
class CreateText3DParams_Batch(ParamsBase)
```

Create Text 3DParams Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Text3DAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateText3DsParams]):  [Read-Write]
- ``default_param`` (CreateText3DsParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateText3DParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateText3DsParams = [
    "", ["51WORLD", "CF4300FF", "plain", 0.200000, False, 1.000000], 0
],
             batch_params: Array[CreateText3DsParams] = []) -> None
```

<a id="unreal.CreateText3DParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateText3DsParams
```

(CreateText3DsParams):  [Read-Write]

<a id="unreal.CreateText3DParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateText3DsParams) -> None
```

<a id="unreal.CreateText3DParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateText3DsParams]
```

(Array[CreateText3DsParams]):  [Read-Write]

<a id="unreal.CreateText3DParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateText3DsParams]) -> None
```

<a id="unreal.Text3DUpdateParams"></a>