## TargetingSelectionTask\_AOE Objects

```python
class TargetingSelectionTask_AOE(TargetingTask)
```

class: UTargetingSelectionTask_AOE Basic AOE based selection task. There are 4 shape types to choose from + a custom option. Box - Defined by a given half extent Cylinder - Defined by the half extent (box) + radius Sphere  - Defined by a given radius Capsule - Defined by the radius + half height SourceComponent - Use a collision component with a specific component tag as the shape

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSelectionTask_AOE.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_channel`` (CollisionChannel):  [Read-Write] The collision channel to use for the overlap check (as long as Collision Profile Name is not set)
- ``collision_object_types`` (Array[ObjectTypeQuery]):  [Read-Write] The collision profile name to use for the overlap check
- ``collision_profile_name`` (CollisionProfileName):  [Read-Write] The collision profile name to use for the overlap check
- ``component_tag`` (Name):  [Read-Write] The component tag to use if a custom component is desired as the overlap shape.
                Use to look up the component on the source actor
- ``default_source_offset`` (Vector):  [Read-Write] The default source location offset used by GetSourceOffset
- ``half_extent`` (Vector):  [Read-Write] The half extent to use for box and cylinder
- ``half_height`` (ScalableFloat):  [Read-Write] The half height to use for capsule overlap checks
- ``ignore_instigator_actor`` (bool):  [Read-Write] Indicates the trace should ignore the source actor
- ``ignore_source_actor`` (bool):  [Read-Write] Indicates the trace should ignore the source actor
- ``radius`` (ScalableFloat):  [Read-Write] The radius to use for sphere and capsule overlaps
- ``shape_type`` (TargetingAOEShape):  [Read-Write] The shape type to use for the AOE
- ``trace_complex`` (bool):  [Read-Write] When enabled, the trace will be performed against complex collision.
- ``use_relative_offset`` (bool):  [Read-Write] Should we offset based on world or relative Source object transform?

<a id="unreal.TargetingSelectionTask_AOE.get_source_rotation"></a>

#### get\_source\_rotation

```python
def get_source_rotation(targeting_handle: TargetingRequestHandle) -> Quat
```

x.get_source_rotation(targeting_handle) -> Quat
Native event to get the source rotation for the AOE

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Quat:

<a id="unreal.TargetingSelectionTask_AOE.get_source_offset"></a>

#### get\_source\_offset

```python
def get_source_offset(targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_source_offset(targeting_handle) -> Vector
Native Event to get a source location offset for the AOE

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_AOE.get_source_location"></a>

#### get\_source\_location

```python
def get_source_location(targeting_handle: TargetingRequestHandle) -> Vector
```

x.get_source_location(targeting_handle) -> Vector
Native Event to get the source location for the AOE

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Vector:

<a id="unreal.TargetingSelectionTask_SourceActor"></a>