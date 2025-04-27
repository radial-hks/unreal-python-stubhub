## AnimNotifyState_Trail Objects

```python
class AnimNotifyState_Trail(AnimNotifyState)
```

Anim Notify State Trail

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyState_Trail.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``first_socket_name`` (Name):  [Read-Write] Name of the first socket defining this trail.
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``ps_template`` (ParticleSystem):  [Read-Write] The particle system to use for this trail.
- ``recycle_spawned_systems`` (bool):  [Read-Write]
- ``render_geometry`` (bool):  [Read-Write] If true, render the trail geometry (this should typically be on)
- ``render_spawn_points`` (bool):  [Read-Write] If true, render stars at each spawned particle point along the trail
- ``render_tangents`` (bool):  [Read-Write] If true, render a line showing the tangent at each spawned particle point along the trail
- ``render_tessellation`` (bool):  [Read-Write] If true, render the tessellated path between spawned particles
- ``second_socket_name`` (Name):  [Read-Write] Name of the second socket defining this trail.
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors
- ``width_scale_curve`` (Name):  [Read-Write] Name of the curve to drive the width scale.
- ``width_scale_mode`` (TrailWidthMode):  [Read-Write] Controls the way width scale is applied. In each method a width scale of 1.0 will mean the width is unchanged from the position of the sockets. A width scale of 0.0 will cause a trail of zero width.
  From Centre = Trail width is scaled outwards from the centre point between the two sockets.
  From First = Trail width is scaled outwards from the position of the first socket.
  From Second = Trail width is scaled outwards from the position of the Second socket.

<a id="unreal.AnimNotifyState_Trail.ps_template"></a>

#### ps_template

```python
@property
def ps_template() -> ParticleSystem
```

(ParticleSystem):  [Read-Only] The particle system to use for this trail.

<a id="unreal.AnimNotifyState_Trail.first_socket_name"></a>

#### first_socket_name

```python
@property
def first_socket_name() -> Name
```

(Name):  [Read-Only] Name of the first socket defining this trail.

<a id="unreal.AnimNotifyState_Trail.second_socket_name"></a>

#### second_socket_name

```python
@property
def second_socket_name() -> Name
```

(Name):  [Read-Only] Name of the second socket defining this trail.

<a id="unreal.AnimNotifyState_Trail.width_scale_mode"></a>

#### width_scale_mode

```python
@property
def width_scale_mode() -> TrailWidthMode
```

(TrailWidthMode):  [Read-Only] Controls the way width scale is applied. In each method a width scale of 1.0 will mean the width is unchanged from the position of the sockets. A width scale of 0.0 will cause a trail of zero width.
From Centre = Trail width is scaled outwards from the centre point between the two sockets.
From First = Trail width is scaled outwards from the position of the first socket.
From Second = Trail width is scaled outwards from the position of the Second socket.

<a id="unreal.AnimNotifyState_Trail.width_scale_curve"></a>

#### width_scale_curve

```python
@property
def width_scale_curve() -> Name
```

(Name):  [Read-Only] Name of the curve to drive the width scale.

<a id="unreal.AnimNotifyState_Trail.recycle_spawned_systems"></a>

#### recycle_spawned_systems

```python
@property
def recycle_spawned_systems() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AnimNotifyState_Trail.override_ps_template"></a>

#### override_ps_template

```python
def override_ps_template(mesh_comp: SkeletalMeshComponent,
                         animation: AnimSequenceBase) -> ParticleSystem
```

x.override_ps_template(mesh_comp, animation) -> ParticleSystem
Override PSTemplate

Args:
    mesh_comp (SkeletalMeshComponent): 
    animation (AnimSequenceBase): 

Returns:
    ParticleSystem:

<a id="unreal.AnimNotify_PauseClothingSimulation"></a>