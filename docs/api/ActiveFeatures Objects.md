## ActiveFeatures Objects

```python
class ActiveFeatures(EnumBase)
```

开启的操作功能，使用bitmask

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

<a id="unreal.ActiveFeatures.KEY_MOVEMENT"></a>

#### KEY\_MOVEMENT

1: 1按键平面移动

<a id="unreal.ActiveFeatures.KEY_MOVEMENT_UP_DOWN"></a>

#### KEY\_MOVEMENT\_UP\_DOWN

2: 2按键上下移动

<a id="unreal.ActiveFeatures.DRAG_MOVEMENT"></a>

#### DRAG\_MOVEMENT

4: 3鼠标拖动移动

<a id="unreal.ActiveFeatures.ROTATION"></a>

#### ROTATION

8: 4旋转镜头

<a id="unreal.ActiveFeatures.ZOOM"></a>

#### ZOOM

16: 5滚轮缩放

<a id="unreal.ActiveFeatures.TERRAIN_HEIGHT_ADAPTATION"></a>

#### TERRAIN\_HEIGHT\_ADAPTATION

32: 6地形高度自适应

<a id="unreal.ActiveFeatures.FOLLOW_ACTOR"></a>

#### FOLLOW\_ACTOR

64: 7追踪Actor

<a id="unreal.ActiveFeatures.AUTO_MOVEMENT"></a>

#### AUTO\_MOVEMENT

128: 8自动移动

<a id="unreal.ActiveFeatures.AUTO_ROTATION"></a>

#### AUTO\_ROTATION

256: 9自动绕点旋转

<a id="unreal.ActiveFeatures.AUTO_SELF_ROTATION"></a>

#### AUTO\_SELF\_ROTATION

512: 10相机自身旋转

<a id="unreal.ActiveFeatures.DOUBLE_CLICK"></a>

#### DOUBLE\_CLICK

1024: 11双击操作

<a id="unreal.CameraMode"></a>