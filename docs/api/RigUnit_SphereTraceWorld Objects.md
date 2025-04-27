## RigUnit_SphereTraceWorld Objects

```python
class RigUnit_SphereTraceWorld(RigUnit)
```

Sweeps a sphere against the world and return the first blocking hit using a specific channel

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldCollision.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (CollisionChannel):  [Read-Write] The 'channel' that this trace is in, used to determine which components to hit
- ``end`` (Vector):  [Read-Write] End of the trace in rig / global space
- ``hit`` (bool):  [Read-Write] Returns true if there was a hit
- ``hit_location`` (Vector):  [Read-Write] Hit location in rig / global Space
- ``hit_normal`` (Vector):  [Read-Write] Hit normal in rig / global Space
- ``radius`` (float):  [Read-Write] Radius of the sphere to use for sweeping / tracing
- ``start`` (Vector):  [Read-Write] Start of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceWorld.__init__"></a>

#### __init__

```python
def __init__(start: Vector = [0.000000, 0.000000, 0.000000],
             end: Vector = [0.000000, 0.000000, 0.000000],
             channel: CollisionChannel = CollisionChannel.ECC_WORLD_STATIC,
             radius: float = 0.000000,
             hit: bool = False,
             hit_location: Vector = [0.000000, 0.000000, 0.000000],
             hit_normal: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SphereTraceWorld.start"></a>

#### start

```python
@property
def start() -> Vector
```

(Vector):  [Read-Write] Start of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceWorld.start"></a>

#### start

```python
@start.setter
def start(value: Vector) -> None
```

<a id="unreal.RigUnit_SphereTraceWorld.end"></a>

#### end

```python
@property
def end() -> Vector
```

(Vector):  [Read-Write] End of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceWorld.end"></a>

#### end

```python
@end.setter
def end(value: Vector) -> None
```

<a id="unreal.RigUnit_SphereTraceWorld.channel"></a>

#### channel

```python
@property
def channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] The 'channel' that this trace is in, used to determine which components to hit

<a id="unreal.RigUnit_SphereTraceWorld.channel"></a>

#### channel

```python
@channel.setter
def channel(value: CollisionChannel) -> None
```

<a id="unreal.RigUnit_SphereTraceWorld.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Radius of the sphere to use for sweeping / tracing

<a id="unreal.RigUnit_SphereTraceWorld.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RigUnit_SphereTraceWorld.hit"></a>

#### hit

```python
@property
def hit() -> bool
```

(bool):  [Read-Only] Returns true if there was a hit

<a id="unreal.RigUnit_SphereTraceWorld.hit_location"></a>

#### hit_location

```python
@property
def hit_location() -> Vector
```

(Vector):  [Read-Only] Hit location in rig / global Space

<a id="unreal.RigUnit_SphereTraceWorld.hit_normal"></a>

#### hit_normal

```python
@property
def hit_normal() -> Vector
```

(Vector):  [Read-Only] Hit normal in rig / global Space

<a id="unreal.RigUnit_SphereTraceByTraceChannel"></a>