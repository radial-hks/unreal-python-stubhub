## ComposureLensBloomPassPolicy Objects

```python
class ComposureLensBloomPassPolicy(ComposurePostProcessPassPolicy)
```

Bloom only rules used for configuring how UComposurePostProcessingPassProxy executes

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposureLensBloomPass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bloom_intensity_param_name`` (Name):  [Read-Write]
- ``replacement_material`` (MaterialInterface):  [Read-Write]
- ``settings`` (LensBloomSettings):  [Read-Write] Bloom settings.

<a id="unreal.ComposureLensBloomPassPolicy.settings"></a>

#### settings

```python
@property
def settings() -> LensBloomSettings
```

(LensBloomSettings):  [Read-Write] Bloom settings.

<a id="unreal.ComposureLensBloomPassPolicy.settings"></a>

#### settings

```python
@settings.setter
def settings(value: LensBloomSettings) -> None
```

<a id="unreal.ComposurePlayerCompositingCameraModifier"></a>