## AudioLinkBlueprintInterface Objects

```python
class AudioLinkBlueprintInterface(Interface)
```

Audio Link Blueprint Interface

**C++ Source:**

- **Module**: AudioLinkEngine
- **File**: IAudioLinkBlueprintInterface.h

<a id="unreal.AudioLinkBlueprintInterface.stop_link"></a>

#### stop_link

```python
def stop_link() -> None
```

x.stop_link() -> None
Stop an audio component's sound, issue any delegates if needed

<a id="unreal.AudioLinkBlueprintInterface.set_link_sound"></a>

#### set_link_sound

```python
def set_link_sound(new_sound: SoundBase) -> None
```

x.set_link_sound(new_sound) -> None
Set Link Sound

Args:
    new_sound (SoundBase):

<a id="unreal.AudioLinkBlueprintInterface.play_link"></a>

#### play_link

```python
def play_link(start_time: float = 0.000000) -> None
```

x.play_link(start_time=0.000000) -> None
Play Link

Args:
    start_time (float):

<a id="unreal.AudioLinkBlueprintInterface.is_link_playing"></a>

#### is_link_playing

```python
def is_link_playing() -> bool
```

x.is_link_playing() -> bool
Is Link Playing

Returns:
    bool:

<a id="unreal.AudioDeviceNotificationSubsystem"></a>