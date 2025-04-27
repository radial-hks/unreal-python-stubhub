## TakeRecorderMicrophoneAudioManager Objects

```python
class TakeRecorderMicrophoneAudioManager(TakeRecorderAudioInputSettings)
```

This class exposes the audio input device list via the project settings details. It does this in
 conjunction with FAudioInputDevicePropertyCustomization. It also manages the IAudioCaptureEditor
 object which handles the low level audio device recording.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderMicrophoneAudioManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_input_device`` (AudioInputDeviceProperty):  [Read-Write] The audio device to use for this microphone source

<a id="unreal.TakeRecorderMicrophoneAudioManager.audio_input_device"></a>

#### audio_input_device

```python
@property
def audio_input_device() -> AudioInputDeviceProperty
```

(AudioInputDeviceProperty):  [Read-Write] The audio device to use for this microphone source

<a id="unreal.TakeRecorderMicrophoneAudioManager.audio_input_device"></a>

#### audio_input_device

```python
@audio_input_device.setter
def audio_input_device(value: AudioInputDeviceProperty) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings"></a>