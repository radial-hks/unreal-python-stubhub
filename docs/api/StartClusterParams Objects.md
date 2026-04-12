## StartClusterParams Objects

```python
class StartClusterParams(ParamsBase)
```

Start Cluster Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ClusterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aggregation_limit`` (int32):  [Read-Write]
- ``algorithm`` (WdpJsonObjectWrapper):  [Read-Write]
- ``filters`` (WdpJsonObjectWrapper):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``mode`` (str):  [Read-Write]
- ``open_on_click`` (bool):  [Read-Write]
- ``url`` (str):  [Read-Write]

<a id="unreal.StartClusterParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(open_on_click: bool = False,
             url: str = "",
             mode: str = "",
             aggregation_limit: int = 0,
             algorithm: WdpJsonObjectWrapper = [],
             filters: WdpJsonObjectWrapper = []) -> None
```

<a id="unreal.StartClusterParams.open_on_click"></a>

#### open\_on\_click

```python
@property
def open_on_click() -> bool
```

(bool):  [Read-Write]

<a id="unreal.StartClusterParams.open_on_click"></a>

#### open\_on\_click

```python
@open_on_click.setter
def open_on_click(value: bool) -> None
```

<a id="unreal.StartClusterParams.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write]

<a id="unreal.StartClusterParams.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.StartClusterParams.mode"></a>

#### mode

```python
@property
def mode() -> str
```

(str):  [Read-Write]

<a id="unreal.StartClusterParams.mode"></a>

#### mode

```python
@mode.setter
def mode(value: str) -> None
```

<a id="unreal.StartClusterParams.aggregation_limit"></a>

#### aggregation\_limit

```python
@property
def aggregation_limit() -> int
```

(int32):  [Read-Write]

<a id="unreal.StartClusterParams.aggregation_limit"></a>

#### aggregation\_limit

```python
@aggregation_limit.setter
def aggregation_limit(value: int) -> None
```

<a id="unreal.StartClusterParams.algorithm"></a>

#### algorithm

```python
@property
def algorithm() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.StartClusterParams.algorithm"></a>

#### algorithm

```python
@algorithm.setter
def algorithm(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.StartClusterParams.filters"></a>

#### filters

```python
@property
def filters() -> WdpJsonObjectWrapper
```

(WdpJsonObjectWrapper):  [Read-Write]

<a id="unreal.StartClusterParams.filters"></a>

#### filters

```python
@filters.setter
def filters(value: WdpJsonObjectWrapper) -> None
```

<a id="unreal.UpdateClusterParams"></a>