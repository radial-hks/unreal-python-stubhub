## LidarPointCloudTraceHit Objects

```python
class LidarPointCloudTraceHit(StructBase)
```

Lidar Point Cloud Trace Hit

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloud.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor`` (LidarPointCloudActor):  [Read-Write]
- ``component`` (LidarPointCloudComponent):  [Read-Write]
- ``points`` (Array[LidarPointCloudPoint]):  [Read-Write]

<a id="unreal.LidarPointCloudTraceHit.__init__"></a>

#### __init__

```python
def __init__(actor: LidarPointCloudActor = None,
             component: LidarPointCloudComponent = None,
             points: Array[LidarPointCloudPoint] = []) -> None
```

<a id="unreal.LidarPointCloudTraceHit.actor"></a>

#### actor

```python
@property
def actor() -> LidarPointCloudActor
```

(LidarPointCloudActor):  [Read-Write]

<a id="unreal.LidarPointCloudTraceHit.actor"></a>

#### actor

```python
@actor.setter
def actor(value: LidarPointCloudActor) -> None
```

<a id="unreal.LidarPointCloudTraceHit.component"></a>

#### component

```python
@property
def component() -> LidarPointCloudComponent
```

(LidarPointCloudComponent):  [Read-Write]

<a id="unreal.LidarPointCloudTraceHit.component"></a>

#### component

```python
@component.setter
def component(value: LidarPointCloudComponent) -> None
```

<a id="unreal.LidarPointCloudTraceHit.points"></a>

#### points

```python
@property
def points() -> Array[LidarPointCloudPoint]
```

(Array[LidarPointCloudPoint]):  [Read-Write]

<a id="unreal.LidarPointCloudTraceHit.points"></a>

#### points

```python
@points.setter
def points(value: Array[LidarPointCloudPoint]) -> None
```

<a id="unreal.LidarPointCloudPoint"></a>