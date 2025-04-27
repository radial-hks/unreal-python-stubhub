## FilmbackOverrideSource Objects

```python
class FilmbackOverrideSource(EnumBase)
```

Controls whether this component can override the camera's filmback, and if so, which override to use

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponent
- **File**: LensComponent.h

<a id="unreal.FilmbackOverrideSource.LENS_FILE"></a>

#### LENS_FILE

0: Override the camera's filmback using the sensor dimensions recorded in the LensInfo of the LensFile

<a id="unreal.FilmbackOverrideSource.CROPPED_FILMBACK_SETTING"></a>

#### CROPPED_FILMBACK_SETTING

1: Override the camera's filmback using the CroppedFilmback setting below

<a id="unreal.FilmbackOverrideSource.DO_NOT_OVERRIDE"></a>

#### DO_NOT_OVERRIDE

2: Do not override the camera's filmback

<a id="unreal.DistortionSource"></a>