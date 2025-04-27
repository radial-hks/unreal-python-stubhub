## BuoyancyComponent Objects

```python
class BuoyancyComponent(ActorComponent)
```

Buoyancy Component

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: BuoyancyComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``buoyancy_data`` (BuoyancyData):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_entered_water_delegate`` (OnPontoonEnteredWater):  [Read-Write]
- ``on_exited_water_delegate`` (OnPontoonExitedWater):  [Read-Write]
- ``pontoons`` (Array[SphericalPontoon]):  [Read-Write]
  deprecated: Use BuoyancyData.Pontoons instead.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.BuoyancyComponent.pontoons"></a>

#### pontoons

```python
@property
def pontoons() -> Array[SphericalPontoon]
```

(Array[SphericalPontoon]):  [Read-Write]
deprecated: Use BuoyancyData.Pontoons instead.

<a id="unreal.BuoyancyComponent.pontoons"></a>

#### pontoons

```python
@pontoons.setter
def pontoons(value: Array[SphericalPontoon]) -> None
```

<a id="unreal.BuoyancyComponent.on_entered_water_delegate"></a>

#### on_entered_water_delegate

```python
@property
def on_entered_water_delegate() -> OnPontoonEnteredWater
```

(OnPontoonEnteredWater):  [Read-Write]

<a id="unreal.BuoyancyComponent.on_entered_water_delegate"></a>

#### on_entered_water_delegate

```python
@on_entered_water_delegate.setter
def on_entered_water_delegate(value: OnPontoonEnteredWater) -> None
```

<a id="unreal.BuoyancyComponent.on_exited_water_delegate"></a>

#### on_exited_water_delegate

```python
@property
def on_exited_water_delegate() -> OnPontoonExitedWater
```

(OnPontoonExitedWater):  [Read-Write]

<a id="unreal.BuoyancyComponent.on_exited_water_delegate"></a>

#### on_exited_water_delegate

```python
@on_exited_water_delegate.setter
def on_exited_water_delegate(value: OnPontoonExitedWater) -> None
```

<a id="unreal.BuoyancyComponent.buoyancy_data"></a>

#### buoyancy_data

```python
@property
def buoyancy_data() -> BuoyancyData
```

(BuoyancyData):  [Read-Only]

<a id="unreal.BuoyancyComponent.on_pontoon_exited_water"></a>

#### on_pontoon_exited_water

```python
def on_pontoon_exited_water(pontoon: SphericalPontoon) -> None
```

x.on_pontoon_exited_water(pontoon) -> None
On Pontoon Exited Water

Args:
    pontoon (SphericalPontoon):

<a id="unreal.BuoyancyComponent.on_pontoon_entered_water"></a>

#### on_pontoon_entered_water

```python
def on_pontoon_entered_water(pontoon: SphericalPontoon) -> None
```

x.on_pontoon_entered_water(pontoon) -> None
On Pontoon Entered Water

Args:
    pontoon (SphericalPontoon):

<a id="unreal.BuoyancyComponent.is_overlapping_water_body"></a>

#### is_overlapping_water_body

```python
def is_overlapping_water_body() -> bool
```

x.is_overlapping_water_body() -> bool
Is Overlapping Water Body

Returns:
    bool:

<a id="unreal.BuoyancyComponent.is_in_water_body"></a>

#### is_in_water_body

```python
def is_in_water_body() -> bool
```

x.is_in_water_body() -> bool
Is in Water Body

Returns:
    bool:

<a id="unreal.BuoyancyComponent.get_last_water_surface_info"></a>

#### get_last_water_surface_info

```python
def get_last_water_surface_info(
) -> Tuple[Vector, Vector, Vector, float, int, Vector]
```

x.get_last_water_surface_info() -> (out_water_plane_location=Vector, out_water_plane_normal=Vector, out_water_surface_position=Vector, out_water_depth=float, out_water_body_idx=int32, out_water_velocity=Vector)
Get Last Water Surface Info

Returns:
    tuple: 

    out_water_plane_location (Vector): 

    out_water_plane_normal (Vector): 

    out_water_surface_position (Vector): 

    out_water_depth (float): 

    out_water_body_idx (int32): 

    out_water_velocity (Vector):

<a id="unreal.BuoyancyComponent.get_current_water_body_components"></a>

#### get_current_water_body_components

```python
def get_current_water_body_components() -> Array[WaterBodyComponent]
```

x.get_current_water_body_components() -> Array[WaterBodyComponent]
Get Current Water Body Components

Returns:
    Array[WaterBodyComponent]:

<a id="unreal.BuoyancyManager"></a>