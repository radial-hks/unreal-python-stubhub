## GetRangeInfoRes Objects

```python
class GetRangeInfoRes(ResultBase)
```

Get Range Info Res

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RangeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``range_style`` (RangeStyle):  [Read-Write]
- ``range_world_points`` (WdpPolygon2D):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetRangeInfoRes.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    message: str = "",
    scene_change_info: WdpSceneChangeInfo = [[], [], []],
    success: bool = False,
    range_world_points: WdpPolygon2D = [[], []],
    range_style: RangeStyle = [
        "stripe", "solid", 10.000000, 1.000000, "6a5acdff"
    ]
) -> None
```

<a id="unreal.GetRangeInfoRes.range_world_points"></a>

#### range\_world\_points

```python
@property
def range_world_points() -> WdpPolygon2D
```

(WdpPolygon2D):  [Read-Write]

<a id="unreal.GetRangeInfoRes.range_world_points"></a>

#### range\_world\_points

```python
@range_world_points.setter
def range_world_points(value: WdpPolygon2D) -> None
```

<a id="unreal.GetRangeInfoRes.range_style"></a>

#### range\_style

```python
@property
def range_style() -> RangeStyle
```

(RangeStyle):  [Read-Write]

<a id="unreal.GetRangeInfoRes.range_style"></a>

#### range\_style

```python
@range_style.setter
def range_style(value: RangeStyle) -> None
```

<a id="unreal.RasterStyle"></a>