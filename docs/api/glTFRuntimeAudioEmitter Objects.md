## glTFRuntimeAudioEmitter Objects

```python
class glTFRuntimeAudioEmitter(StructBase)
```

Gl TFRuntime Audio Emitter

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write]
- ``sound`` (SoundBase):  [Read-Write]
- ``volume`` (float):  [Read-Write]

<a id="unreal.glTFRuntimeAudioEmitter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str = "",
             volume: float = 0.000000,
             sound: SoundBase = None) -> None
```

<a id="unreal.glTFRuntimeAudioEmitter.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.glTFRuntimeAudioEmitter.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.glTFRuntimeAudioEmitter.volume"></a>

#### volume

```python
@property
def volume() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeAudioEmitter.volume"></a>

#### volume

```python
@volume.setter
def volume(value: float) -> None
```

<a id="unreal.glTFRuntimeAudioEmitter.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Write]

<a id="unreal.glTFRuntimeAudioEmitter.sound"></a>

#### sound

```python
@sound.setter
def sound(value: SoundBase) -> None
```

<a id="unreal.glTFRuntimeAudioConfig"></a>