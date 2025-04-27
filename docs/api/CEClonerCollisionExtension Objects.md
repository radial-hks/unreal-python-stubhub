## CEClonerCollisionExtension Objects

```python
class CEClonerCollisionExtension(CEClonerExtensionBase)
```

Extension dealing with collisions and physics related options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerCollisionExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_grid_resolution`` (int32):  [Read-Write] Resolution of the neighbor grid to detect collision between particles
- ``collision_grid_size`` (Vector):  [Read-Write] Size of the neighbor grid to detect collision between particles, particles outside this grid will not have collisions
- ``collision_iterations`` (int32):  [Read-Write] Amount of iterations to improve particle collision results but affects performance
- ``collision_radii`` (Array[float]):  [Read-Write] Radius expected around each particle for collision, order matches attachment index
- ``collision_radius_mode`` (CEClonerCollisionRadiusMode):  [Read-Write] Collision radius calculation mode
- ``collision_velocity_enabled`` (bool):  [Read-Write] Recalculate accurate velocity after collision is updated
- ``mass_max`` (float):  [Read-Write] Maximum particle mass, used for collisions to push apart
- ``mass_min`` (float):  [Read-Write] Minimum particle mass, used for collisions to push apart
- ``particle_collision_enabled`` (bool):  [Read-Write] Allow particles to react to other emitter particles, uses a neighbor grid to detect collision
- ``surface_collision_enabled`` (bool):  [Read-Write] Allow particles to react to surface by using the distance field,
  ensure the mesh you want particle to collide with is tick enough or increase its distance field resolution scale in static mesh editor

<a id="unreal.CEClonerCollisionExtension.set_surface_collision_enabled"></a>

#### set_surface_collision_enabled

```python
def set_surface_collision_enabled(surface_collision_enabled: bool) -> None
```

x.set_surface_collision_enabled(surface_collision_enabled) -> None
Set Surface Collision Enabled

Args:
    surface_collision_enabled (bool):

<a id="unreal.CEClonerCollisionExtension.set_particle_collision_enabled"></a>

#### set_particle_collision_enabled

```python
def set_particle_collision_enabled(particle_collision_enabled: bool) -> None
```

x.set_particle_collision_enabled(particle_collision_enabled) -> None
Set Particle Collision Enabled

Args:
    particle_collision_enabled (bool):

<a id="unreal.CEClonerCollisionExtension.set_mass_min"></a>

#### set_mass_min

```python
def set_mass_min(mass_min: float) -> None
```

x.set_mass_min(mass_min) -> None
Set Mass Min

Args:
    mass_min (float):

<a id="unreal.CEClonerCollisionExtension.set_mass_max"></a>

#### set_mass_max

```python
def set_mass_max(mass_max: float) -> None
```

x.set_mass_max(mass_max) -> None
Set Mass Max

Args:
    mass_max (float):

<a id="unreal.CEClonerCollisionExtension.set_collision_velocity_enabled"></a>

#### set_collision_velocity_enabled

```python
def set_collision_velocity_enabled(collision_velocity_enabled: bool) -> None
```

x.set_collision_velocity_enabled(collision_velocity_enabled) -> None
Set Collision Velocity Enabled

Args:
    collision_velocity_enabled (bool):

<a id="unreal.CEClonerCollisionExtension.set_collision_radius_mode"></a>

#### set_collision_radius_mode

```python
def set_collision_radius_mode(mode: CEClonerCollisionRadiusMode) -> None
```

x.set_collision_radius_mode(mode) -> None
Set Collision Radius Mode

Args:
    mode (CEClonerCollisionRadiusMode):

<a id="unreal.CEClonerCollisionExtension.set_collision_iterations"></a>

#### set_collision_iterations

```python
def set_collision_iterations(collision_iterations: int) -> None
```

x.set_collision_iterations(collision_iterations) -> None
Set Collision Iterations

Args:
    collision_iterations (int32):

<a id="unreal.CEClonerCollisionExtension.set_collision_grid_size"></a>

#### set_collision_grid_size

```python
def set_collision_grid_size(collision_grid_size: Vector) -> None
```

x.set_collision_grid_size(collision_grid_size) -> None
Set Collision Grid Size

Args:
    collision_grid_size (Vector):

<a id="unreal.CEClonerCollisionExtension.set_collision_grid_resolution"></a>

#### set_collision_grid_resolution

```python
def set_collision_grid_resolution(collision_grid_resolution: int) -> None
```

x.set_collision_grid_resolution(collision_grid_resolution) -> None
Set Collision Grid Resolution

Args:
    collision_grid_resolution (int32):

<a id="unreal.CEClonerCollisionExtension.get_surface_collision_enabled"></a>

#### get_surface_collision_enabled

```python
def get_surface_collision_enabled() -> bool
```

x.get_surface_collision_enabled() -> bool
Get Surface Collision Enabled

Returns:
    bool:

<a id="unreal.CEClonerCollisionExtension.get_particle_collision_enabled"></a>

#### get_particle_collision_enabled

```python
def get_particle_collision_enabled() -> bool
```

x.get_particle_collision_enabled() -> bool
Get Particle Collision Enabled

Returns:
    bool:

<a id="unreal.CEClonerCollisionExtension.get_mass_min"></a>

#### get_mass_min

```python
def get_mass_min() -> float
```

x.get_mass_min() -> float
Get Mass Min

Returns:
    float:

<a id="unreal.CEClonerCollisionExtension.get_mass_max"></a>

#### get_mass_max

```python
def get_mass_max() -> float
```

x.get_mass_max() -> float
Get Mass Max

Returns:
    float:

<a id="unreal.CEClonerCollisionExtension.get_collision_velocity_enabled"></a>

#### get_collision_velocity_enabled

```python
def get_collision_velocity_enabled() -> bool
```

x.get_collision_velocity_enabled() -> bool
Get Collision Velocity Enabled

Returns:
    bool:

<a id="unreal.CEClonerCollisionExtension.get_collision_radius_mode"></a>

#### get_collision_radius_mode

```python
def get_collision_radius_mode() -> CEClonerCollisionRadiusMode
```

x.get_collision_radius_mode() -> CEClonerCollisionRadiusMode
Get Collision Radius Mode

Returns:
    CEClonerCollisionRadiusMode:

<a id="unreal.CEClonerCollisionExtension.get_collision_radii"></a>

#### get_collision_radii

```python
def get_collision_radii() -> Array[float]
```

x.get_collision_radii() -> Array[float]
Get Collision Radii

Returns:
    Array[float]:

<a id="unreal.CEClonerCollisionExtension.get_collision_iterations"></a>

#### get_collision_iterations

```python
def get_collision_iterations() -> int
```

x.get_collision_iterations() -> int32
Get Collision Iterations

Returns:
    int32:

<a id="unreal.CEClonerCollisionExtension.get_collision_grid_size"></a>

#### get_collision_grid_size

```python
def get_collision_grid_size() -> Vector
```

x.get_collision_grid_size() -> Vector
Get Collision Grid Size

Returns:
    Vector:

<a id="unreal.CEClonerCollisionExtension.get_collision_grid_resolution"></a>

#### get_collision_grid_resolution

```python
def get_collision_grid_resolution() -> int
```

x.get_collision_grid_resolution() -> int32
Get Collision Grid Resolution

Returns:
    int32:

<a id="unreal.CEClonerConstraintExtension"></a>