## TakeRecorderMicrophoneAudioSource Objects

```python
class TakeRecorderMicrophoneAudioSource(
        TakeRecorderMicrophoneAudioSourceSettings)
```

A recording source that records microphone audio

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderMicrophoneAudioSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_asset_name`` (str):  [Read-Write] The name of the audio asset.
  Supports any of the following format specifiers that will be substituted when a take is recorded :
  {day} - The day of the timestamp for the start of the recording.
  {month} - The month of the timestamp for the start of the recording.
  {year} - The year of the timestamp for the start of the recording.
  {hour} - The hour of the timestamp for the start of the recording.
  {minute} - The minute of the timestamp for the start of the recording.
  {second} - The second of the timestamp for the start of the recording.
  {take} - The take number.
  {slate} - The slate string.
- ``audio_channel`` (AudioInputDeviceChannelProperty):  [Read-Write] The audio device to use for this microphone source
- ``audio_gain`` (float):  [Read-Write] Gain in decibels to apply to recorded audio
- ``audio_source_name`` (Text):  [Read-Write] Name of the audio source
- ``audio_sub_directory`` (str):  [Read-Write] The name of the subdirectory audio will be placed in. Leave this empty to place into the same directory as the sequence base path
  Supports any of the following format specifiers that will be substituted when a take is recorded :
  {day} - The day of the timestamp for the start of the recording.
  {month} - The month of the timestamp for the start of the recording.
  {year} - The year of the timestamp for the start of the recording.
  {hour} - The hour of the timestamp for the start of the recording.
  {minute} - The minute of the timestamp for the start of the recording.
  {second} - The second of the timestamp for the start of the recording.
  {take} - The take number.
  {slate} - The slate string.
- ``audio_track_name`` (Text):  [Read-Write] Name of the recorded audio track
- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``replace_recorded_audio`` (bool):  [Read-Write] Replace existing recorded audio with any newly recorded audio
- ``split_audio_channels_into_separate_tracks`` (bool):  [Read-Write]
  deprecated: SplitAudioChannelsIntoSeparateTracks is deprecated.
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderMicrophoneAudioSource.audio_gain"></a>

#### audio_gain

```python
@property
def audio_gain() -> float
```

(float):  [Read-Write] Gain in decibels to apply to recorded audio

<a id="unreal.TakeRecorderMicrophoneAudioSource.audio_gain"></a>

#### audio_gain

```python
@audio_gain.setter
def audio_gain(value: float) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSource.split_audio_channels_into_separate_tracks"></a>

#### split_audio_channels_into_separate_tracks

```python
@property
def split_audio_channels_into_separate_tracks() -> bool
```

(bool):  [Read-Write]
deprecated: SplitAudioChannelsIntoSeparateTracks is deprecated.

<a id="unreal.TakeRecorderMicrophoneAudioSource.split_audio_channels_into_separate_tracks"></a>

#### split_audio_channels_into_separate_tracks

```python
@split_audio_channels_into_separate_tracks.setter
def split_audio_channels_into_separate_tracks(value: bool) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSource.replace_recorded_audio"></a>

#### replace_recorded_audio

```python
@property
def replace_recorded_audio() -> bool
```

(bool):  [Read-Write] Replace existing recorded audio with any newly recorded audio

<a id="unreal.TakeRecorderMicrophoneAudioSource.replace_recorded_audio"></a>

#### replace_recorded_audio

```python
@replace_recorded_audio.setter
def replace_recorded_audio(value: bool) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSource.audio_channel"></a>

#### audio_channel

```python
@property
def audio_channel() -> AudioInputDeviceChannelProperty
```

(AudioInputDeviceChannelProperty):  [Read-Write] The audio device to use for this microphone source

<a id="unreal.TakeRecorderMicrophoneAudioSource.audio_channel"></a>

#### audio_channel

```python
@audio_channel.setter
def audio_channel(value: AudioInputDeviceChannelProperty) -> None
```

<a id="unreal.TakeRecorderNearbySpawnedActorSource"></a>