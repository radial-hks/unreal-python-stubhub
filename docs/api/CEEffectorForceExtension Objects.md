## CEEffectorForceExtension Objects

```python
class CEEffectorForceExtension(CEEffectorExtensionBase)
```

Effector supported forces to affect clones

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorForceExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attraction_force_enabled`` (bool):  [Read-Write] Enable attraction force to allow each clone instances to gravitate toward a location
- ``attraction_force_falloff`` (float):  [Read-Write]
- ``attraction_force_strength`` (float):  [Read-Write]
- ``curl_noise_force_enabled`` (bool):  [Read-Write] Enable curl noise force to allow each clone instance to add random location variation
- ``curl_noise_force_frequency`` (float):  [Read-Write]
- ``curl_noise_force_strength`` (float):  [Read-Write]
- ``drag_force_enabled`` (bool):  [Read-Write] Enable drag force to decrease particles velocity
- ``drag_force_linear`` (float):  [Read-Write]
- ``drag_force_rotational`` (float):  [Read-Write]
- ``forces_enabled`` (bool):  [Read-Write] Forces global state
- ``gravity_force_acceleration`` (Vector):  [Read-Write]
- ``gravity_force_enabled`` (bool):  [Read-Write] Enable gravity force to pull particles based on an acceleration vector
- ``orientation_force_enabled`` (bool):  [Read-Write] Enable orientation force to allow each clone instance to rotate around its pivot
- ``orientation_force_max`` (Vector):  [Read-Write]
- ``orientation_force_min`` (Vector):  [Read-Write]
- ``orientation_force_rate`` (float):  [Read-Write]
- ``vector_noise_force_amount`` (float):  [Read-Write]
- ``vector_noise_force_enabled`` (bool):  [Read-Write] Enable vector random noise force to add variation to clones behavior
- ``vortex_force_amount`` (float):  [Read-Write]
- ``vortex_force_axis`` (Vector):  [Read-Write]
- ``vortex_force_enabled`` (bool):  [Read-Write] Enable vortex force to allow each clone instance to rotate around a specific axis on the cloner pivot

<a id="unreal.CEEffectorForceExtension.set_vortex_force_enabled"></a>

#### set_vortex_force_enabled

```python
def set_vortex_force_enabled(force_enabled: bool) -> None
```

x.set_vortex_force_enabled(force_enabled) -> None
Set Vortex Force Enabled

Args:
    force_enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_vortex_force_axis"></a>

#### set_vortex_force_axis

```python
def set_vortex_force_axis(force_vortex_axis: Vector) -> None
```

x.set_vortex_force_axis(force_vortex_axis) -> None
Set Vortex Force Axis

Args:
    force_vortex_axis (Vector):

<a id="unreal.CEEffectorForceExtension.set_vortex_force_amount"></a>

#### set_vortex_force_amount

```python
def set_vortex_force_amount(force_vortex_amount: float) -> None
```

x.set_vortex_force_amount(force_vortex_amount) -> None
Set Vortex Force Amount

Args:
    force_vortex_amount (float):

<a id="unreal.CEEffectorForceExtension.set_vector_noise_force_enabled"></a>

#### set_vector_noise_force_enabled

```python
def set_vector_noise_force_enabled(enabled: bool) -> None
```

x.set_vector_noise_force_enabled(enabled) -> None
Set Vector Noise Force Enabled

Args:
    enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_vector_noise_force_amount"></a>

#### set_vector_noise_force_amount

```python
def set_vector_noise_force_amount(amount: float) -> None
```

x.set_vector_noise_force_amount(amount) -> None
Set Vector Noise Force Amount

Args:
    amount (float):

<a id="unreal.CEEffectorForceExtension.set_orientation_force_rate"></a>

#### set_orientation_force_rate

```python
def set_orientation_force_rate(force_orientation_rate: float) -> None
```

x.set_orientation_force_rate(force_orientation_rate) -> None
Set Orientation Force Rate

Args:
    force_orientation_rate (float):

<a id="unreal.CEEffectorForceExtension.set_orientation_force_min"></a>

#### set_orientation_force_min

```python
def set_orientation_force_min(force_orientation_min: Vector) -> None
```

x.set_orientation_force_min(force_orientation_min) -> None
Set Orientation Force Min

Args:
    force_orientation_min (Vector):

<a id="unreal.CEEffectorForceExtension.set_orientation_force_max"></a>

#### set_orientation_force_max

```python
def set_orientation_force_max(force_orientation_max: Vector) -> None
```

x.set_orientation_force_max(force_orientation_max) -> None
Set Orientation Force Max

Args:
    force_orientation_max (Vector):

<a id="unreal.CEEffectorForceExtension.set_orientation_force_enabled"></a>

#### set_orientation_force_enabled

```python
def set_orientation_force_enabled(force_enabled: bool) -> None
```

x.set_orientation_force_enabled(force_enabled) -> None
Set Orientation Force Enabled

Args:
    force_enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_gravity_force_enabled"></a>

#### set_gravity_force_enabled

```python
def set_gravity_force_enabled(force_enabled: bool) -> None
```

x.set_gravity_force_enabled(force_enabled) -> None
Set Gravity Force Enabled

Args:
    force_enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_gravity_force_acceleration"></a>

#### set_gravity_force_acceleration

```python
def set_gravity_force_acceleration(acceleration: Vector) -> None
```

x.set_gravity_force_acceleration(acceleration) -> None
Set Gravity Force Acceleration

Args:
    acceleration (Vector):

<a id="unreal.CEEffectorForceExtension.set_forces_enabled"></a>

#### set_forces_enabled

```python
def set_forces_enabled(forces_enabled: bool) -> None
```

x.set_forces_enabled(forces_enabled) -> None
Set Forces Enabled

Args:
    forces_enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_drag_force_rotational"></a>

#### set_drag_force_rotational

```python
def set_drag_force_rotational(strength: float) -> None
```

x.set_drag_force_rotational(strength) -> None
Set Drag Force Rotational

Args:
    strength (float):

<a id="unreal.CEEffectorForceExtension.set_drag_force_linear"></a>

#### set_drag_force_linear

```python
def set_drag_force_linear(strength: float) -> None
```

x.set_drag_force_linear(strength) -> None
Set Drag Force Linear

Args:
    strength (float):

<a id="unreal.CEEffectorForceExtension.set_drag_force_enabled"></a>

#### set_drag_force_enabled

```python
def set_drag_force_enabled(enabled: bool) -> None
```

x.set_drag_force_enabled(enabled) -> None
Set Drag Force Enabled

Args:
    enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_curl_noise_force_strength"></a>

#### set_curl_noise_force_strength

```python
def set_curl_noise_force_strength(force_curl_noise_strength: float) -> None
```

x.set_curl_noise_force_strength(force_curl_noise_strength) -> None
Set Curl Noise Force Strength

Args:
    force_curl_noise_strength (float):

<a id="unreal.CEEffectorForceExtension.set_curl_noise_force_frequency"></a>

#### set_curl_noise_force_frequency

```python
def set_curl_noise_force_frequency(force_curl_noise_frequency: float) -> None
```

x.set_curl_noise_force_frequency(force_curl_noise_frequency) -> None
Set Curl Noise Force Frequency

Args:
    force_curl_noise_frequency (float):

<a id="unreal.CEEffectorForceExtension.set_curl_noise_force_enabled"></a>

#### set_curl_noise_force_enabled

```python
def set_curl_noise_force_enabled(force_enabled: bool) -> None
```

x.set_curl_noise_force_enabled(force_enabled) -> None
Set Curl Noise Force Enabled

Args:
    force_enabled (bool):

<a id="unreal.CEEffectorForceExtension.set_attraction_force_strength"></a>

#### set_attraction_force_strength

```python
def set_attraction_force_strength(force_strength: float) -> None
```

x.set_attraction_force_strength(force_strength) -> None
Set Attraction Force Strength

Args:
    force_strength (float):

<a id="unreal.CEEffectorForceExtension.set_attraction_force_falloff"></a>

#### set_attraction_force_falloff

```python
def set_attraction_force_falloff(force_falloff: float) -> None
```

x.set_attraction_force_falloff(force_falloff) -> None
Set Attraction Force Falloff

Args:
    force_falloff (float):

<a id="unreal.CEEffectorForceExtension.set_attraction_force_enabled"></a>

#### set_attraction_force_enabled

```python
def set_attraction_force_enabled(force_enabled: bool) -> None
```

x.set_attraction_force_enabled(force_enabled) -> None
Set Attraction Force Enabled

Args:
    force_enabled (bool):

<a id="unreal.CEEffectorForceExtension.get_vortex_force_enabled"></a>

#### get_vortex_force_enabled

```python
def get_vortex_force_enabled() -> bool
```

x.get_vortex_force_enabled() -> bool
Get Vortex Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_vortex_force_axis"></a>

#### get_vortex_force_axis

```python
def get_vortex_force_axis() -> Vector
```

x.get_vortex_force_axis() -> Vector
Get Vortex Force Axis

Returns:
    Vector:

<a id="unreal.CEEffectorForceExtension.get_vortex_force_amount"></a>

#### get_vortex_force_amount

```python
def get_vortex_force_amount() -> float
```

x.get_vortex_force_amount() -> float
Get Vortex Force Amount

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_vector_noise_force_enabled"></a>

#### get_vector_noise_force_enabled

```python
def get_vector_noise_force_enabled() -> bool
```

x.get_vector_noise_force_enabled() -> bool
Get Vector Noise Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_vector_noise_force_amount"></a>

#### get_vector_noise_force_amount

```python
def get_vector_noise_force_amount() -> float
```

x.get_vector_noise_force_amount() -> float
Get Vector Noise Force Amount

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_orientation_force_rate"></a>

#### get_orientation_force_rate

```python
def get_orientation_force_rate() -> float
```

x.get_orientation_force_rate() -> float
Get Orientation Force Rate

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_orientation_force_min"></a>

#### get_orientation_force_min

```python
def get_orientation_force_min() -> Vector
```

x.get_orientation_force_min() -> Vector
Get Orientation Force Min

Returns:
    Vector:

<a id="unreal.CEEffectorForceExtension.get_orientation_force_max"></a>

#### get_orientation_force_max

```python
def get_orientation_force_max() -> Vector
```

x.get_orientation_force_max() -> Vector
Get Orientation Force Max

Returns:
    Vector:

<a id="unreal.CEEffectorForceExtension.get_orientation_force_enabled"></a>

#### get_orientation_force_enabled

```python
def get_orientation_force_enabled() -> bool
```

x.get_orientation_force_enabled() -> bool
Get Orientation Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_gravity_force_enabled"></a>

#### get_gravity_force_enabled

```python
def get_gravity_force_enabled() -> bool
```

x.get_gravity_force_enabled() -> bool
Get Gravity Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_gravity_force_acceleration"></a>

#### get_gravity_force_acceleration

```python
def get_gravity_force_acceleration() -> Vector
```

x.get_gravity_force_acceleration() -> Vector
Get Gravity Force Acceleration

Returns:
    Vector:

<a id="unreal.CEEffectorForceExtension.get_forces_enabled"></a>

#### get_forces_enabled

```python
def get_forces_enabled() -> bool
```

x.get_forces_enabled() -> bool
Get Forces Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_drag_force_rotational"></a>

#### get_drag_force_rotational

```python
def get_drag_force_rotational() -> float
```

x.get_drag_force_rotational() -> float
Get Drag Force Rotational

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_drag_force_linear"></a>

#### get_drag_force_linear

```python
def get_drag_force_linear() -> float
```

x.get_drag_force_linear() -> float
Get Drag Force Linear

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_drag_force_enabled"></a>

#### get_drag_force_enabled

```python
def get_drag_force_enabled() -> bool
```

x.get_drag_force_enabled() -> bool
Get Drag Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_curl_noise_force_strength"></a>

#### get_curl_noise_force_strength

```python
def get_curl_noise_force_strength() -> float
```

x.get_curl_noise_force_strength() -> float
Get Curl Noise Force Strength

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_curl_noise_force_frequency"></a>

#### get_curl_noise_force_frequency

```python
def get_curl_noise_force_frequency() -> float
```

x.get_curl_noise_force_frequency() -> float
Get Curl Noise Force Frequency

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_curl_noise_force_enabled"></a>

#### get_curl_noise_force_enabled

```python
def get_curl_noise_force_enabled() -> bool
```

x.get_curl_noise_force_enabled() -> bool
Get Curl Noise Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorForceExtension.get_attraction_force_strength"></a>

#### get_attraction_force_strength

```python
def get_attraction_force_strength() -> float
```

x.get_attraction_force_strength() -> float
Get Attraction Force Strength

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_attraction_force_falloff"></a>

#### get_attraction_force_falloff

```python
def get_attraction_force_falloff() -> float
```

x.get_attraction_force_falloff() -> float
Get Attraction Force Falloff

Returns:
    float:

<a id="unreal.CEEffectorForceExtension.get_attraction_force_enabled"></a>

#### get_attraction_force_enabled

```python
def get_attraction_force_enabled() -> bool
```

x.get_attraction_force_enabled() -> bool
Get Attraction Force Enabled

Returns:
    bool:

<a id="unreal.CEEffectorLibrary"></a>