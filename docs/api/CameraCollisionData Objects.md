## CameraCollisionData Objects

```python
class CameraCollisionData(StructBase)
```

相机碰撞数据

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_mode`` (CameraCollisionMode):  [Read-Write] 碰撞模式
- ``collision_profile`` (Name):  [Read-Write] 碰撞检测profile名称
- ``custom_points`` (Array[Vector]):  [Read-Write] 数据碰撞限制边界点
- ``ground_position_mode`` (GroundPositionMode):  [Read-Write] 追踪地面时模式

<a id="unreal.CameraCollisionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    collision_mode: CameraCollisionMode = CameraCollisionMode.CCM_NO_COLLISION,
    collision_profile: Name = "None",
    custom_points: Array[Vector] = [],
    ground_position_mode: GroundPositionMode = GroundPositionMode.
    GPM_NO_COLLISION
) -> None
```

<a id="unreal.CameraCollisionData.collision_mode"></a>

#### collision\_mode

```python
@property
def collision_mode() -> CameraCollisionMode
```

(CameraCollisionMode):  [Read-Write] 碰撞模式

<a id="unreal.CameraCollisionData.collision_mode"></a>

#### collision\_mode

```python
@collision_mode.setter
def collision_mode(value: CameraCollisionMode) -> None
```

<a id="unreal.CameraCollisionData.collision_profile"></a>

#### collision\_profile

```python
@property
def collision_profile() -> Name
```

(Name):  [Read-Write] 碰撞检测profile名称

<a id="unreal.CameraCollisionData.collision_profile"></a>

#### collision\_profile

```python
@collision_profile.setter
def collision_profile(value: Name) -> None
```

<a id="unreal.CameraCollisionData.custom_points"></a>

#### custom\_points

```python
@property
def custom_points() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] 数据碰撞限制边界点

<a id="unreal.CameraCollisionData.custom_points"></a>

#### custom\_points

```python
@custom_points.setter
def custom_points(value: Array[Vector]) -> None
```

<a id="unreal.CameraCollisionData.ground_position_mode"></a>

#### ground\_position\_mode

```python
@property
def ground_position_mode() -> GroundPositionMode
```

(GroundPositionMode):  [Read-Write] 追踪地面时模式

<a id="unreal.CameraCollisionData.ground_position_mode"></a>

#### ground\_position\_mode

```python
@ground_position_mode.setter
def ground_position_mode(value: GroundPositionMode) -> None
```

<a id="unreal.TableRowBase"></a>