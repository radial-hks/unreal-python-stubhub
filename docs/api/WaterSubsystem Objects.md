## WaterSubsystem Objects

```python
class WaterSubsystem(TickableWorldSubsystem)
```

This is the API used to get information about water at runtime

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_camera_underwater_state_changed`` (OnCameraUnderwaterStateChanged):  [Read-Write]
- ``on_water_scalability_changed`` (OnWaterScalabilityChanged):  [Read-Write]

<a id="unreal.WaterSubsystem.on_camera_underwater_state_changed"></a>

#### on\_camera\_underwater\_state\_changed

```python
@property
def on_camera_underwater_state_changed() -> OnCameraUnderwaterStateChanged
```

(OnCameraUnderwaterStateChanged):  [Read-Write]

<a id="unreal.WaterSubsystem.on_camera_underwater_state_changed"></a>

#### on\_camera\_underwater\_state\_changed

```python
@on_camera_underwater_state_changed.setter
def on_camera_underwater_state_changed(
        value: OnCameraUnderwaterStateChanged) -> None
```

<a id="unreal.WaterSubsystem.on_water_scalability_changed"></a>

#### on\_water\_scalability\_changed

```python
@property
def on_water_scalability_changed() -> OnWaterScalabilityChanged
```

(OnWaterScalabilityChanged):  [Read-Write]

<a id="unreal.WaterSubsystem.on_water_scalability_changed"></a>

#### on\_water\_scalability\_changed

```python
@on_water_scalability_changed.setter
def on_water_scalability_changed(value: OnWaterScalabilityChanged) -> None
```

<a id="unreal.WaterSubsystem.set_ocean_flood_height"></a>

#### set\_ocean\_flood\_height

```python
def set_ocean_flood_height(flood_height: float) -> None
```

x.set_ocean_flood_height(flood_height) -> None
Set Ocean Flood Height

Args:
    flood_height (float):

<a id="unreal.WaterSubsystem.print_to_water_log"></a>

#### print\_to\_water\_log

```python
def print_to_water_log(message: str, warning: bool) -> None
```

x.print_to_water_log(message, warning) -> None
Print to Water Log

Args:
    message (str): 
    warning (bool):

<a id="unreal.WaterSubsystem.is_water_rendering_enabled"></a>

#### is\_water\_rendering\_enabled

```python
def is_water_rendering_enabled() -> bool
```

x.is_water_rendering_enabled() -> bool
Is Water Rendering Enabled

Returns:
    bool:

<a id="unreal.WaterSubsystem.is_underwater_post_process_enabled"></a>

#### is\_underwater\_post\_process\_enabled

```python
def is_underwater_post_process_enabled() -> bool
```

x.is_underwater_post_process_enabled() -> bool
Is Underwater Post Process Enabled

Returns:
    bool:

<a id="unreal.WaterSubsystem.is_shallow_water_simulation_enabled"></a>

#### is\_shallow\_water\_simulation\_enabled

```python
def is_shallow_water_simulation_enabled() -> bool
```

x.is_shallow_water_simulation_enabled() -> bool
Is Shallow Water Simulation Enabled

Returns:
    bool:

<a id="unreal.WaterSubsystem.get_water_time_seconds"></a>

#### get\_water\_time\_seconds

```python
def get_water_time_seconds() -> float
```

x.get_water_time_seconds() -> float
Get Water Time Seconds

Returns:
    float:

<a id="unreal.WaterSubsystem.get_smoothed_world_time_seconds"></a>

#### get\_smoothed\_world\_time\_seconds

```python
def get_smoothed_world_time_seconds() -> float
```

x.get_smoothed_world_time_seconds() -> float
Get Smoothed World Time Seconds

Returns:
    float:

<a id="unreal.WaterSubsystem.get_shallow_water_simulation_render_target_size"></a>

#### get\_shallow\_water\_simulation\_render\_target\_size

```python
@classmethod
def get_shallow_water_simulation_render_target_size(cls) -> int
```

X.get_shallow_water_simulation_render_target_size() -> int32
Get Shallow Water Simulation Render Target Size

Returns:
    int32:

<a id="unreal.WaterSubsystem.get_shallow_water_max_impulse_forces"></a>

#### get\_shallow\_water\_max\_impulse\_forces

```python
@classmethod
def get_shallow_water_max_impulse_forces(cls) -> int
```

X.get_shallow_water_max_impulse_forces() -> int32
Get Shallow Water Max Impulse Forces

Returns:
    int32:

<a id="unreal.WaterSubsystem.get_shallow_water_max_dynamic_forces"></a>

#### get\_shallow\_water\_max\_dynamic\_forces

```python
@classmethod
def get_shallow_water_max_dynamic_forces(cls) -> int
```

X.get_shallow_water_max_dynamic_forces() -> int32
Get Shallow Water Max Dynamic Forces

Returns:
    int32:

<a id="unreal.WaterSubsystem.get_ocean_total_height"></a>

#### get\_ocean\_total\_height

```python
def get_ocean_total_height() -> float
```

x.get_ocean_total_height() -> float
Returns the total height of the ocean. This should correspond to the base height plus any additional height, like flood for example

Returns:
    float:

<a id="unreal.WaterSubsystem.get_ocean_flood_height"></a>

#### get\_ocean\_flood\_height

```python
def get_ocean_flood_height() -> float
```

x.get_ocean_flood_height() -> float
Returns the relative flood height

Returns:
    float:

<a id="unreal.WaterSubsystem.get_ocean_base_height"></a>

#### get\_ocean\_base\_height

```python
def get_ocean_base_height() -> float
```

x.get_ocean_base_height() -> float
Returns the base height of the ocean. This should correspond to its world Z position

Returns:
    float:

<a id="unreal.WaterSubsystem.get_camera_underwater_depth"></a>

#### get\_camera\_underwater\_depth

```python
def get_camera_underwater_depth() -> float
```

x.get_camera_underwater_depth() -> float
Get Camera Underwater Depth

Returns:
    float:

<a id="unreal.WaterZone"></a>