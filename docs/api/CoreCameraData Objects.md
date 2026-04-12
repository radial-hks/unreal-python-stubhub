## CoreCameraData Objects

```python
class CoreCameraData(StructBase)
```

核心相机数据

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_location`` (Vector):  [Read-Write] 相机位置
- ``camera_rotation`` (Rotator):  [Read-Write] 相机旋转
- ``fov`` (float):  [Read-Write] 相机FOV
- ``pivot`` (Vector):  [Read-Write] 相机旋转轴点

<a id="unreal.CoreCameraData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(camera_location: Vector = [0.000000, 0.000000, 0.000000],
             camera_rotation: Rotator = [0.000000, 0.000000, 0.000000],
             fov: float = 0.000000,
             pivot: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.CoreCameraData.camera_location"></a>

#### camera\_location

```python
@property
def camera_location() -> Vector
```

(Vector):  [Read-Write] 相机位置

<a id="unreal.CoreCameraData.camera_location"></a>

#### camera\_location

```python
@camera_location.setter
def camera_location(value: Vector) -> None
```

<a id="unreal.CoreCameraData.camera_rotation"></a>

#### camera\_rotation

```python
@property
def camera_rotation() -> Rotator
```

(Rotator):  [Read-Write] 相机旋转

<a id="unreal.CoreCameraData.camera_rotation"></a>

#### camera\_rotation

```python
@camera_rotation.setter
def camera_rotation(value: Rotator) -> None
```

<a id="unreal.CoreCameraData.fov"></a>

#### fov

```python
@property
def fov() -> float
```

(float):  [Read-Write] 相机FOV

<a id="unreal.CoreCameraData.fov"></a>

#### fov

```python
@fov.setter
def fov(value: float) -> None
```

<a id="unreal.CoreCameraData.pivot"></a>

#### pivot

```python
@property
def pivot() -> Vector
```

(Vector):  [Read-Write] 相机旋转轴点

<a id="unreal.CoreCameraData.pivot"></a>

#### pivot

```python
@pivot.setter
def pivot(value: Vector) -> None
```

<a id="unreal.TravelAnimationSettings"></a>