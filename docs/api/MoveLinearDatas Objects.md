## MoveLinearDatas Objects

```python
class MoveLinearDatas(ParamsBase)
```

Move Linear Datas

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: MoveLinearAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data`` (Array[MoveLinearData]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``operations`` (WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.MoveLinearDatas.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data: Array[MoveLinearData] = [],
             operations: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.MoveLinearDatas.data"></a>

#### data

```python
@property
def data() -> Array[MoveLinearData]
```

(Array[MoveLinearData]):  [Read-Write]

<a id="unreal.MoveLinearDatas.data"></a>

#### data

```python
@data.setter
def data(value: Array[MoveLinearData]) -> None
```

<a id="unreal.MoveLinearDatas.operations"></a>

#### operations

```python
@property
def operations() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.MoveLinearDatas.operations"></a>

#### operations

```python
@operations.setter
def operations(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.ParabolaStyle"></a>