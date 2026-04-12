## UpdateClusterParams Objects

```python
class UpdateClusterParams(ParamsBase)
```

Update Cluster Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ClusterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aggregation_limit`` (int32):  [Read-Write]
- ``attr`` (Array[UpdateAttrParams]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``open_on_click`` (bool):  [Read-Write]

<a id="unreal.UpdateClusterParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(open_on_click: bool = False,
             aggregation_limit: int = 0,
             attr: Array[UpdateAttrParams] = []) -> None
```

<a id="unreal.UpdateClusterParams.open_on_click"></a>

#### open\_on\_click

```python
@property
def open_on_click() -> bool
```

(bool):  [Read-Write]

<a id="unreal.UpdateClusterParams.open_on_click"></a>

#### open\_on\_click

```python
@open_on_click.setter
def open_on_click(value: bool) -> None
```

<a id="unreal.UpdateClusterParams.aggregation_limit"></a>

#### aggregation\_limit

```python
@property
def aggregation_limit() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateClusterParams.aggregation_limit"></a>

#### aggregation\_limit

```python
@aggregation_limit.setter
def aggregation_limit(value: int) -> None
```

<a id="unreal.UpdateClusterParams.attr"></a>

#### attr

```python
@property
def attr() -> Array[UpdateAttrParams]
```

(Array[UpdateAttrParams]):  [Read-Write]

<a id="unreal.UpdateClusterParams.attr"></a>

#### attr

```python
@attr.setter
def attr(value: Array[UpdateAttrParams]) -> None
```

<a id="unreal.ColumnarHeatMapData"></a>