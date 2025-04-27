## LidarPointCloudPoint Objects

```python
class LidarPointCloudPoint(StructBase)
```

Lidar Point Cloud Point

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (Color):  [Read-Write]
- ``location`` (Vector3f):  [Read-Write]
- ``normal`` (LidarPointCloudNormal):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.LidarPointCloudPoint.__init__"></a>

#### __init__

```python
def __init__(location: Vector3f = [0.000000, 0.000000, 0.000000],
             color: Color = [0, 0, 0, 0],
             normal: LidarPointCloudNormal = [127, 127, 127],
             visible: bool = False) -> None
```

<a id="unreal.LidarPointCloudPoint.location"></a>

#### location

```python
@property
def location() -> Vector3f
```

(Vector3f):  [Read-Write]

<a id="unreal.LidarPointCloudPoint.location"></a>

#### location

```python
@location.setter
def location(value: Vector3f) -> None
```

<a id="unreal.LidarPointCloudPoint.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.LidarPointCloudPoint.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.LidarPointCloudPoint.normal"></a>

#### normal

```python
@property
def normal() -> LidarPointCloudNormal
```

(LidarPointCloudNormal):  [Read-Write]

<a id="unreal.LidarPointCloudPoint.normal"></a>

#### normal

```python
@normal.setter
def normal(value: LidarPointCloudNormal) -> None
```

<a id="unreal.LidarPointCloudPoint.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LidarPointCloudPoint.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.LidarPointCloudNormal"></a>