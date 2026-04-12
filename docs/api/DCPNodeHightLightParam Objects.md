## DCPNodeHightLightParam Objects

```python
class DCPNodeHightLightParam(DCPNodeBaseParam)
```

DCPNode Hight Light Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exclusion`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``high_light_style`` (DCPNodeHighLightStyleParam):  [Read-Write]
- ``hightlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.DCPNodeHightLightParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    node_id: int = 0,
    hightlight: bool = False,
    exclusion: bool = False,
    high_light_style: DCPNodeHighLightStyleParam = [
        "000000", 0.500000, 0.100000, False, []
    ]
) -> None
```

<a id="unreal.DCPNodeHightLightParam.hightlight"></a>

#### hightlight

```python
@property
def hightlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeHightLightParam.hightlight"></a>

#### hightlight

```python
@hightlight.setter
def hightlight(value: bool) -> None
```

<a id="unreal.DCPNodeHightLightParam.exclusion"></a>

#### exclusion

```python
@property
def exclusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeHightLightParam.exclusion"></a>

#### exclusion

```python
@exclusion.setter
def exclusion(value: bool) -> None
```

<a id="unreal.DCPNodeHightLightParam.high_light_style"></a>

#### high\_light\_style

```python
@property
def high_light_style() -> DCPNodeHighLightStyleParam
```

(DCPNodeHighLightStyleParam):  [Read-Write]

<a id="unreal.DCPNodeHightLightParam.high_light_style"></a>

#### high\_light\_style

```python
@high_light_style.setter
def high_light_style(value: DCPNodeHighLightStyleParam) -> None
```

<a id="unreal.DCPNodeLevelParam"></a>