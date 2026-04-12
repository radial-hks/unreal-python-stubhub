## SkyCreatorFunctionLibrary Objects

```python
class SkyCreatorFunctionLibrary(BlueprintFunctionLibrary)
```

Sky Creator Function Library

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorFunctionLibrary.h

<a id="unreal.SkyCreatorFunctionLibrary.kilometers_to_centimeters"></a>

#### kilometers\_to\_centimeters

```python
@classmethod
def kilometers_to_centimeters(cls, value: float) -> float
```

X.kilometers_to_centimeters(value) -> float
Convert Kilometers to Centimeters

Args:
    value (float): 

Returns:
    float:

<a id="unreal.SkyCreatorFunctionLibrary.is_application_foreground_now"></a>

#### is\_application\_foreground\_now

```python
@classmethod
def is_application_foreground_now(cls) -> bool
```

X.is_application_foreground_now() -> bool
Is Application Foreground Now

Returns:
    bool:

<a id="unreal.SkyCreatorFunctionLibrary.get_real_sun_position"></a>

#### get\_real\_sun\_position

```python
@classmethod
def get_real_sun_position(cls, latitude: float, longitude: float,
                          time_zone: float, is_daylight_saving_time: bool,
                          date_time: DateTime) -> CelestialPositionData
```

X.get_real_sun_position(latitude, longitude, time_zone, is_daylight_saving_time, date_time) -> CelestialPositionData
Get Real Sun Position

Args:
    latitude (float): 
    longitude (float): 
    time_zone (float): 
    is_daylight_saving_time (bool): 
    date_time (DateTime): 

Returns:
    CelestialPositionData:

<a id="unreal.SkyCreatorFunctionLibrary.get_real_moon_position"></a>

#### get\_real\_moon\_position

```python
@classmethod
def get_real_moon_position(cls, latitude: float, longitude: float,
                           time_zone: float, is_daylight_saving_time: bool,
                           date_time: DateTime) -> CelestialPositionData
```

X.get_real_moon_position(latitude, longitude, time_zone, is_daylight_saving_time, date_time) -> CelestialPositionData
Get Real Moon Position

Args:
    latitude (float): 
    longitude (float): 
    time_zone (float): 
    is_daylight_saving_time (bool): 
    date_time (DateTime): 

Returns:
    CelestialPositionData:

<a id="unreal.SkyCreatorFunctionLibrary.get_cloud_density_at_position"></a>

#### get\_cloud\_density\_at\_position

```python
@classmethod
def get_cloud_density_at_position(
        cls, world_context_object: Object, position: Vector,
        parameter_collection: MaterialParameterCollection,
        material: MaterialInterface,
        render_target: TextureRenderTarget2D) -> float
```

X.get_cloud_density_at_position(world_context_object, position, parameter_collection, material, render_target) -> float
Get Cloud Density at Position

Args:
    world_context_object (Object): 
    position (Vector): 
    parameter_collection (MaterialParameterCollection): 
    material (MaterialInterface): 
    render_target (TextureRenderTarget2D): 

Returns:
    float:

<a id="unreal.SkyCreatorFunctionLibrary.find_lightning_position"></a>

#### find\_lightning\_position

```python
@classmethod
def find_lightning_position(cls, world_context_object: Object,
                            sample_cloud_density: bool, samples: int,
                            parameter_collection: MaterialParameterCollection,
                            material: MaterialInterface,
                            render_target: TextureRenderTarget2D,
                            position: Vector, inner_radius: float,
                            outer_radius: float, min_height: float,
                            max_height: float,
                            density_threshold: float) -> Optional[Vector]
```

X.find_lightning_position(world_context_object, sample_cloud_density, samples, parameter_collection, material, render_target, position, inner_radius, outer_radius, min_height, max_height, density_threshold) -> Vector or None
Find Lightning Position

Args:
    world_context_object (Object): 
    sample_cloud_density (bool): 
    samples (int32): 
    parameter_collection (MaterialParameterCollection): 
    material (MaterialInterface): 
    render_target (TextureRenderTarget2D): 
    position (Vector): 
    inner_radius (float): 
    outer_radius (float): 
    min_height (float): 
    max_height (float): 
    density_threshold (float): 

Returns:
    Vector or None: 

    out_position (Vector):

<a id="unreal.SkyCreatorFunctionLibrary.dynamic_convert_render_target_to_texture2d"></a>

#### dynamic\_convert\_render\_target\_to\_texture2d

```python
def dynamic_convert_render_target_to_texture2d(
        render_target: TextureRenderTarget2D) -> Texture2D
```

x.dynamic_convert_render_target_to_texture2d(render_target) -> Texture2D
Dynamic Convert Render Target to Texture 2D

Args:
    render_target (TextureRenderTarget2D): 

Returns:
    Texture2D:

<a id="unreal.SkyCreatorFunctionLibrary.create_and_assign_mid"></a>

#### create\_and\_assign\_mid

```python
@classmethod
def create_and_assign_mid(
        cls, world_context_object: Object,
        material: MaterialInterface) -> MaterialInstanceDynamic
```

X.create_and_assign_mid(world_context_object, material) -> MaterialInstanceDynamic
Create and Assign MID

Args:
    world_context_object (Object): 
    material (MaterialInterface): 

Returns:
    MaterialInstanceDynamic: 

    mid (MaterialInstanceDynamic):

<a id="unreal.SkyCreatorFunctionLibrary.convert_render_target_to_texture2d"></a>

#### convert\_render\_target\_to\_texture2d

```python
@classmethod
def convert_render_target_to_texture2d(
        cls, render_target: TextureRenderTarget2D) -> Texture2D
```

X.convert_render_target_to_texture2d(render_target) -> Texture2D
Convert Render Target to Texture 2D

Args:
    render_target (TextureRenderTarget2D): 

Returns:
    Texture2D: 

    texture (Texture2D):

<a id="unreal.SkyCreatorFunctionLibrary.check_cloud_density_at_position"></a>

#### check\_cloud\_density\_at\_position

```python
@classmethod
def check_cloud_density_at_position(
        cls, world_context_object: Object, position: Vector,
        parameter_collection: MaterialParameterCollection,
        material: MaterialInterface,
        render_target: TextureRenderTarget2D) -> bool
```

X.check_cloud_density_at_position(world_context_object, position, parameter_collection, material, render_target) -> bool
Check Cloud Density at Position

Args:
    world_context_object (Object): 
    position (Vector): 
    parameter_collection (MaterialParameterCollection): 
    material (MaterialInterface): 
    render_target (TextureRenderTarget2D): 

Returns:
    bool:

<a id="unreal.SkyCreatorFunctionLibrary.centimeters_to_kilometers"></a>

#### centimeters\_to\_kilometers

```python
@classmethod
def centimeters_to_kilometers(cls, value: float) -> float
```

X.centimeters_to_kilometers(value) -> float
Convert Centimeters to Kilometers

Args:
    value (float): 

Returns:
    float:

<a id="unreal.SkyCreatorWeatherPreset"></a>