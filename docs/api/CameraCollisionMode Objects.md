## CameraCollisionMode Objects

```python
class CameraCollisionMode(EnumBase)
```

相机碰撞模式 无碰撞/使用碰撞预设/使用算法/使用混合碰撞（物理+算法）

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

<a id="unreal.CameraCollisionMode.CCM_NO_COLLISION"></a>

#### CCM\_NO\_COLLISION

0: 无碰撞

<a id="unreal.CameraCollisionMode.CCM_PROFILE"></a>

#### CCM\_PROFILE

1: 使用碰撞profile

<a id="unreal.CameraCollisionMode.CCM_CUSTOM_BOUNDS"></a>

#### CCM\_CUSTOM\_BOUNDS

2: 使用边界点计算碰撞

<a id="unreal.CameraCollisionMode.CCM_MIXED"></a>

#### CCM\_MIXED

3: 同时使用边界点和碰撞profile

<a id="unreal.UserInputActionType"></a>