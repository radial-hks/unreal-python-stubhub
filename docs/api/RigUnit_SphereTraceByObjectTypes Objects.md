## RigUnit_SphereTraceByObjectTypes Objects

```python
class RigUnit_SphereTraceByObjectTypes(RigUnit)
```

Sweeps a sphere against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldCollision.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end`` (Vector):  [Read-Write] End of the trace in rig / global space
- ``hit`` (bool):  [Read-Write] Returns true if there was a hit
- ``hit_location`` (Vector):  [Read-Write] Hit location in rig / global Space
- ``hit_normal`` (Vector):  [Read-Write] Hit normal in rig / global Space
- ``object_types`` (Array[ObjectTypeQuery]):  [Read-Write] The types of objects that this trace can hit
- ``radius`` (float):  [Read-Write] Radius of the sphere to use for sweeping / tracing
- ``start`` (Vector):  [Read-Write] Start of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceByObjectTypes.__init__"></a>

#### __init__

```python
def __init__(start: Vector = [0.000000, 0.000000, 0.000000],
             end: Vector = [0.000000, 0.000000, 0.000000],
             object_types: Array[ObjectTypeQuery] = [],
             radius: float = 0.000000,
             hit: bool = False,
             hit_location: Vector = [0.000000, 0.000000, 0.000000],
             hit_normal: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SphereTraceByObjectTypes.start"></a>

#### start

```python
@property
def start() -> Vector
```

(Vector):  [Read-Write] Start of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceByObjectTypes.start"></a>

#### start

```python
@start.setter
def start(value: Vector) -> None
```

<a id="unreal.RigUnit_SphereTraceByObjectTypes.end"></a>

#### end

```python
@property
def end() -> Vector
```

(Vector):  [Read-Write] End of the trace in rig / global space

<a id="unreal.RigUnit_SphereTraceByObjectTypes.end"></a>

#### end

```python
@end.setter
def end(value: Vector) -> None
```

<a id="unreal.RigUnit_SphereTraceByObjectTypes.object_types"></a>

#### object_types

```python
@property
def object_types() -> Array[ObjectTypeQuery]
```

(Array[ObjectTypeQuery]):  [Read-Write] The types of objects that this trace can hit

<a id="unreal.RigUnit_SphereTraceByObjectTypes.object_types"></a>

#### object_types

```python
@object_types.setter
def object_types(value: Array[ObjectTypeQuery]) -> None
```

<a id="unreal.RigUnit_SphereTraceByObjectTypes.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] Radius of the sphere to use for sweeping / tracing

<a id="unreal.RigUnit_SphereTraceByObjectTypes.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.RigUnit_SphereTraceByObjectTypes.hit"></a>

#### hit

```python
@property
def hit() -> bool
```

(bool):  [Read-Only] Returns true if there was a hit

<a id="unreal.RigUnit_SphereTraceByObjectTypes.hit_location"></a>

#### hit_location

```python
@property
def hit_location() -> Vector
```

(Vector):  [Read-Only] Hit location in rig / global Space

<a id="unreal.RigUnit_SphereTraceByObjectTypes.hit_normal"></a>

#### hit_normal

```python
@property
def hit_normal() -> Vector
```

(Vector):  [Read-Only] Hit normal in rig / global Space

<a id="unreal.RigUnit_Control"></a>