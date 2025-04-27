## AvaSequencePlayParams Objects

```python
class AvaSequencePlayParams(StructBase)
```

Ava Sequence Play Params

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequenceShared.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_settings`` (AvaSequencePlayAdvancedSettings):  [Read-Write]
- ``end`` (AvaSequenceTime):  [Read-Write]
- ``play_mode`` (AvaSequencePlayMode):  [Read-Write]
- ``start`` (AvaSequenceTime):  [Read-Write]

<a id="unreal.AvaSequencePlayParams.__init__"></a>

#### __init__

```python
def __init__(
    start: AvaSequenceTime = [
        AvaSequenceTimeType.FRAME, 0, 0.000000, 0.000000, "", False
    ],
    end: AvaSequenceTime = [
        AvaSequenceTimeType.FRAME, 0, 0.000000, 0.000000, "", False
    ],
    play_mode: AvaSequencePlayMode = AvaSequencePlayMode.FORWARD,
    advanced_settings: AvaSequencePlayAdvancedSettings = [0, 1.000000, False]
) -> None
```

<a id="unreal.AvaSequencePlayParams.start"></a>

#### start

```python
@property
def start() -> AvaSequenceTime
```

(AvaSequenceTime):  [Read-Write]

<a id="unreal.AvaSequencePlayParams.start"></a>

#### start

```python
@start.setter
def start(value: AvaSequenceTime) -> None
```

<a id="unreal.AvaSequencePlayParams.end"></a>

#### end

```python
@property
def end() -> AvaSequenceTime
```

(AvaSequenceTime):  [Read-Write]

<a id="unreal.AvaSequencePlayParams.end"></a>

#### end

```python
@end.setter
def end(value: AvaSequenceTime) -> None
```

<a id="unreal.AvaSequencePlayParams.play_mode"></a>

#### play_mode

```python
@property
def play_mode() -> AvaSequencePlayMode
```

(AvaSequencePlayMode):  [Read-Write]

<a id="unreal.AvaSequencePlayParams.play_mode"></a>

#### play_mode

```python
@play_mode.setter
def play_mode(value: AvaSequencePlayMode) -> None
```

<a id="unreal.AvaSequencePlayParams.advanced_settings"></a>

#### advanced_settings

```python
@property
def advanced_settings() -> AvaSequencePlayAdvancedSettings
```

(AvaSequencePlayAdvancedSettings):  [Read-Write]

<a id="unreal.AvaSequencePlayParams.advanced_settings"></a>

#### advanced_settings

```python
@advanced_settings.setter
def advanced_settings(value: AvaSequencePlayAdvancedSettings) -> None
```

<a id="unreal.AvaAnimPlayParams"></a>