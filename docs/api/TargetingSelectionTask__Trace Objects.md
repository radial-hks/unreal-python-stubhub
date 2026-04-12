## TargetingSelectionTask\_Trace Objects

```python
class TargetingSelectionTask_Trace(TargetingTask)
```

class: UTargetingSelectionTask_Trace Selection task that can perform a synchronous or asynchronous trace (line/sweep) to find all targets up to the first blocking hit (or its end point).

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSelectionTask_Trace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_profile_name`` (CollisionProfileName):  [Read-Write] The collision profile name to use instead of trace channel (does not work for async traces)
- ``complex_trace`` (bool):  [Read-Write] Indicates the trace should perform a complex trace
- ``default_source_offset`` (Vector):  [Read-Write] The default source location offset used by GetSourceOffset
- ``default_swept_trace_box_half_extent_x`` (ScalableFloat):  [Read-Write] The default swept extents used by GetSweptTraceExtents when the trace type is set to Box
- ``default_swept_trace_box_half_extent_y`` (ScalableFloat):  [Read-Write] The default swept extents used by GetSweptTraceBoxHalfExtents when the trace type is set to Box
- ``default_swept_trace_box_half_extent_z`` (ScalableFloat):  [Read-Write] The default swept extents used by GetSweptTraceBoxHalfExtents when the trace type is set to Box
- ``default_swept_trace_capsule_half_height`` (ScalableFloat):  [Read-Write] The default swept trace radius used by GetSweptTraceRadius when the trace type is set to Capsule
- ``default_swept_trace_radius`` (ScalableFloat):  [Read-Write] The default swept trace radius used by GetSweptTraceRadius when the trace type is set to Sphere or Capsule
- ``default_swept_trace_rotation`` (Rotator):  [Read-Write] The default swept rotation (relative to the trace direction) used by GetSweptTraceRotation when the trace type is set to Capsule or Box
- ``default_trace_length`` (ScalableFloat):  [Read-Write] The default trace length to use if GetTraceLength is not overridden by a child
- ``explicit_trace_direction`` (Vector):  [Read-Write] An explicit trace direction to use (default uses pawn control rotation or actor forward vector in GetTraceDirection)
- ``ignore_instigator_actor`` (bool):  [Read-Write] Indicates the trace should ignore the source actor
- ``ignore_source_actor`` (bool):  [Read-Write] Indicates the trace should ignore the source actor
- ``multi_trace`` (bool):  [Read-Write] Indicates whether the trace should be a multi trace or a single trace
- ``trace_channel`` (TraceTypeQuery):  [Read-Write] The trace channel to use
- ``trace_type`` (TargetingTraceType):  [Read-Write] The trace type (i.e. shape) to use

<a id="unreal.TargetingSelectionTask_Trace.get_trace_length"></a>

#### get\_trace\_length

```python
def get_trace_length(targeting_handle: TargetingRequestHandle) -> float
```

x.get_trace_length(targeting_handle) -> float
Native Event to get the length for the Trace

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    float:

<a id="unreal.TargetingSelectionTask_Trace.get_trace_direction"></a>

#### get\_trace\_direction

```python
def get_trace_direction(targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_trace_direction(targeting_handle) -> Vector
Native Event to get the direction for the Trace

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_Trace.get_swept_trace_rotation"></a>

#### get\_swept\_trace\_rotation

```python
def get_swept_trace_rotation(
        targeting_handle: TargetingRequestHandle) -> Rotator
```

x.get_swept_trace_rotation(targeting_handle) -> Rotator
Native Event to get the swept trace rotation relative to trace direction
      (only called if TraceType = ETargetingTraceType::Capsule or TraceType = ETargetingTraceType::Box)

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Rotator:

<a id="unreal.TargetingSelectionTask_Trace.get_swept_trace_radius"></a>

#### get\_swept\_trace\_radius

```python
def get_swept_trace_radius(targeting_handle: TargetingRequestHandle) -> float
```

x.get_swept_trace_radius(targeting_handle) -> float
Native Event to get the swept trace radius (only called if TraceType = ETargetingTraceType::Sphere or TraceType = ETargetingTraceType::Capsule)

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    float:

<a id="unreal.TargetingSelectionTask_Trace.get_swept_trace_capsule_half_height"></a>

#### get\_swept\_trace\_capsule\_half\_height

```python
def get_swept_trace_capsule_half_height(
        targeting_handle: TargetingRequestHandle) -> float
```

x.get_swept_trace_capsule_half_height(targeting_handle) -> float
Native Event to get the swept trace capsule's half height (only called if  TraceType = ETargetingTraceType::Capsule)

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    float:

<a id="unreal.TargetingSelectionTask_Trace.get_swept_trace_box_half_extents"></a>

#### get\_swept\_trace\_box\_half\_extents

```python
def get_swept_trace_box_half_extents(
        targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_swept_trace_box_half_extents(targeting_handle) -> Vector
Native Event to get the swept box trace half extents (only called if TraceType = ETargetingTraceType::Box)

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_Trace.get_source_offset"></a>

#### get\_source\_offset

```python
def get_source_offset(targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_source_offset(targeting_handle) -> Vector
Native Event to get a source location offset for the Trace

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_Trace.get_source_location"></a>

#### get\_source\_location

```python
def get_source_location(targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_source_location(targeting_handle) -> Vector
Native Event to get the source location for the Trace

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_Trace.get_additional_actors_to_ignore"></a>

#### get\_additional\_actors\_to\_ignore

```python
def get_additional_actors_to_ignore(
        targeting_handle: TargetingRequestHandle) -> Array[Actor]
```

x.get_additional_actors_to_ignore(targeting_handle) -> Array[Actor]
Native Event to get additional actors the Trace should ignore

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Array[Actor]: 

    out_additional_actors_to_ignore (Array[Actor]):

<a id="unreal.TargetingSubsystem"></a>