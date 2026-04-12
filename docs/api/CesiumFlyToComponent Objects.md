## CesiumFlyToComponent Objects

```python
class CesiumFlyToComponent(CesiumGlobeAnchoredActorComponent)
```

Smoothly animates the Actor to which it is attached on a flight to a new
location on the globe.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFlyToComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``duration`` (float):  [Read-Write] The length in seconds that the flight should last.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``globe_anchor`` (CesiumGlobeAnchorComponent):  [Read-Write] The globe anchor attached to the same Actor as this component. Don't
  save/load or copy this. It is set in BeginPlay and OnRegister.
- ``height_percentage_curve`` (CurveFloat):  [Read-Write] A curve that controls what percentage of the maximum height the Actor
  should take at a given time on the flight. This curve must be kept in the 0
  to 1 range on both axes. The MaximumHeightByDistanceCurve controls the
  actual maximum height that is achieved during the flight.

  If this curve is not specified, the height will be a smooth interpolation
  between the height at the original location and the height at the
  destination location, and the MaximumHeightByDistanceCurve will be ignored.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``maximum_height_by_distance_curve`` (CurveFloat):  [Read-Write] A curve that controls the maximum height that will be achieved during the
  flight as a function of the straight-line distance of the flight, in
  meters. If the start and end point are on opposite sides of the globe, the
  straight-line distance goes through the Earth even though the flight itself
  will not.

  If HeightPercentageCurve is not specified, this property is ignored.
  If HeightPercentageCurve is specified, but this property is not, then the
  maximum height is 30,000 meters regardless of distance.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_flight_complete`` (CesiumFlightCompleted):  [Read-Write] A delegate that will be called when the Actor finishes flying.
- ``on_flight_interrupted`` (CesiumFlightInterrupted):  [Read-Write] A delegate that will be called when the Actor's flight is interrupted.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``progress_curve`` (CurveFloat):  [Read-Write] A curve that is used to determine the flight progress percentage for all
  the other curves. The input is the fraction (0.0 to 1.0) of the total time
  that has passed so far, and the output is the fraction of the total curve
  that should be traversed at this time. This curve allows the Actor to
  accelerate and deaccelerate as desired throughout the flight.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``rotation_to_use`` (CesiumFlyToRotation):  [Read-Write] Indicates which rotation to use during flights.

<a id="unreal.CesiumFlyToComponent.progress_curve"></a>

#### progress\_curve

```python
@property
def progress_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] A curve that is used to determine the flight progress percentage for all
the other curves. The input is the fraction (0.0 to 1.0) of the total time
that has passed so far, and the output is the fraction of the total curve
that should be traversed at this time. This curve allows the Actor to
accelerate and deaccelerate as desired throughout the flight.

<a id="unreal.CesiumFlyToComponent.progress_curve"></a>

#### progress\_curve

```python
@progress_curve.setter
def progress_curve(value: CurveFloat) -> None
```

<a id="unreal.CesiumFlyToComponent.height_percentage_curve"></a>

#### height\_percentage\_curve

```python
@property
def height_percentage_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] A curve that controls what percentage of the maximum height the Actor
should take at a given time on the flight. This curve must be kept in the 0
to 1 range on both axes. The MaximumHeightByDistanceCurve controls the
actual maximum height that is achieved during the flight.

If this curve is not specified, the height will be a smooth interpolation
between the height at the original location and the height at the
destination location, and the MaximumHeightByDistanceCurve will be ignored.

<a id="unreal.CesiumFlyToComponent.height_percentage_curve"></a>

#### height\_percentage\_curve

```python
@height_percentage_curve.setter
def height_percentage_curve(value: CurveFloat) -> None
```

<a id="unreal.CesiumFlyToComponent.maximum_height_by_distance_curve"></a>

#### maximum\_height\_by\_distance\_curve

```python
@property
def maximum_height_by_distance_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] A curve that controls the maximum height that will be achieved during the
flight as a function of the straight-line distance of the flight, in
meters. If the start and end point are on opposite sides of the globe, the
straight-line distance goes through the Earth even though the flight itself
will not.

If HeightPercentageCurve is not specified, this property is ignored.
If HeightPercentageCurve is specified, but this property is not, then the
maximum height is 30,000 meters regardless of distance.

<a id="unreal.CesiumFlyToComponent.maximum_height_by_distance_curve"></a>

#### maximum\_height\_by\_distance\_curve

```python
@maximum_height_by_distance_curve.setter
def maximum_height_by_distance_curve(value: CurveFloat) -> None
```

<a id="unreal.CesiumFlyToComponent.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] The length in seconds that the flight should last.

<a id="unreal.CesiumFlyToComponent.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.CesiumFlyToComponent.rotation_to_use"></a>

#### rotation\_to\_use

```python
@property
def rotation_to_use() -> CesiumFlyToRotation
```

(CesiumFlyToRotation):  [Read-Write] Indicates which rotation to use during flights.

<a id="unreal.CesiumFlyToComponent.rotation_to_use"></a>

#### rotation\_to\_use

```python
@rotation_to_use.setter
def rotation_to_use(value: CesiumFlyToRotation) -> None
```

<a id="unreal.CesiumFlyToComponent.on_flight_complete"></a>

#### on\_flight\_complete

```python
@property
def on_flight_complete() -> CesiumFlightCompleted
```

(CesiumFlightCompleted):  [Read-Write] A delegate that will be called when the Actor finishes flying.

<a id="unreal.CesiumFlyToComponent.on_flight_complete"></a>

#### on\_flight\_complete

```python
@on_flight_complete.setter
def on_flight_complete(value: CesiumFlightCompleted) -> None
```

<a id="unreal.CesiumFlyToComponent.on_flight_interrupted"></a>

#### on\_flight\_interrupted

```python
@property
def on_flight_interrupted() -> CesiumFlightInterrupted
```

(CesiumFlightInterrupted):  [Read-Write] A delegate that will be called when the Actor's flight is interrupted.

<a id="unreal.CesiumFlyToComponent.on_flight_interrupted"></a>

#### on\_flight\_interrupted

```python
@on_flight_interrupted.setter
def on_flight_interrupted(value: CesiumFlightInterrupted) -> None
```

<a id="unreal.CesiumFlyToComponent.interrupt_flight"></a>

#### interrupt\_flight

```python
def interrupt_flight() -> None
```

x.interrupt_flight() -> None
Interrupts the flight that is currently in progress, leaving the Actor
wherever it is currently.

<a id="unreal.CesiumFlyToComponent.fly_to_location_unreal"></a>

#### fly\_to\_location\_unreal

```python
def fly_to_location_unreal(unreal_destination: Vector,
                           yaw_at_destination: float,
                           pitch_at_destination: float,
                           can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_unreal(unreal_destination, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth flight to the given destination in Unreal coordinates, such
that the Actor ends at the specified yaw and pitch. The yaw and pitch are
expressed relative to an East-South-Up frame at the destination. The
characteristics of the flight can be configured with the properties on this
component.

If CanInterruptByMoving is true and the Actor moves independent of this
component, then the flight in progress will be canceled.

Args:
    unreal_destination (Vector): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.CesiumFlyToComponent.fly_to_location_longitude_latitude_height"></a>

#### fly\_to\_location\_longitude\_latitude\_height

```python
def fly_to_location_longitude_latitude_height(
        longitude_latitude_height_destination: Vector,
        yaw_at_destination: float, pitch_at_destination: float,
        can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_longitude_latitude_height(longitude_latitude_height_destination, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth camera flight to the given WGS84 longitude in degrees (x),
latitude in degrees (y), and height in meters (z) such that the camera
ends at the given yaw and pitch. The yaw and pitch are expressed relative
to an East-South-Up frame at the destination. The characteristics of the
flight can be configured with the properties on this component.

Note that the height is measured in meters above the WGS84 ellipsoid, and
should not be confused with a height relative to mean sea level, which may
be tens of meters different depending on where you are on the globe.

If CanInterruptByMoving is true and the Actor moves independent of this
component, then the flight in progress will be canceled.

Args:
    longitude_latitude_height_destination (Vector): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.CesiumFlyToComponent.fly_to_location_earth_centered_earth_fixed"></a>

#### fly\_to\_location\_earth\_centered\_earth\_fixed

```python
def fly_to_location_earth_centered_earth_fixed(
        earth_centered_earth_fixed_destination: Vector,
        yaw_at_destination: float, pitch_at_destination: float,
        can_interrupt_by_moving: bool) -> None
```

x.fly_to_location_earth_centered_earth_fixed(earth_centered_earth_fixed_destination, yaw_at_destination, pitch_at_destination, can_interrupt_by_moving) -> None
Begin a smooth flight to the given Earth-Centered, Earth-Fixed
(ECEF) destination, such that the Actor ends at the specified yaw and
pitch. The yaw and pitch are expressed relative to an East-South-Up frame
at the destination. The characteristics of the flight can be configured
with the properties on this component.

If CanInterruptByMoving is true and the Actor moves independent of this
component, then the flight in progress will be canceled.

Args:
    earth_centered_earth_fixed_destination (Vector): 
    yaw_at_destination (double): 
    pitch_at_destination (double): 
    can_interrupt_by_moving (bool):

<a id="unreal.CesiumGeoreference"></a>