## DisplayClusterConfigurationICVFX_CameraDepthOfField Objects

```python
class DisplayClusterConfigurationICVFX_CameraDepthOfField(StructBase)
```

Display Cluster Configuration ICVFX Camera Depth Of Field

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_ICVFX.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatically_set_distance_to_wall`` (bool):  [Read-Write] Allows the ICVFX camera to automatically compute its distance from the stage walls using ray casting every tick
- ``compensation_lut`` (Texture2D):  [Read-Write] Look-up texture that encodes the specific amount of compensation used for each combination of wall distance and object distance
- ``depth_of_field_gain`` (float):  [Read-Write] A gain factor that scales the amount of depth of field blur rendered on the wall
- ``distance_to_wall`` (float):  [Read-Write] The distance from the ICVFX camera to the wall it is pointing at
- ``distance_to_wall_offset`` (float):  [Read-Write] An offset applied to DistanceToWall (applied regardless of whether DistanceToWall is automatically set)
- ``enable_depth_of_field_compensation`` (bool):  [Read-Write] Enables depth of field correction on the wall, which dynamically adjusts the size of the defocus circle of confusion to compensate for the real-world camera blur when shooting the wall

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.__init__"></a>

#### __init__

```python
def __init__(enable_depth_of_field_compensation: bool = False,
             automatically_set_distance_to_wall: bool = False,
             distance_to_wall: float = 0.000000,
             distance_to_wall_offset: float = 0.000000,
             depth_of_field_gain: float = 0.000000,
             compensation_lut: Texture2D = None) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.enable_depth_of_field_compensation"></a>

#### enable_depth_of_field_compensation

```python
@property
def enable_depth_of_field_compensation() -> bool
```

(bool):  [Read-Write] Enables depth of field correction on the wall, which dynamically adjusts the size of the defocus circle of confusion to compensate for the real-world camera blur when shooting the wall

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.enable_depth_of_field_compensation"></a>

#### enable_depth_of_field_compensation

```python
@enable_depth_of_field_compensation.setter
def enable_depth_of_field_compensation(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.automatically_set_distance_to_wall"></a>

#### automatically_set_distance_to_wall

```python
@property
def automatically_set_distance_to_wall() -> bool
```

(bool):  [Read-Write] Allows the ICVFX camera to automatically compute its distance from the stage walls using ray casting every tick

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.automatically_set_distance_to_wall"></a>

#### automatically_set_distance_to_wall

```python
@automatically_set_distance_to_wall.setter
def automatically_set_distance_to_wall(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.distance_to_wall"></a>

#### distance_to_wall

```python
@property
def distance_to_wall() -> float
```

(float):  [Read-Write] The distance from the ICVFX camera to the wall it is pointing at

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.distance_to_wall"></a>

#### distance_to_wall

```python
@distance_to_wall.setter
def distance_to_wall(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.distance_to_wall_offset"></a>

#### distance_to_wall_offset

```python
@property
def distance_to_wall_offset() -> float
```

(float):  [Read-Write] An offset applied to DistanceToWall (applied regardless of whether DistanceToWall is automatically set)

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.distance_to_wall_offset"></a>

#### distance_to_wall_offset

```python
@distance_to_wall_offset.setter
def distance_to_wall_offset(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.depth_of_field_gain"></a>

#### depth_of_field_gain

```python
@property
def depth_of_field_gain() -> float
```

(float):  [Read-Write] A gain factor that scales the amount of depth of field blur rendered on the wall

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.depth_of_field_gain"></a>

#### depth_of_field_gain

```python
@depth_of_field_gain.setter
def depth_of_field_gain(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.compensation_lut"></a>

#### compensation_lut

```python
@property
def compensation_lut() -> Texture2D
```

(Texture2D):  [Read-Write] Look-up texture that encodes the specific amount of compensation used for each combination of wall distance and object distance

<a id="unreal.DisplayClusterConfigurationICVFX_CameraDepthOfField.compensation_lut"></a>

#### compensation_lut

```python
@compensation_lut.setter
def compensation_lut(value: Texture2D) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraSoftEdge"></a>