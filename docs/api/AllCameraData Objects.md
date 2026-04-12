## AllCameraData Objects

```python
class AllCameraData(TableRowBase)
```

完整的相机数据

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_data`` (CameraCollisionData):  [Read-Write] 碰撞限制参数
- ``core_camera_data`` (CoreCameraData):  [Read-Write] 核心数据，位置、旋转、FOV
- ``rotate_limit_data`` (CameraRotationLimitationData):  [Read-Write] 旋转限制参数
- ``zoom_limit_data`` (CameraZoomLimitationData):  [Read-Write] 缩放限制参数

<a id="unreal.AllCameraData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    core_camera_data: CoreCameraData = [[0.000000, 0.000000, 0.000000],
                                        [0.000000, 0.000000, 0.000000],
                                        90.000000,
                                        [0.000000, 0.000000, 0.000000]],
    rotate_limit_data: CameraRotationLimitationData = [
        -89.000000, 0.000000, -179.999985, 179.999985, False
    ],
    zoom_limit_data: CameraZoomLimitationData = [
        0.000000, 1000000.000000, 50.000000, 110.000000
    ],
    collision_data: CameraCollisionData = [
        CameraCollisionMode.CCM_NO_COLLISION, "NoCollision", [],
        GroundPositionMode.GPM_AVOID_ONLY
    ]
) -> None
```

<a id="unreal.AllCameraData.core_camera_data"></a>

#### core\_camera\_data

```python
@property
def core_camera_data() -> CoreCameraData
```

(CoreCameraData):  [Read-Write] 核心数据，位置、旋转、FOV

<a id="unreal.AllCameraData.core_camera_data"></a>

#### core\_camera\_data

```python
@core_camera_data.setter
def core_camera_data(value: CoreCameraData) -> None
```

<a id="unreal.AllCameraData.rotate_limit_data"></a>

#### rotate\_limit\_data

```python
@property
def rotate_limit_data() -> CameraRotationLimitationData
```

(CameraRotationLimitationData):  [Read-Write] 旋转限制参数

<a id="unreal.AllCameraData.rotate_limit_data"></a>

#### rotate\_limit\_data

```python
@rotate_limit_data.setter
def rotate_limit_data(value: CameraRotationLimitationData) -> None
```

<a id="unreal.AllCameraData.zoom_limit_data"></a>

#### zoom\_limit\_data

```python
@property
def zoom_limit_data() -> CameraZoomLimitationData
```

(CameraZoomLimitationData):  [Read-Write] 缩放限制参数

<a id="unreal.AllCameraData.zoom_limit_data"></a>

#### zoom\_limit\_data

```python
@zoom_limit_data.setter
def zoom_limit_data(value: CameraZoomLimitationData) -> None
```

<a id="unreal.AllCameraData.collision_data"></a>

#### collision\_data

```python
@property
def collision_data() -> CameraCollisionData
```

(CameraCollisionData):  [Read-Write] 碰撞限制参数

<a id="unreal.AllCameraData.collision_data"></a>

#### collision\_data

```python
@collision_data.setter
def collision_data(value: CameraCollisionData) -> None
```

<a id="unreal.CameraZoomLimitationData"></a>