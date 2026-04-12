## CesiumSubLevelComponent Objects

```python
class CesiumSubLevelComponent(ActorComponent)
```

A component intended to be attached to a Level Instance Actor that turns that
Level Instance into a Cesium sub-level. Only a single Cesium sub-level can be
active (visible) at any given time.

A globe (like the planet Earth) is an unusual sort of level in Unreal in that
it has truly massive coordinate values and the "up" direction depends on
where exactly on the globe you're located. Many things in the Unreal
ecosystem, such as the gravity system, don't expect this situation and will
have incorrect and surprising behavior when used on a globe.

Cesium sub-levels help to mitigate this. Only one sub-level can be active at
any given time, and when it is, that sub-level's origin becomes the origin of
the Unreal world. Furthermore, at the origin location, Unreal's +X axis
points East, its +Y axis points South, and its +Z axis points Up. Thus,
within a sub-level, gravity works in the normal way that Unreal objects
expect, and coordinate values stay relatively small. This allows you to use
just about any Unreal object within a sub-level without worrying about
surprising behavior.

Globe-aware objects, particularly those with a "Cesium Globe Anchor"
component attached to them, are allowed to exist outside sub-levels and even
move between them. If all your objects are globe aware, there's no need to
use sub-levels at all.

In the Editor, the currently-active sub-level is selected by clicking the
"Eye" icon next to the Level Instance in the Outliner.

At runtime, the currently-active sub-level is selected by the Actor with a
CesiumOriginShiftComponent attached to it. If this Actor is inside a
sub-level's "Load Radius" that sub-level will be activated. If multiple
sub-levels are in range, only the closest one will be activated.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSubLevelComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enabled`` (bool):  [Read-Write] Whether this sub-level is enabled. An enabled sub-level will be
  automatically loaded when the camera moves within its LoadRadius and
  no other levels are closer, and the Georeference will be updated so that
  this level's Longitude, Latitude, and Height become (0, 0, 0) in the Unreal
  World. A sub-level that is not enabled will be ignored by Cesium at
  runtime.
- ``georeference`` (CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the actor's
  coordinate system relates to the coordinate system in this Unreal Engine
  level.

  If this is null, the sub-level will find and use the first Georeference
  Actor in the level, or create one if necessary. To get the active/effective
  Georeference from Blueprints or C++, use ResolvedGeoreference instead.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``load_radius`` (double):  [Read-Write] How close to the sub-level local origin, in meters, the camera needs to be
  to load the level.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``origin_height`` (double):  [Read-Write] The height of the georeference origin for this sub-level in meters above
  the ellipsoid. This height should not be confused with a height above
  Mean Sea Level. When this sub-level is active, the CesiumGeoreference will
  adopt this origin.
- ``origin_latitude`` (double):  [Read-Write] The latitude of the georeference origin for this sub-level in degrees, in
  the range [-90, 90]. When this sub-level is active, the CesiumGeoreference
  will adopt this origin.
- ``origin_longitude`` (double):  [Read-Write] The longitude of the georeference origin for this sub-level in degrees, in
  the range [-180, 180]. When this sub-level is active, the
  CesiumGeoreference will adopt this origin.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``resolved_georeference`` (CesiumGeoreference):  [Read-Only] The resolved georeference used by this sub-level. This is not serialized
  because it may point to a Georeference in the PersistentLevel while this
  Actor is in a sub-level. If the Georeference property is specified,
  however then this property will have the same value.

  This property will be null before ResolveGeoreference is called.

<a id="unreal.CesiumSubLevelComponent.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Whether this sub-level is enabled. An enabled sub-level will be
automatically loaded when the camera moves within its LoadRadius and
no other levels are closer, and the Georeference will be updated so that
this level's Longitude, Latitude, and Height become (0, 0, 0) in the Unreal
World. A sub-level that is not enabled will be ignored by Cesium at
runtime.

<a id="unreal.CesiumSubLevelComponent.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.CesiumSubLevelComponent.origin_latitude"></a>

#### origin\_latitude

```python
@property
def origin_latitude() -> float
```

(double):  [Read-Write] The latitude of the georeference origin for this sub-level in degrees, in
the range [-90, 90]. When this sub-level is active, the CesiumGeoreference
will adopt this origin.

<a id="unreal.CesiumSubLevelComponent.origin_latitude"></a>

#### origin\_latitude

```python
@origin_latitude.setter
def origin_latitude(value: float) -> None
```

<a id="unreal.CesiumSubLevelComponent.origin_longitude"></a>

#### origin\_longitude

```python
@property
def origin_longitude() -> float
```

(double):  [Read-Write] The longitude of the georeference origin for this sub-level in degrees, in
the range [-180, 180]. When this sub-level is active, the
CesiumGeoreference will adopt this origin.

<a id="unreal.CesiumSubLevelComponent.origin_longitude"></a>

#### origin\_longitude

```python
@origin_longitude.setter
def origin_longitude(value: float) -> None
```

<a id="unreal.CesiumSubLevelComponent.origin_height"></a>

#### origin\_height

```python
@property
def origin_height() -> float
```

(double):  [Read-Write] The height of the georeference origin for this sub-level in meters above
the ellipsoid. This height should not be confused with a height above
Mean Sea Level. When this sub-level is active, the CesiumGeoreference will
adopt this origin.

<a id="unreal.CesiumSubLevelComponent.origin_height"></a>

#### origin\_height

```python
@origin_height.setter
def origin_height(value: float) -> None
```

<a id="unreal.CesiumSubLevelComponent.load_radius"></a>

#### load\_radius

```python
@property
def load_radius() -> float
```

(double):  [Read-Write] How close to the sub-level local origin, in meters, the camera needs to be
to load the level.

<a id="unreal.CesiumSubLevelComponent.load_radius"></a>

#### load\_radius

```python
@load_radius.setter
def load_radius(value: float) -> None
```

<a id="unreal.CesiumSubLevelComponent.georeference"></a>

#### georeference

```python
@property
def georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Write] The designated georeference actor controlling how the actor's
coordinate system relates to the coordinate system in this Unreal Engine
level.

If this is null, the sub-level will find and use the first Georeference
Actor in the level, or create one if necessary. To get the active/effective
Georeference from Blueprints or C++, use ResolvedGeoreference instead.

<a id="unreal.CesiumSubLevelComponent.georeference"></a>

#### georeference

```python
@georeference.setter
def georeference(value: CesiumGeoreference) -> None
```

<a id="unreal.CesiumSubLevelComponent.resolved_georeference"></a>

#### resolved\_georeference

```python
@property
def resolved_georeference() -> CesiumGeoreference
```

(CesiumGeoreference):  [Read-Only] The resolved georeference used by this sub-level. This is not serialized
because it may point to a Georeference in the PersistentLevel while this
Actor is in a sub-level. If the Georeference property is specified,
however then this property will have the same value.

This property will be null before ResolveGeoreference is called.

<a id="unreal.CesiumSubLevelComponent.set_origin_longitude_latitude_height"></a>

#### set\_origin\_longitude\_latitude\_height

```python
def set_origin_longitude_latitude_height(
        longitude_latitude_height: Vector) -> None
```

x.set_origin_longitude_latitude_height(longitude_latitude_height) -> None
Sets the longitude (X), latitude (Y), and height (Z) of this sub-level's
georeference origin. When this sub-level is active, the CesiumGeoreference
will adopt this origin. Longitude and latitude are in degrees. Height is in
meters above the ellipsoid, which should not be confused with meters
above Mean Sea Level.

Args:
    longitude_latitude_height (Vector):

<a id="unreal.CesiumSubLevelComponent.resolve_georeference"></a>

#### resolve\_georeference

```python
def resolve_georeference(force_reresolve: bool = False) -> CesiumGeoreference
```

x.resolve_georeference(force_reresolve=False) -> CesiumGeoreference
Resolves the Cesium Georeference to use with this components. Returns
the value of the Georeference property if it is set. Otherwise, finds a
Georeference in the World and returns it, creating it if necessary. The
resolved Georeference is cached so subsequent calls to this function will
return the same instance, unless ForceReresolve is true.

Args:
    force_reresolve (bool): 

Returns:
    CesiumGeoreference:

<a id="unreal.CesiumSubLevelSwitcherComponent"></a>