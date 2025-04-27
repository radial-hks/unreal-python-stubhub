## NamedFilmbackPreset Objects

```python
class NamedFilmbackPreset(StructBase)
```

A named bundle of filmback settings used to implement filmback presets

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filmback_settings`` (CameraFilmbackSettings):  [Read-Write]
- ``name`` (str):  [Read-Write] Name for the preset.

<a id="unreal.NamedFilmbackPreset.__init__"></a>

#### __init__

```python
def __init__(
    name: str = "",
    filmback_settings: CameraFilmbackSettings = [
        24.889999, 18.670000, 0.000000, 0.000000, 1.330000
    ]
) -> None
```

<a id="unreal.NamedFilmbackPreset.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Name for the preset.

<a id="unreal.NamedFilmbackPreset.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.NamedFilmbackPreset.filmback_settings"></a>

#### filmback_settings

```python
@property
def filmback_settings() -> CameraFilmbackSettings
```

(CameraFilmbackSettings):  [Read-Write]

<a id="unreal.NamedFilmbackPreset.filmback_settings"></a>

#### filmback_settings

```python
@filmback_settings.setter
def filmback_settings(value: CameraFilmbackSettings) -> None
```

<a id="unreal.CameraLensSettings"></a>