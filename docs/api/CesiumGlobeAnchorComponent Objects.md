## CesiumGlobeAnchorComponent Objects

```python
class CesiumGlobeAnchorComponent(ActorComponent)
```

This component can be added to a movable actor to anchor it to the globe
and maintain precise placement. When the owning actor is transformed through
normal Unreal Engine mechanisms, the internal geospatial coordinates will be
automatically updated. The actor position can also be set in terms of
Earth-Centered, Earth-Fixed coordinates (ECEF) or Longitude, Latitude, and
Height relative to the ellipsoid.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumGlobeAnchorComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_to_earth_centered_earth_fixed_matrix`` (Matrix):  [Read-Write] The 4x4 transformation matrix from the Actors's local coordinate system to
  the Earth-Centered, Earth-Fixed (ECEF) coordinate system.

  The ECEF coordinate system is a right-handed system located at the center
  of the Earth. The +X axis points to the intersection of the Equator and
  Prime Meridian (zero degrees longitude). The +Y axis points to the
  intersection of the Equator and +90 degrees longitude. The +Z axis points
  up through the North Pole.

  If `AdjustOrientationForGlobeWhenMoving` is enabled and this property is
  set, the Actor's orientation will also be adjusted to account for globe
  curvature.
- ``actor_to_ecef_array`` (double):  [Read-Write] This is used only to preserve the transformation saved by old versions of
  Cesium for Unreal. See the Serialize method.
  deprecated: Property '_actorToECEF_Array' is deprecated.
- ``adjust_orientation_for_globe_when_moving`` (bool):  [Read-Write] Whether to adjust the Actor's orientation based on globe curvature as the
  Actor moves.

  The Earth is not flat, so as we move across its surface, the direction of
  "up" changes. If we ignore this fact and leave an object's orientation
  unchanged as it moves over the globe surface, the object will become
  increasingly tilted and eventually be completely upside-down when we arrive
  at the opposite side of the globe.

  When this setting is enabled, this Component will automatically apply a
  rotation to the Actor to account for globe curvature any time the Actor's
  position on the globe changes.

  This property should usually be enabled, but it may be useful to disable it
  when your application already accounts for globe curvature itself when it
  updates an Actor's position and orientation, because in that case the Actor
  would be over-rotated.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``georeference`` (CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the owning actor's
  coordinate system relates to the coordinate system in this Unreal Engine
  level.

  If this is null, the Component will find and use the first Georeference
  Actor in the level, or create one if necessary. To get the active/effective
  Georeference from Blueprints or C++, use ResolvedGeoreference instead.

  If setting this property changes the CesiumGeoreference, the globe position
  will be maintained and the Actor's transform will be updated according to
  the new CesiumGeoreference.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``resolved_georeference`` (CesiumGeoreference):  [Read-Only] The resolved georeference used by this component. This is not serialized
  because it may point to a Georeference in the PersistentLevel while this
  component is in a sub-level. If the Georeference property is specified,
  however then this property will have the same value.

  This property will be null before ResolveGeoreference is called, which
  happens automatically when the component is registered.
- ``teleport_when_updating_transform`` (bool):  [Read-Write] Using the teleport flag will move objects to the updated transform
  immediately and without affecting their velocity. This is useful when
  working with physics actors that maintain an internal velocity which we do
  not want to change when updating location.

<a id="unreal.CesiumGlobeAnchorComponent.georeference"></a>

#### georeference

```python
@property
def georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the owning actor's
coordinate system relates to the coordinate system in this Unreal Engine
level.

If this is null, the Component will find and use the first Georeference
Actor in the level, or create one if necessary. To get the active/effective
Georeference from Blueprints or C++, use ResolvedGeoreference instead.

If setting this property changes the CesiumGeoreference, the globe position
will be maintained and the Actor's transform will be updated according to
the new CesiumGeoreference.

<a id="unreal.CesiumGlobeAnchorComponent.georeference"></a>

#### georeference

```python
@georeference.setter
def georeference(value: CesiumGeoreference) -> None
```

<a id="unreal.CesiumGlobeAnchorComponent.resolved_georeference"></a>

#### resolved\_georeference

```python
@property
def resolved_georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Only] The resolved georeference used by this component. This is not serialized
because it may point to a Georeference in the PersistentLevel while this
component is in a sub-level. If the Georeference property is specified,
however then this property will have the same value.

This property will be null before ResolveGeoreference is called, which
happens automatically when the component is registered.

<a id="unreal.CesiumGlobeAnchorComponent.adjust_orientation_for_globe_when_moving"></a>

#### adjust\_orientation\_for\_globe\_when\_moving

```python
@property
def adjust_orientation_for_globe_when_moving() -> bool
```

(bool):  [Read-Write] Whether to adjust the Actor's orientation based on globe curvature as the
Actor moves.

The Earth is not flat, so as we move across its surface, the direction of
"up" changes. If we ignore this fact and leave an object's orientation
unchanged as it moves over the globe surface, the object will become
increasingly tilted and eventually be completely upside-down when we arrive
at the opposite side of the globe.

When this setting is enabled, this Component will automatically apply a
rotation to the Actor to account for globe curvature any time the Actor's
position on the globe changes.

This property should usually be enabled, but it may be useful to disable it
when your application already accounts for globe curvature itself when it
updates an Actor's position and orientation, because in that case the Actor
would be over-rotated.

<a id="unreal.CesiumGlobeAnchorComponent.adjust_orientation_for_globe_when_moving"></a>

#### adjust\_orientation\_for\_globe\_when\_moving

```python
@adjust_orientation_for_globe_when_moving.setter
def adjust_orientation_for_globe_when_moving(value: bool) -> None
```

<a id="unreal.CesiumGlobeAnchorComponent.teleport_when_updating_transform"></a>

#### teleport\_when\_updating\_transform

```python
@property
def teleport_when_updating_transform() -> bool
```

(bool):  [Read-Write] Using the teleport flag will move objects to the updated transform
immediately and without affecting their velocity. This is useful when
working with physics actors that maintain an internal velocity which we do
not want to change when updating location.

<a id="unreal.CesiumGlobeAnchorComponent.teleport_when_updating_transform"></a>

#### teleport\_when\_updating\_transform

```python
@teleport_when_updating_transform.setter
def teleport_when_updating_transform(value: bool) -> None
```

<a id="unreal.CesiumGlobeAnchorComponent.actor_to_earth_centered_earth_fixed_matrix"></a>

#### actor\_to\_earth\_centered\_earth\_fixed\_matrix

```python
@property
def actor_to_earth_centered_earth_fixed_matrix() -> Matrix
```

(Matrix):  [Read-Write] The 4x4 transformation matrix from the Actors's local coordinate system to
the Earth-Centered, Earth-Fixed (ECEF) coordinate system.

The ECEF coordinate system is a right-handed system located at the center
of the Earth. The +X axis points to the intersection of the Equator and
Prime Meridian (zero degrees longitude). The +Y axis points to the
intersection of the Equator and +90 degrees longitude. The +Z axis points
up through the North Pole.

If `AdjustOrientationForGlobeWhenMoving` is enabled and this property is
set, the Actor's orientation will also be adjusted to account for globe
curvature.

<a id="unreal.CesiumGlobeAnchorComponent.actor_to_earth_centered_earth_fixed_matrix"></a>

#### actor\_to\_earth\_centered\_earth\_fixed\_matrix

```python
@actor_to_earth_centered_earth_fixed_matrix.setter
def actor_to_earth_centered_earth_fixed_matrix(value: Matrix) -> None
```

<a id="unreal.CesiumGlobeAnchorComponent.actor_to_ecef_array"></a>

#### actor\_to\_ecef\_array

```python
@property
def actor_to_ecef_array() -> float
```

(double):  [Read-Write] This is used only to preserve the transformation saved by old versions of
Cesium for Unreal. See the Serialize method.
deprecated: Property '_actorToECEF_Array' is deprecated.

<a id="unreal.CesiumGlobeAnchorComponent.actor_to_ecef_array"></a>

#### actor\_to\_ecef\_array

```python
@actor_to_ecef_array.setter
def actor_to_ecef_array(value: float) -> None
```

<a id="unreal.CesiumGlobeAnchorComponent.sync"></a>

#### sync

```python
def sync() -> None
```

x.sync() -> None
Synchronizes the properties of this globe anchor.

It is usually not necessary to call this method because it is called
automatically when needed.

This method performs the following actions:

  - If the ActorToEarthCenteredEarthFixedMatrix has not yet been
determined, it is computed from the Actor's current root transform.
  - If the Actor's root transform has changed since the last time this
component was registered, this method updates the
ActorToEarthCenteredEarthFixedMatrix from the current transform.
  - If the origin of the CesiumGeoreference has changed, the Actor's root
transform is updated based on the ActorToEarthCenteredEarthFixedMatrix and
the new georeference origin.

<a id="unreal.CesiumGlobeAnchorComponent.snap_to_east_south_up"></a>

#### snap\_to\_east\_south\_up

```python
def snap_to_east_south_up() -> None
```

x.snap_to_east_south_up() -> None
Rotates the Actor so that its +X axis points in the local East direction,
its +Y axis points in the local South direction, and its +Z axis points in
the local Up direction.

<a id="unreal.CesiumGlobeAnchorComponent.snap_local_up_to_ellipsoid_normal"></a>

#### snap\_local\_up\_to\_ellipsoid\_normal

```python
def snap_local_up_to_ellipsoid_normal() -> None
```

x.snap_local_up_to_ellipsoid_normal() -> None
Rotates the Actor so that its local +Z axis is aligned with the ellipsoid
surface normal at its current location.

<a id="unreal.CesiumGlobeAnchorComponent.set_east_south_up_rotation"></a>

#### set\_east\_south\_up\_rotation

```python
def set_east_south_up_rotation(east_south_up_rotation: Quat) -> None
```

x.set_east_south_up_rotation(east_south_up_rotation) -> None
Sets the rotation of the Actor relative to a local coordinate system
centered on this object where the +X points in the local East direction,
the +Y axis points in the local South direction, and the +Z axis points in
the local Up direction.

When the rotation is set via this method, it is internally converted to
and stored in the ActorToEarthCenteredEarthFixedMatrix property. As a
result, getting this property will not necessarily return the exact value
that was set.

Args:
    east_south_up_rotation (Quat):

<a id="unreal.CesiumGlobeAnchorComponent.set_earth_centered_earth_fixed_rotation"></a>

#### set\_earth\_centered\_earth\_fixed\_rotation

```python
def set_earth_centered_earth_fixed_rotation(
        earth_centered_earth_fixed_rotation: Quat) -> None
```

x.set_earth_centered_earth_fixed_rotation(earth_centered_earth_fixed_rotation) -> None
Sets the rotation of the Actor relative to the Earth-Centered, Earth-Fixed
(ECEF) coordinate system.

The ECEF coordinate system is a right-handed system located at the center
of the Earth. The +X axis points from there to the intersection of the
Equator and Prime Meridian (zero degrees longitude). The +Y axis points to
the intersection of the Equator and +90 degrees longitude. The +Z axis
points up through the North Pole.

Args:
    earth_centered_earth_fixed_rotation (Quat):

<a id="unreal.CesiumGlobeAnchorComponent.resolve_georeference"></a>

#### resolve\_georeference

```python
def resolve_georeference(force_reresolve: bool = False) -> CesiumGeoreference
```

x.resolve_georeference(force_reresolve=False) -> CesiumGeoreference
Resolves the Cesium Georeference to use with this Component. Returns
the value of the Georeference property if it is set. Otherwise, finds a
Georeference in the World and returns it, creating it if necessary. The
resolved Georeference is cached so subsequent calls to this function will
return the same instance, unless ForceReresolve is true.

Args:
    force_reresolve (bool): 

Returns:
    CesiumGeoreference:

<a id="unreal.CesiumGlobeAnchorComponent.move_to_longitude_latitude_height"></a>

#### move\_to\_longitude\_latitude\_height

```python
def move_to_longitude_latitude_height(
        longitude_latitude_height: Vector) -> None
```

x.move_to_longitude_latitude_height(longitude_latitude_height) -> None
Moves the Actor to which this component is attached to a given longitude in
degrees (X), latitude in degrees (Y), and height in meters (Z).

The Height (Z) is measured in meters above the ellipsoid. Do not
confused an ellipsoidal height with a geoid height or height above mean sea
level, which can be tens of meters higher or lower depending on where in
the world the object is located.

If `AdjustOrientationForGlobeWhenMoving` is enabled, the Actor's
orientation will also be adjusted to account for globe curvature.

Args:
    longitude_latitude_height (Vector):

<a id="unreal.CesiumGlobeAnchorComponent.inaccurate_move_to_longitude_latitude_height"></a>

#### inaccurate\_move\_to\_longitude\_latitude\_height

```python
def inaccurate_move_to_longitude_latitude_height(
        longitude_latitude_height: Vector) -> None
```

deprecated: 'inaccurate_move_to_longitude_latitude_height' was renamed to 'move_to_longitude_latitude_height'.

<a id="unreal.CesiumGlobeAnchorComponent.move_to_earth_centered_earth_fixed_position"></a>

#### move\_to\_earth\_centered\_earth\_fixed\_position

```python
def move_to_earth_centered_earth_fixed_position(
        earth_centered_earth_fixed_position: Vector) -> None
```

x.move_to_earth_centered_earth_fixed_position(earth_centered_earth_fixed_position) -> None
Moves the Actor to which this component is attached to a given globe
position in Earth-Centered, Earth-Fixed coordinates in meters.

If AdjustOrientationForGlobeWhenMoving is enabled, this method will
also update the orientation based on the globe curvature.

Args:
    earth_centered_earth_fixed_position (Vector):

<a id="unreal.CesiumGlobeAnchorComponent.inaccurate_move_to_ecef"></a>

#### inaccurate\_move\_to\_ecef

```python
def inaccurate_move_to_ecef(
        earth_centered_earth_fixed_position: Vector) -> None
```

deprecated: 'inaccurate_move_to_ecef' was renamed to 'move_to_earth_centered_earth_fixed_position'.

<a id="unreal.CesiumGlobeAnchorComponent.move_to_ecef"></a>

#### move\_to\_ecef

```python
def move_to_ecef(earth_centered_earth_fixed_position: Vector) -> None
```

deprecated: 'move_to_ecef' was renamed to 'move_to_earth_centered_earth_fixed_position'.

<a id="unreal.CesiumGlobeAnchorComponent.invalidate_resolved_georeference"></a>

#### invalidate\_resolved\_georeference

```python
def invalidate_resolved_georeference() -> None
```

x.invalidate_resolved_georeference() -> None
Invalidate Resolved Georeference
deprecated: The resolved georeference can no longer be explicitly invalidated. To change the georeference, call SetGeoreference or ReregisterComponent.

<a id="unreal.CesiumGlobeAnchorComponent.get_longitude_latitude_height"></a>

#### get\_longitude\_latitude\_height

```python
def get_longitude_latitude_height() -> Vector
```

x.get_longitude_latitude_height() -> Vector
Gets the longitude in degrees (X), latitude in degrees (Y),
and height in meters above the ellipsoid (Z) of the actor.

Do not confuse the ellipsoid height with a geoid height or height above
mean sea level, which can be tens of meters higher or lower depending on
where in the world the object is located.

Returns:
    Vector:

<a id="unreal.CesiumGlobeAnchorComponent.inaccurate_get_longitude_latitude_height"></a>

#### inaccurate\_get\_longitude\_latitude\_height

```python
def inaccurate_get_longitude_latitude_height() -> Vector
```

deprecated: 'inaccurate_get_longitude_latitude_height' was renamed to 'get_longitude_latitude_height'.

<a id="unreal.CesiumGlobeAnchorComponent.get_longitude"></a>

#### get\_longitude

```python
def get_longitude() -> float
```

x.get_longitude() -> double
Gets the longitude in degrees.

Returns:
    double:

<a id="unreal.CesiumGlobeAnchorComponent.get_latitude"></a>

#### get\_latitude

```python
def get_latitude() -> float
```

x.get_latitude() -> double
Gets the latitude in degrees.

Returns:
    double:

<a id="unreal.CesiumGlobeAnchorComponent.get_height"></a>

#### get\_height

```python
def get_height() -> float
```

x.get_height() -> double
Gets the height in meters above the ellipsoid.

Do not confuse the ellipsoid height with a geoid height or height above
mean sea level, which can be tens of meters higher or lower depending on
where in the world the object is located.

Returns:
    double:

<a id="unreal.CesiumGlobeAnchorComponent.get_east_south_up_rotation"></a>

#### get\_east\_south\_up\_rotation

```python
def get_east_south_up_rotation() -> Quat
```

x.get_east_south_up_rotation() -> Quat
Gets the rotation of the Actor relative to a local coordinate system
centered on this object where the +X points in the local East direction,
the +Y axis points in the local South direction, and the +Z axis points in
the local Up direction.

Returns:
    Quat:

<a id="unreal.CesiumGlobeAnchorComponent.get_earth_centered_earth_fixed_rotation"></a>

#### get\_earth\_centered\_earth\_fixed\_rotation

```python
def get_earth_centered_earth_fixed_rotation() -> Quat
```

x.get_earth_centered_earth_fixed_rotation() -> Quat
Gets the rotation of the Actor relative to the Earth-Centered, Earth-Fixed
(ECEF) coordinate system.

The ECEF coordinate system is a right-handed system located at the center
of the Earth. The +X axis points from there to the intersection of the
Equator and Prime Meridian (zero degrees longitude). The +Y axis points to
the intersection of the Equator and +90 degrees longitude. The +Z axis
points up through the North Pole.

Returns:
    Quat:

<a id="unreal.CesiumGlobeAnchorComponent.get_earth_centered_earth_fixed_position"></a>

#### get\_earth\_centered\_earth\_fixed\_position

```python
def get_earth_centered_earth_fixed_position() -> Vector
```

x.get_earth_centered_earth_fixed_position() -> Vector
Gets the Earth-Centered, Earth-Fixed (ECEF) coordinates of the Actor in
meters.

Returns:
    Vector:

<a id="unreal.CesiumGlobeAnchorComponent.inaccurate_get_ecef"></a>

#### inaccurate\_get\_ecef

```python
def inaccurate_get_ecef() -> Vector
```

deprecated: 'inaccurate_get_ecef' was renamed to 'get_earth_centered_earth_fixed_position'.

<a id="unreal.CesiumGlobeAnchorComponent.get_ecef"></a>

#### get\_ecef

```python
def get_ecef() -> Vector
```

deprecated: 'get_ecef' was renamed to 'get_earth_centered_earth_fixed_position'.

<a id="unreal.CesiumGeoreferenceComponent"></a>