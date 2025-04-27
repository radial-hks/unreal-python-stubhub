## AudioDeviceNotificationSubsystem Objects

```python
class AudioDeviceNotificationSubsystem(EngineSubsystem)
```

UAudioDeviceNotificationSubsystem

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioDeviceNotificationSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_capture_device_changed`` (OnAudioDefaultDeviceChanged):  [Read-Write] Multicast delegate triggered when default capture device changes
- ``default_render_device_changed`` (OnAudioDefaultDeviceChanged):  [Read-Write] Multicast delegate triggered when default render device changes
- ``device_added`` (OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered when a device is added
- ``device_removed`` (OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered when a device is removed
- ``device_state_changed`` (OnAudioDeviceStateChanged):  [Read-Write] Multicast delegate triggered on device state change
- ``device_switched`` (OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered on device switch

<a id="unreal.AudioDeviceNotificationSubsystem.default_capture_device_changed"></a>

#### default_capture_device_changed

```python
@property
def default_capture_device_changed() -> OnAudioDefaultDeviceChanged
```

(OnAudioDefaultDeviceChanged):  [Read-Write] Multicast delegate triggered when default capture device changes

<a id="unreal.AudioDeviceNotificationSubsystem.default_capture_device_changed"></a>

#### default_capture_device_changed

```python
@default_capture_device_changed.setter
def default_capture_device_changed(value: OnAudioDefaultDeviceChanged) -> None
```

<a id="unreal.AudioDeviceNotificationSubsystem.default_render_device_changed"></a>

#### default_render_device_changed

```python
@property
def default_render_device_changed() -> OnAudioDefaultDeviceChanged
```

(OnAudioDefaultDeviceChanged):  [Read-Write] Multicast delegate triggered when default render device changes

<a id="unreal.AudioDeviceNotificationSubsystem.default_render_device_changed"></a>

#### default_render_device_changed

```python
@default_render_device_changed.setter
def default_render_device_changed(value: OnAudioDefaultDeviceChanged) -> None
```

<a id="unreal.AudioDeviceNotificationSubsystem.device_added"></a>

#### device_added

```python
@property
def device_added() -> OnAudioDeviceChange
```

(OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered when a device is added

<a id="unreal.AudioDeviceNotificationSubsystem.device_added"></a>

#### device_added

```python
@device_added.setter
def device_added(value: OnAudioDeviceChange) -> None
```

<a id="unreal.AudioDeviceNotificationSubsystem.device_removed"></a>

#### device_removed

```python
@property
def device_removed() -> OnAudioDeviceChange
```

(OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered when a device is removed

<a id="unreal.AudioDeviceNotificationSubsystem.device_removed"></a>

#### device_removed

```python
@device_removed.setter
def device_removed(value: OnAudioDeviceChange) -> None
```

<a id="unreal.AudioDeviceNotificationSubsystem.device_state_changed"></a>

#### device_state_changed

```python
@property
def device_state_changed() -> OnAudioDeviceStateChanged
```

(OnAudioDeviceStateChanged):  [Read-Write] Multicast delegate triggered on device state change

<a id="unreal.AudioDeviceNotificationSubsystem.device_state_changed"></a>

#### device_state_changed

```python
@device_state_changed.setter
def device_state_changed(value: OnAudioDeviceStateChanged) -> None
```

<a id="unreal.AudioDeviceNotificationSubsystem.device_switched"></a>

#### device_switched

```python
@property
def device_switched() -> OnAudioDeviceChange
```

(OnAudioDeviceChange):  [Read-Write] Multicast delegate triggered on device switch

<a id="unreal.AudioDeviceNotificationSubsystem.device_switched"></a>

#### device_switched

```python
@device_switched.setter
def device_switched(value: OnAudioDeviceChange) -> None
```

<a id="unreal.AudioMixerLibrary"></a>