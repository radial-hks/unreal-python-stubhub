## CEEffectorNoiseMode Objects

```python
class CEEffectorNoiseMode(CEEffectorModeBase)
```

CEEffector Noise Mode

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorNoiseMode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (float):  [Read-Write] Intensity of the noise field
- ``location_strength`` (Vector):  [Read-Write] Amplitude of the noise field for location
- ``pan`` (Vector):  [Read-Write] Panning to offset the noise field sampling
- ``rotation_strength`` (Rotator):  [Read-Write] Amplitude of the noise field for rotation
- ``scale_strength`` (Vector):  [Read-Write] Amplitude of the noise field for scale

<a id="unreal.CEEffectorNoiseMode.set_scale_strength"></a>

#### set_scale_strength

```python
def set_scale_strength(strength: Vector) -> None
```

x.set_scale_strength(strength) -> None
Set Scale Strength

Args:
    strength (Vector):

<a id="unreal.CEEffectorNoiseMode.set_rotation_strength"></a>

#### set_rotation_strength

```python
def set_rotation_strength(strength: Rotator) -> None
```

x.set_rotation_strength(strength) -> None
Set Rotation Strength

Args:
    strength (Rotator):

<a id="unreal.CEEffectorNoiseMode.set_pan"></a>

#### set_pan

```python
def set_pan(pan: Vector) -> None
```

x.set_pan(pan) -> None
Set Pan

Args:
    pan (Vector):

<a id="unreal.CEEffectorNoiseMode.set_location_strength"></a>

#### set_location_strength

```python
def set_location_strength(strength: Vector) -> None
```

x.set_location_strength(strength) -> None
Set Location Strength

Args:
    strength (Vector):

<a id="unreal.CEEffectorNoiseMode.set_frequency"></a>

#### set_frequency

```python
def set_frequency(frequency: float) -> None
```

x.set_frequency(frequency) -> None
Set Frequency

Args:
    frequency (float):

<a id="unreal.CEEffectorNoiseMode.get_scale_strength"></a>

#### get_scale_strength

```python
def get_scale_strength() -> Vector
```

x.get_scale_strength() -> Vector
Get Scale Strength

Returns:
    Vector:

<a id="unreal.CEEffectorNoiseMode.get_rotation_strength"></a>

#### get_rotation_strength

```python
def get_rotation_strength() -> Rotator
```

x.get_rotation_strength() -> Rotator
Get Rotation Strength

Returns:
    Rotator:

<a id="unreal.CEEffectorNoiseMode.get_pan"></a>

#### get_pan

```python
def get_pan() -> Vector
```

x.get_pan() -> Vector
Get Pan

Returns:
    Vector:

<a id="unreal.CEEffectorNoiseMode.get_location_strength"></a>

#### get_location_strength

```python
def get_location_strength() -> Vector
```

x.get_location_strength() -> Vector
Get Location Strength

Returns:
    Vector:

<a id="unreal.CEEffectorNoiseMode.get_frequency"></a>

#### get_frequency

```python
def get_frequency() -> float
```

x.get_frequency() -> float
Get Frequency

Returns:
    float:

<a id="unreal.CEEffectorOffsetMode"></a>