## NamedLensPreset Objects

```python
class NamedLensPreset(StructBase)
```

A named bundle of lens settings used to implement lens presets.

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lens_settings`` (CameraLensSettings):  [Read-Write]
- ``name`` (str):  [Read-Write] Name for the preset.

<a id="unreal.NamedLensPreset.__init__"></a>

#### __init__

```python
def __init__(
    name: str = "",
    lens_settings: CameraLensSettings = [
        50.000000, 50.000000, 2.000000, 2.000000, 15.000000, 1.000000, 5
    ]
) -> None
```

<a id="unreal.NamedLensPreset.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Name for the preset.

<a id="unreal.NamedLensPreset.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.NamedLensPreset.lens_settings"></a>

#### lens_settings

```python
@property
def lens_settings() -> CameraLensSettings
```

(CameraLensSettings):  [Read-Write]

<a id="unreal.NamedLensPreset.lens_settings"></a>

#### lens_settings

```python
@lens_settings.setter
def lens_settings(value: CameraLensSettings) -> None
```

<a id="unreal.PlateCropSettings"></a>