## SkyCreatorBackgroundCloudSettings Objects

```python
class SkyCreatorBackgroundCloudSettings(StructBase)
```

Sky Creator Background Cloud Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_clouds_color_tint`` (LinearColor):  [Read-Write] Color Tint of Background Clouds.
- ``background_clouds_intensity`` (float):  [Read-Write] Overall intensity of Background Clouds.
- ``background_clouds_layer_a`` (float):  [Read-Write] Amount of 'Layer A' in Background Clouds.
- ``background_clouds_layer_b`` (float):  [Read-Write] Amount of 'Layer B' in Background Clouds.
- ``background_clouds_layer_c`` (float):  [Read-Write] Amount of 'Layer C' in Background Clouds.
- ``background_clouds_lightning_phase`` (float):  [Read-Write] Amount of Lightning Phase in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(background_clouds_intensity: float = 0.000000,
             background_clouds_color_tint: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             background_clouds_layer_a: float = 0.000000,
             background_clouds_layer_b: float = 0.000000,
             background_clouds_layer_c: float = 0.000000,
             background_clouds_lightning_phase: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_intensity"></a>

#### background\_clouds\_intensity

```python
@property
def background_clouds_intensity() -> float
```

(float):  [Read-Write] Overall intensity of Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_intensity"></a>

#### background\_clouds\_intensity

```python
@background_clouds_intensity.setter
def background_clouds_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_color_tint"></a>

#### background\_clouds\_color\_tint

```python
@property
def background_clouds_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Color Tint of Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_color_tint"></a>

#### background\_clouds\_color\_tint

```python
@background_clouds_color_tint.setter
def background_clouds_color_tint(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_a"></a>

#### background\_clouds\_layer\_a

```python
@property
def background_clouds_layer_a() -> float
```

(float):  [Read-Write] Amount of 'Layer A' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_a"></a>

#### background\_clouds\_layer\_a

```python
@background_clouds_layer_a.setter
def background_clouds_layer_a(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_b"></a>

#### background\_clouds\_layer\_b

```python
@property
def background_clouds_layer_b() -> float
```

(float):  [Read-Write] Amount of 'Layer B' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_b"></a>

#### background\_clouds\_layer\_b

```python
@background_clouds_layer_b.setter
def background_clouds_layer_b(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_c"></a>

#### background\_clouds\_layer\_c

```python
@property
def background_clouds_layer_c() -> float
```

(float):  [Read-Write] Amount of 'Layer C' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_layer_c"></a>

#### background\_clouds\_layer\_c

```python
@background_clouds_layer_c.setter
def background_clouds_layer_c(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_lightning_phase"></a>

#### background\_clouds\_lightning\_phase

```python
@property
def background_clouds_lightning_phase() -> float
```

(float):  [Read-Write] Amount of Lightning Phase in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings.background_clouds_lightning_phase"></a>

#### background\_clouds\_lightning\_phase

```python
@background_clouds_lightning_phase.setter
def background_clouds_lightning_phase(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings"></a>