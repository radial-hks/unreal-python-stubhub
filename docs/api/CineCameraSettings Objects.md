## CineCameraSettings Objects

```python
class CineCameraSettings(DeveloperSettings)
```

Cine Camera Settings

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``crop_presets`` (Array[NamedPlateCropPreset]):  [Read-Write] List of available crop presets
- ``default_crop_preset_name`` (str):  [Read-Write] Name of the default crop preset
- ``default_filmback_preset`` (str):  [Read-Write] Name of the default filmback preset
- ``default_lens_f_stop`` (float):  [Read-Write] Default aperture (will be constrained by default lens)
- ``default_lens_focal_length`` (float):  [Read-Write] Default focal length (will be constrained by default lens)
- ``default_lens_preset_name`` (str):  [Read-Write] Name of the default lens preset
- ``filmback_presets`` (Array[NamedFilmbackPreset]):  [Read-Write] List of available filmback presets
- ``lens_presets`` (Array[NamedLensPreset]):  [Read-Write] List of available lens presets

<a id="unreal.CineCameraSettings.default_lens_preset_name"></a>

#### default_lens_preset_name

```python
@property
def default_lens_preset_name() -> str
```

(str):  [Read-Write] Name of the default lens preset

<a id="unreal.CineCameraSettings.default_lens_preset_name"></a>

#### default_lens_preset_name

```python
@default_lens_preset_name.setter
def default_lens_preset_name(value: str) -> None
```

<a id="unreal.CineCameraSettings.default_lens_focal_length"></a>

#### default_lens_focal_length

```python
@property
def default_lens_focal_length() -> float
```

(float):  [Read-Write] Default focal length (will be constrained by default lens)

<a id="unreal.CineCameraSettings.default_lens_focal_length"></a>

#### default_lens_focal_length

```python
@default_lens_focal_length.setter
def default_lens_focal_length(value: float) -> None
```

<a id="unreal.CineCameraSettings.default_lens_f_stop"></a>

#### default_lens_f_stop

```python
@property
def default_lens_f_stop() -> float
```

(float):  [Read-Write] Default aperture (will be constrained by default lens)

<a id="unreal.CineCameraSettings.default_lens_f_stop"></a>

#### default_lens_f_stop

```python
@default_lens_f_stop.setter
def default_lens_f_stop(value: float) -> None
```

<a id="unreal.CineCameraSettings.lens_presets"></a>

#### lens_presets

```python
@property
def lens_presets() -> Array[NamedLensPreset]
```

(Array[NamedLensPreset]):  [Read-Write] List of available lens presets

<a id="unreal.CineCameraSettings.lens_presets"></a>

#### lens_presets

```python
@lens_presets.setter
def lens_presets(value: Array[NamedLensPreset]) -> None
```

<a id="unreal.CineCameraSettings.default_filmback_preset"></a>

#### default_filmback_preset

```python
@property
def default_filmback_preset() -> str
```

(str):  [Read-Write] Name of the default filmback preset

<a id="unreal.CineCameraSettings.default_filmback_preset"></a>

#### default_filmback_preset

```python
@default_filmback_preset.setter
def default_filmback_preset(value: str) -> None
```

<a id="unreal.CineCameraSettings.filmback_presets"></a>

#### filmback_presets

```python
@property
def filmback_presets() -> Array[NamedFilmbackPreset]
```

(Array[NamedFilmbackPreset]):  [Read-Write] List of available filmback presets

<a id="unreal.CineCameraSettings.filmback_presets"></a>

#### filmback_presets

```python
@filmback_presets.setter
def filmback_presets(value: Array[NamedFilmbackPreset]) -> None
```

<a id="unreal.CineCameraSettings.default_crop_preset_name"></a>

#### default_crop_preset_name

```python
@property
def default_crop_preset_name() -> str
```

(str):  [Read-Write] Name of the default crop preset

<a id="unreal.CineCameraSettings.default_crop_preset_name"></a>

#### default_crop_preset_name

```python
@default_crop_preset_name.setter
def default_crop_preset_name(value: str) -> None
```

<a id="unreal.CineCameraSettings.crop_presets"></a>

#### crop_presets

```python
@property
def crop_presets() -> Array[NamedPlateCropPreset]
```

(Array[NamedPlateCropPreset]):  [Read-Write] List of available crop presets

<a id="unreal.CineCameraSettings.crop_presets"></a>

#### crop_presets

```python
@crop_presets.setter
def crop_presets(value: Array[NamedPlateCropPreset]) -> None
```

<a id="unreal.CineCameraSettings.get_lens_preset_by_name"></a>

#### get_lens_preset_by_name

```python
def get_lens_preset_by_name(preset_name: str) -> Optional[CameraLensSettings]
```

x.get_lens_preset_by_name(preset_name) -> CameraLensSettings or None
Gets the Lens settings associated with a given preset name
Returns true if a preset with the given name was found

Args:
    preset_name (str): 

Returns:
    CameraLensSettings or None: 

    lens_settings (CameraLensSettings):

<a id="unreal.CineCameraSettings.get_filmback_preset_by_name"></a>

#### get_filmback_preset_by_name

```python
def get_filmback_preset_by_name(
        preset_name: str) -> Optional[CameraFilmbackSettings]
```

x.get_filmback_preset_by_name(preset_name) -> CameraFilmbackSettings or None
Gets the Filmback settings associated with a given preset name
Returns true if a preset with the given name was found

Args:
    preset_name (str): 

Returns:
    CameraFilmbackSettings or None: 

    filmback_settings (CameraFilmbackSettings):

<a id="unreal.CineCameraSettings.get_crop_preset_by_name"></a>

#### get_crop_preset_by_name

```python
def get_crop_preset_by_name(preset_name: str) -> Optional[PlateCropSettings]
```

x.get_crop_preset_by_name(preset_name) -> PlateCropSettings or None
Gets the Crop settings associated with a given preset name
Returns true if a preset with the given name was found

Args:
    preset_name (str): 

Returns:
    PlateCropSettings or None: 

    crop_settings (PlateCropSettings):

<a id="unreal.CineCameraSettings.get_cine_camera_settings"></a>

#### get_cine_camera_settings

```python
@classmethod
def get_cine_camera_settings(cls) -> CineCameraSettings
```

X.get_cine_camera_settings() -> CineCameraSettings
Get Cine Camera Settings

Returns:
    CineCameraSettings:

<a id="unreal.AutomatedLevelSequenceCapture"></a>