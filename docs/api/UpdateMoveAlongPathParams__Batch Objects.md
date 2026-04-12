## UpdateMoveAlongPathParams\_Batch Objects

```python
class UpdateMoveAlongPathParams_Batch(ParamsBase)
```

Update Move Along Path Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[UpdateMoveAlongPathParams]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.UpdateMoveAlongPathParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(batch_params: Array[UpdateMoveAlongPathParams] = []) -> None
```

<a id="unreal.UpdateMoveAlongPathParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[UpdateMoveAlongPathParams]
```

(Array[UpdateMoveAlongPathParams]):  [Read-Write]

<a id="unreal.UpdateMoveAlongPathParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[UpdateMoveAlongPathParams]) -> None
```

<a id="unreal.OnMoveAlongPathEndEvent"></a>