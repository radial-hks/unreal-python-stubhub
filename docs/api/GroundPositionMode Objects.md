## GroundPositionMode Objects

```python
class GroundPositionMode(EnumBase)
```

地面检测模式 不检测/保持相对高度/只在碰撞时改变高度
需要重新考虑这个逻辑

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

<a id="unreal.GroundPositionMode.GPM_NO_COLLISION"></a>

#### GPM\_NO\_COLLISION

0: 不检测地面

<a id="unreal.GroundPositionMode.GPM_KEEP_RELATIVE_HEIGHT"></a>

#### GPM\_KEEP\_RELATIVE\_HEIGHT

1: 保持相对地面高度

<a id="unreal.GroundPositionMode.GPM_AVOID_ONLY"></a>

#### GPM\_AVOID\_ONLY

2: 只在碰撞时改变高度

<a id="unreal.CameraCollisionMode"></a>