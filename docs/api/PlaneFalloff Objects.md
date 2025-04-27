## PlaneFalloff Objects

```python
class PlaneFalloff(FieldNodeFloat)
```

Plane scalar field that will be defined only within a distance from a plane

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``default`` (float):  [Read-Write] The field value will be set to Default if the sample distance from the plane is higher than the distance
- ``distance`` (float):  [Read-Write] Distance limit for the plane falloff field
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``falloff`` (FieldFalloffType):  [Read-Write] Type of falloff function used to model the evolution of the field from the plane surface to the distance isosurface
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``magnitude`` (float):  [Read-Write] Magnitude of the plane falloff field
- ``max_range`` (float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
- ``min_range`` (float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
- ``normal`` (Vector):  [Read-Write] Plane normal of the plane falloff field
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``position`` (Vector):  [Read-Write] Plane position of the plane falloff field
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.PlaneFalloff.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write] Magnitude of the plane falloff field

<a id="unreal.PlaneFalloff.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.PlaneFalloff.min_range"></a>

#### min_range

```python
@property
def min_range() -> float
```

(float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude

<a id="unreal.PlaneFalloff.min_range"></a>

#### min_range

```python
@min_range.setter
def min_range(value: float) -> None
```

<a id="unreal.PlaneFalloff.max_range"></a>

#### max_range

```python
@property
def max_range() -> float
```

(float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude

<a id="unreal.PlaneFalloff.max_range"></a>

#### max_range

```python
@max_range.setter
def max_range(value: float) -> None
```

<a id="unreal.PlaneFalloff.default"></a>

#### default

```python
@property
def default() -> float
```

(float):  [Read-Write] The field value will be set to Default if the sample distance from the plane is higher than the distance

<a id="unreal.PlaneFalloff.default"></a>

#### default

```python
@default.setter
def default(value: float) -> None
```

<a id="unreal.PlaneFalloff.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write] Distance limit for the plane falloff field

<a id="unreal.PlaneFalloff.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.PlaneFalloff.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Plane position of the plane falloff field

<a id="unreal.PlaneFalloff.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.PlaneFalloff.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Write] Plane normal of the plane falloff field

<a id="unreal.PlaneFalloff.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector) -> None
```

<a id="unreal.PlaneFalloff.falloff"></a>

#### falloff

```python
@property
def falloff() -> FieldFalloffType
```

(FieldFalloffType):  [Read-Write] Type of falloff function used to model the evolution of the field from the plane surface to the distance isosurface

<a id="unreal.PlaneFalloff.falloff"></a>

#### falloff

```python
@falloff.setter
def falloff(value: FieldFalloffType) -> None
```

<a id="unreal.PlaneFalloff.set_plane_falloff"></a>

#### set_plane_falloff

```python
def set_plane_falloff(magnitude: float = 1.000000,
                      min_range: float = 0.000000,
                      max_range: float = 1.000000,
                      default: float = ...,
                      distance: float = ...,
                      position: Vector = ...,
                      normal: Vector = ...,
                      falloff: FieldFalloffType = ...) -> PlaneFalloff
```

x.set_plane_falloff(magnitude=1.000000, min_range=0.000000, max_range=1.000000, default, distance, position, normal, falloff) -> PlaneFalloff
Plane scalar field that will be defined only within a distance from a plane

Args:
    magnitude (float): Magnitude of the plane falloff field
    min_range (float): The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
    max_range (float): The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
    default (float): The field value will be set to default if the sample projected distance ((Sample Position - Center Position).dot(Plane Normal)) is higher than the Plane Distance
    distance (float): Distance limit for the plane falloff field starting from the center position and extending in the direction of the plane normal
    position (Vector): Plane center position of the plane falloff field
    normal (Vector): Plane normal of the plane falloff field
    falloff (FieldFalloffType): Type of falloff function used to model the evolution of the field from the plane surface to the distance isosurface

Returns:
    PlaneFalloff:

<a id="unreal.BoxFalloff"></a>