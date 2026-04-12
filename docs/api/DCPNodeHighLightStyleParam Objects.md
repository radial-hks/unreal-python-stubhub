## DCPNodeHighLightStyleParam Objects

```python
class DCPNodeHighLightStyleParam(ParamsBase)
```

DCPNode High Light Style Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_occluded`` (bool):  [Read-Write]
- ``color`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``opacity`` (float):  [Read-Write]
- ``opacity_scale`` (float):  [Read-Write]
- ``outline_style`` (NodeOutlineStyleParam):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(color: str = "",
             opacity: float = 0.000000,
             opacity_scale: float = 0.000000,
             can_be_occluded: bool = False,
             outline_style: NodeOutlineStyleParam = []) -> None
```

<a id="unreal.DCPNodeHighLightStyleParam.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.DCPNodeHighLightStyleParam.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.DCPNodeHighLightStyleParam.opacity_scale"></a>

#### opacity\_scale

```python
@property
def opacity_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.opacity_scale"></a>

#### opacity\_scale

```python
@opacity_scale.setter
def opacity_scale(value: float) -> None
```

<a id="unreal.DCPNodeHighLightStyleParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@property
def can_be_occluded() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.can_be_occluded"></a>

#### can\_be\_occluded

```python
@can_be_occluded.setter
def can_be_occluded(value: bool) -> None
```

<a id="unreal.DCPNodeHighLightStyleParam.outline_style"></a>

#### outline\_style

```python
@property
def outline_style() -> NodeOutlineStyleParam
```

(NodeOutlineStyleParam):  [Read-Write]

<a id="unreal.DCPNodeHighLightStyleParam.outline_style"></a>

#### outline\_style

```python
@outline_style.setter
def outline_style(value: NodeOutlineStyleParam) -> None
```

<a id="unreal.SetOtherNodesVisibilityParam"></a>