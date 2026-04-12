## CesiumOriginShiftComponent Objects

```python
class CesiumOriginShiftComponent(CesiumGlobeAnchoredActorComponent)
```

Automatically shifts the origin of the Unreal world coordinate system as the
object to which this component is attached moves. This improves rendering
precision by keeping coordinate values small, and can also help world
building by keeping the globe's local up direction aligned with the +Z axis.

This component is typically attached to a camera or Pawn. By default, it only
shifts the origin when entering a new sub-level (a Level Instance Actor with
a CesiumSubLevelComponent attached to it). By changing the Mode and Distance
properties, it can also shift the origin continually when in between
sub-levels (or when not using sub-levels at all).

It is essential to add a CesiumGlobeAnchorComponent to all other non-globe
aware objects in the level; otherwise, they will appear to move when the
origin is shifted. It is not necessary to anchor objects that are in
sub-levels, because the origin remains constant for the entire time that a
sub-level is active.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumOriginShiftComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``distance`` (double):  [Read-Write] The maximum distance between the origin of the Unreal coordinate system and
  the Actor to which this component is attached. When this distance is
  exceeded, the origin is shifted to bring it close to the Actor. This
  property is ignored if the Mode property is set to "Disabled" or "Switch
  Sub Levels Only".

  When the value of this property is 0.0, the origin is shifted continuously.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``globe_anchor`` (CesiumGlobeAnchorComponent):  [Read-Write] The globe anchor attached to the same Actor as this component. Don't
  save/load or copy this. It is set in BeginPlay and OnRegister.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mode`` (CesiumOriginShiftMode):  [Read-Write] Indicates how to shift the origin as the Actor to which this component is
  attached moves.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.CesiumOriginShiftComponent.mode"></a>

#### mode

```python
@property
def mode() -> CesiumOriginShiftMode
```

(CesiumOriginShiftMode):  [Read-Write] Indicates how to shift the origin as the Actor to which this component is
attached moves.

<a id="unreal.CesiumOriginShiftComponent.mode"></a>

#### mode

```python
@mode.setter
def mode(value: CesiumOriginShiftMode) -> None
```

<a id="unreal.CesiumOriginShiftComponent.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(double):  [Read-Write] The maximum distance between the origin of the Unreal coordinate system and
the Actor to which this component is attached. When this distance is
exceeded, the origin is shifted to bring it close to the Actor. This
property is ignored if the Mode property is set to "Disabled" or "Switch
Sub Levels Only".

When the value of this property is 0.0, the origin is shifted continuously.

<a id="unreal.CesiumOriginShiftComponent.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.CesiumPolygonRasterOverlay"></a>