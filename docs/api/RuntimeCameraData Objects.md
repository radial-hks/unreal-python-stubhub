## RuntimeCameraData Objects

```python
class RuntimeCameraData(StructBase)
```

运行时相机数据

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``height_to_ground`` (double):  [Read-Write] 相机距离地面的高度
- ``screen_center_ground_location`` (Vector):  [Read-Write] 相机中心在地面位置的坐标
- ``screen_center_location`` (Vector):  [Read-Write] 相机中心在Visibility通道上的世界位置坐标

<a id="unreal.RuntimeCameraData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        height_to_ground: float = 0.000000,
        screen_center_ground_location: Vector = [0.000000, 0.000000, 0.000000],
        screen_center_location: Vector = [0.000000, 0.000000,
                                          0.000000]) -> None
```

<a id="unreal.RuntimeCameraData.height_to_ground"></a>

#### height\_to\_ground

```python
@property
def height_to_ground() -> float
```

(double):  [Read-Write] 相机距离地面的高度

<a id="unreal.RuntimeCameraData.height_to_ground"></a>

#### height\_to\_ground

```python
@height_to_ground.setter
def height_to_ground(value: float) -> None
```

<a id="unreal.RuntimeCameraData.screen_center_ground_location"></a>

#### screen\_center\_ground\_location

```python
@property
def screen_center_ground_location() -> Vector
```

(Vector):  [Read-Write] 相机中心在地面位置的坐标

<a id="unreal.RuntimeCameraData.screen_center_ground_location"></a>

#### screen\_center\_ground\_location

```python
@screen_center_ground_location.setter
def screen_center_ground_location(value: Vector) -> None
```

<a id="unreal.RuntimeCameraData.screen_center_location"></a>

#### screen\_center\_location

```python
@property
def screen_center_location() -> Vector
```

(Vector):  [Read-Write] 相机中心在Visibility通道上的世界位置坐标

<a id="unreal.RuntimeCameraData.screen_center_location"></a>

#### screen\_center\_location

```python
@screen_center_location.setter
def screen_center_location(value: Vector) -> None
```

<a id="unreal.UniqueNetIdWrapper"></a>