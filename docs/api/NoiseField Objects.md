## NoiseField Objects

```python
class NoiseField(FieldNodeFloat)
```

Defines a perlin noise scalar value if the sample is within a box

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``max_range`` (float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange
- ``min_range`` (float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``transform`` (Transform):  [Read-Write] Transform of the box in which the perlin noise will be defined

<a id="unreal.NoiseField.min_range"></a>

#### min_range

```python
@property
def min_range() -> float
```

(float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange

<a id="unreal.NoiseField.min_range"></a>

#### min_range

```python
@min_range.setter
def min_range(value: float) -> None
```

<a id="unreal.NoiseField.max_range"></a>

#### max_range

```python
@property
def max_range() -> float
```

(float):  [Read-Write] The initial function value between 0 and 1 will be scaled between MinRange and MaxRange

<a id="unreal.NoiseField.max_range"></a>

#### max_range

```python
@max_range.setter
def max_range(value: float) -> None
```

<a id="unreal.NoiseField.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] Transform of the box in which the perlin noise will be defined

<a id="unreal.NoiseField.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.NoiseField.set_noise_field"></a>

#### set_noise_field

```python
def set_noise_field(min_range: float = 0.000000,
                    max_range: float = 1.000000,
                    transform: Transform = ...) -> NoiseField
```

x.set_noise_field(min_range=0.000000, max_range=1.000000, transform) -> NoiseField
Defines a perlin noise scalar value if the sample is within a box

Args:
    min_range (float): The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
    max_range (float): The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
    transform (Transform): Transform of the box in which the perlin noise will be defined

Returns:
    NoiseField:

<a id="unreal.UniformVector"></a>