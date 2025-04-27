## NamedPlateCropPreset Objects

```python
class NamedPlateCropPreset(StructBase)
```

A named bundle of crop settings used to implement crop presets.

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``crop_settings`` (PlateCropSettings):  [Read-Write]
- ``name`` (str):  [Read-Write] Name for the preset.

<a id="unreal.NamedPlateCropPreset.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             crop_settings: PlateCropSettings = [0.000000]) -> None
```

<a id="unreal.NamedPlateCropPreset.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Name for the preset.

<a id="unreal.NamedPlateCropPreset.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.NamedPlateCropPreset.crop_settings"></a>

#### crop_settings

```python
@property
def crop_settings() -> PlateCropSettings
```

(PlateCropSettings):  [Read-Write]

<a id="unreal.NamedPlateCropPreset.crop_settings"></a>

#### crop_settings

```python
@crop_settings.setter
def crop_settings(value: PlateCropSettings) -> None
```

<a id="unreal.CameraTrackingFocusSettings"></a>