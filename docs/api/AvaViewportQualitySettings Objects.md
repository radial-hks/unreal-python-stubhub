## AvaViewportQualitySettings Objects

```python
class AvaViewportQualitySettings(StructBase)
```

Motion Design Viewport Quality Settings

Advanced render and quality viewport settings to control performance for a given Viewport.
Human-readable and blueprint-able structure that holds flags for the FShowEngineFlags structure.
Can convert FShowEngineFlags to FAvaViewportQualitySettings and apply FAvaViewportQualitySettings to a FShowEngineFlags structure.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaViewportQualitySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``features`` (Array[AvaViewportQualitySettingsFeature]):  [Read-Write] Advanced viewport client engine features indexed by FEngineShowFlags names.

<a id="unreal.AvaViewportQualitySettings.__init__"></a>

#### __init__

```python
def __init__(features: Array[AvaViewportQualitySettingsFeature] = []) -> None
```

<a id="unreal.AvaViewportQualitySettings.features"></a>

#### features

```python
@property
def features() -> Array[AvaViewportQualitySettingsFeature]
```

(Array[AvaViewportQualitySettingsFeature]):  [Read-Write] Advanced viewport client engine features indexed by FEngineShowFlags names.

<a id="unreal.AvaViewportQualitySettings.features"></a>

#### features

```python
@features.setter
def features(value: Array[AvaViewportQualitySettingsFeature]) -> None
```

<a id="unreal.OpenColorIOColorSpace"></a>