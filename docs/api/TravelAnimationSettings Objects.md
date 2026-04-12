## TravelAnimationSettings Objects

```python
class TravelAnimationSettings(StructBase)
```

相机Travel动画的配置

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_scale`` (float):  [Read-Write] 曲线的弧度，数值越大，飞起的高度越高，0为直线，1为将起点终点的切线抬高XY距离的倍率
- ``e_animation_blend_features`` (int32):  [Read-Write] 启用哪些动画过度的功能，可以只使用一部分
- ``path`` (Map[float, Vector]):  [Read-Write] 如果过度类型为CustomPath，则会根据这个数据创建一条spline来过度相机
- ``travel_anim_type`` (TravelAnimType):  [Read-Write] 相机过度动画的方式

<a id="unreal.TravelAnimationSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(e_animation_blend_features: int = 0,
             travel_anim_type: TravelAnimType = TravelAnimType.TAT_LINEAR,
             curve_scale: float = 0.000000,
             path: Map[float, Vector] = {}) -> None
```

<a id="unreal.TravelAnimationSettings.e_animation_blend_features"></a>

#### e\_animation\_blend\_features

```python
@property
def e_animation_blend_features() -> int
```

(int32):  [Read-Write] 启用哪些动画过度的功能，可以只使用一部分

<a id="unreal.TravelAnimationSettings.e_animation_blend_features"></a>

#### e\_animation\_blend\_features

```python
@e_animation_blend_features.setter
def e_animation_blend_features(value: int) -> None
```

<a id="unreal.TravelAnimationSettings.travel_anim_type"></a>

#### travel\_anim\_type

```python
@property
def travel_anim_type() -> TravelAnimType
```

(TravelAnimType):  [Read-Write] 相机过度动画的方式

<a id="unreal.TravelAnimationSettings.travel_anim_type"></a>

#### travel\_anim\_type

```python
@travel_anim_type.setter
def travel_anim_type(value: TravelAnimType) -> None
```

<a id="unreal.TravelAnimationSettings.curve_scale"></a>

#### curve\_scale

```python
@property
def curve_scale() -> float
```

(float):  [Read-Write] 曲线的弧度，数值越大，飞起的高度越高，0为直线，1为将起点终点的切线抬高XY距离的倍率

<a id="unreal.TravelAnimationSettings.curve_scale"></a>

#### curve\_scale

```python
@curve_scale.setter
def curve_scale(value: float) -> None
```

<a id="unreal.TravelAnimationSettings.path"></a>

#### path

```python
@property
def path() -> Map[float, Vector]
```

(Map[float, Vector]):  [Read-Write] 如果过度类型为CustomPath，则会根据这个数据创建一条spline来过度相机

<a id="unreal.TravelAnimationSettings.path"></a>

#### path

```python
@path.setter
def path(value: Map[float, Vector]) -> None
```

<a id="unreal.AutoSelfRotationSettings"></a>