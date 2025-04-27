## MoviePipelineColorSetting Objects

```python
class MoviePipelineColorSetting(MoviePipelineSetting)
```

Movie Pipeline Color Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineColorSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disable_tone_curve`` (bool):  [Read-Write] If true the Filmic Tone Curve will not be applied. Disabling this will allow you to export linear data for EXRs. Force Disabled if Open Color IO is enabled.
- ``ocio_configuration`` (OpenColorIODisplayConfiguration):  [Read-Write] OCIO config to be passed to OCIO View Extension. If this is enabled the Tone Curve will be disabled.

<a id="unreal.MoviePipelineColorSetting.ocio_configuration"></a>

#### ocio_configuration

```python
@property
def ocio_configuration() -> OpenColorIODisplayConfiguration
```

(OpenColorIODisplayConfiguration):  [Read-Write] OCIO config to be passed to OCIO View Extension. If this is enabled the Tone Curve will be disabled.

<a id="unreal.MoviePipelineColorSetting.ocio_configuration"></a>

#### ocio_configuration

```python
@ocio_configuration.setter
def ocio_configuration(value: OpenColorIODisplayConfiguration) -> None
```

<a id="unreal.MoviePipelineColorSetting.disable_tone_curve"></a>

#### disable_tone_curve

```python
@property
def disable_tone_curve() -> bool
```

(bool):  [Read-Write] If true the Filmic Tone Curve will not be applied. Disabling this will allow you to export linear data for EXRs. Force Disabled if Open Color IO is enabled.

<a id="unreal.MoviePipelineColorSetting.disable_tone_curve"></a>

#### disable_tone_curve

```python
@disable_tone_curve.setter
def disable_tone_curve(value: bool) -> None
```

<a id="unreal.MoviePipelineCommandLineEncoder"></a>