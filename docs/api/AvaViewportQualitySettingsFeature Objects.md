## AvaViewportQualitySettingsFeature Objects

```python
class AvaViewportQualitySettingsFeature(StructBase)
```

Ava Viewport Quality Settings Feature

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaViewportQualitySettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] True if this engine feature show flag should be enabled.
- ``name`` (str):  [Read-Write] The name of the feature in the engine show flags.

<a id="unreal.AvaViewportQualitySettingsFeature.__init__"></a>

#### __init__

```python
def __init__(name: str = "", enabled: bool = False) -> None
```

<a id="unreal.AvaViewportQualitySettingsFeature.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] The name of the feature in the engine show flags.

<a id="unreal.AvaViewportQualitySettingsFeature.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.AvaViewportQualitySettingsFeature.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] True if this engine feature show flag should be enabled.

<a id="unreal.AvaViewportQualitySettingsFeature.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.AvaViewportQualitySettings"></a>