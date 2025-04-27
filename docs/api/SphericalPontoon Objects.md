## SphericalPontoon Objects

```python
class SphericalPontoon(StructBase)
```

Spherical Pontoon

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: BuoyancyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_location`` (Vector):  [Read-Write]
- ``center_socket`` (Name):  [Read-Write] The socket to center this pontoon on. Also used as the name of the pontoon for effects
- ``current_water_body_component`` (WaterBodyComponent):  [Read-Write]
- ``fx_enabled`` (bool):  [Read-Write] Should this pontoon be considered as a candidate location for visual/audio effects upon entering water for burst cues? To be implemented by user
- ``immersion_depth`` (float):  [Read-Write]
- ``is_in_water`` (bool):  [Read-Write]
- ``local_force`` (Vector):  [Read-Write]
- ``offset`` (Vector):  [Read-Write]
- ``radius`` (float):  [Read-Write] The radius of the pontoon
- ``relative_location`` (Vector):  [Read-Write] Relative Location of pontoon WRT parent actor. Overridden by Center Socket.
- ``socket_rotation`` (Quat):  [Read-Write]
- ``water_body_index`` (int32):  [Read-Write]
- ``water_depth`` (float):  [Read-Write]
- ``water_height`` (float):  [Read-Write]
- ``water_plane_location`` (Vector):  [Read-Write]
- ``water_plane_normal`` (Vector):  [Read-Write]
- ``water_surface_position`` (Vector):  [Read-Write]
- ``water_velocity`` (Vector):  [Read-Write]

<a id="unreal.SphericalPontoon.__init__"></a>

#### __init__

```python
def __init__(center_socket: Name = "None",
             relative_location: Vector = [0.000000, 0.000000, 0.000000],
             radius: float = 0.000000,
             fx_enabled: bool = False,
             local_force: Vector = [0.000000, 0.000000, 0.000000],
             center_location: Vector = [0.000000, 0.000000, 0.000000],
             socket_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             offset: Vector = [0.000000, 0.000000, 0.000000],
             water_height: float = 0.000000,
             water_depth: float = 0.000000,
             immersion_depth: float = 0.000000,
             water_plane_location: Vector = [0.000000, 0.000000, 0.000000],
             water_plane_normal: Vector = [0.000000, 0.000000, 0.000000],
             water_surface_position: Vector = [0.000000, 0.000000, 0.000000],
             water_velocity: Vector = [0.000000, 0.000000, 0.000000],
             water_body_index: int = 0,
             is_in_water: bool = False,
             current_water_body_component: WaterBodyComponent = None) -> None
```

<a id="unreal.SphericalPontoon.center_socket"></a>

#### center_socket

```python
@property
def center_socket() -> Name
```

(Name):  [Read-Only] The socket to center this pontoon on. Also used as the name of the pontoon for effects

<a id="unreal.SphericalPontoon.relative_location"></a>

#### relative_location

```python
@property
def relative_location() -> Vector
```

(Vector):  [Read-Only] Relative Location of pontoon WRT parent actor. Overridden by Center Socket.

<a id="unreal.SphericalPontoon.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Only] The radius of the pontoon

<a id="unreal.SphericalPontoon.fx_enabled"></a>

#### fx_enabled

```python
@property
def fx_enabled() -> bool
```

(bool):  [Read-Only] Should this pontoon be considered as a candidate location for visual/audio effects upon entering water for burst cues? To be implemented by user

<a id="unreal.SphericalPontoon.local_force"></a>

#### local_force

```python
@property
def local_force() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.center_location"></a>

#### center_location

```python
@property
def center_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.socket_rotation"></a>

#### socket_rotation

```python
@property
def socket_rotation() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.SphericalPontoon.offset"></a>

#### offset

```python
@property
def offset() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.water_height"></a>

#### water_height

```python
@property
def water_height() -> float
```

(float):  [Read-Only]

<a id="unreal.SphericalPontoon.water_depth"></a>

#### water_depth

```python
@property
def water_depth() -> float
```

(float):  [Read-Only]

<a id="unreal.SphericalPontoon.immersion_depth"></a>

#### immersion_depth

```python
@property
def immersion_depth() -> float
```

(float):  [Read-Only]

<a id="unreal.SphericalPontoon.water_plane_location"></a>

#### water_plane_location

```python
@property
def water_plane_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.water_plane_normal"></a>

#### water_plane_normal

```python
@property
def water_plane_normal() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.water_surface_position"></a>

#### water_surface_position

```python
@property
def water_surface_position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.water_velocity"></a>

#### water_velocity

```python
@property
def water_velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SphericalPontoon.water_body_index"></a>

#### water_body_index

```python
@property
def water_body_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.SphericalPontoon.is_in_water"></a>

#### is_in_water

```python
@property
def is_in_water() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SphericalPontoon.current_water_body_component"></a>

#### current_water_body_component

```python
@property
def current_water_body_component() -> WaterBodyComponent
```

(WaterBodyComponent):  [Read-Only]

<a id="unreal.BlueprintSessionResult"></a>