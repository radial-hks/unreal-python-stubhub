## SourceEffectPannerSettings Objects

```python
class SourceEffectPannerSettings(StructBase)
```

Source Effect Panner Settings

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectPanner.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pan`` (float):  [Read-Write] The pan of the source. -1.0 means left, 0.0 means center, 1.0 means right.
- ``spread`` (float):  [Read-Write] The spread of the source. 1.0 means left only in left channel, right only in right; 0.0 means both mixed, -1.0 means right and left channels are inverted.

<a id="unreal.SourceEffectPannerSettings.__init__"></a>

#### __init__

```python
def __init__(spread: float = 0.000000, pan: float = 0.000000) -> None
```

<a id="unreal.SourceEffectPannerSettings.spread"></a>

#### spread

```python
@property
def spread() -> float
```

(float):  [Read-Write] The spread of the source. 1.0 means left only in left channel, right only in right; 0.0 means both mixed, -1.0 means right and left channels are inverted.

<a id="unreal.SourceEffectPannerSettings.spread"></a>

#### spread

```python
@spread.setter
def spread(value: float) -> None
```

<a id="unreal.SourceEffectPannerSettings.pan"></a>

#### pan

```python
@property
def pan() -> float
```

(float):  [Read-Write] The pan of the source. -1.0 means left, 0.0 means center, 1.0 means right.

<a id="unreal.SourceEffectPannerSettings.pan"></a>

#### pan

```python
@pan.setter
def pan(value: float) -> None
```

<a id="unreal.SourceEffectPhaserSettings"></a>