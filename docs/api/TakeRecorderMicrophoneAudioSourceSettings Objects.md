## TakeRecorderMicrophoneAudioSourceSettings Objects

```python
class TakeRecorderMicrophoneAudioSourceSettings(TakeRecorderSource)
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
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_source_name"></a>

#### audio_source_name

```python
@property
def audio_source_name() -> Text
```

(Text):  [Read-Write] Name of the audio source

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_source_name"></a>

#### audio_source_name

```python
@audio_source_name.setter
def audio_source_name(value: Text) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_track_name"></a>

#### audio_track_name

```python
@property
def audio_track_name() -> Text
```

(Text):  [Read-Write] Name of the recorded audio track

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_track_name"></a>

#### audio_track_name

```python
@audio_track_name.setter
def audio_track_name(value: Text) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_asset_name"></a>

#### audio_asset_name

```python
@property
def audio_asset_name() -> str
```

(str):  [Read-Write] The name of the audio asset.
Supports any of the following format specifiers that will be substituted when a take is recorded :
{day} - The day of the timestamp for the start of the recording.
{month} - The month of the timestamp for the start of the recording.
{year} - The year of the timestamp for the start of the recording.
{hour} - The hour of the timestamp for the start of the recording.
{minute} - The minute of the timestamp for the start of the recording.
{second} - The second of the timestamp for the start of the recording.
{take} - The take number.
{slate} - The slate string.

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_asset_name"></a>

#### audio_asset_name

```python
@audio_asset_name.setter
def audio_asset_name(value: str) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_sub_directory"></a>

#### audio_sub_directory

```python
@property
def audio_sub_directory() -> str
```

(str):  [Read-Write] The name of the subdirectory audio will be placed in. Leave this empty to place into the same directory as the sequence base path
Supports any of the following format specifiers that will be substituted when a take is recorded :
{day} - The day of the timestamp for the start of the recording.
{month} - The month of the timestamp for the start of the recording.
{year} - The year of the timestamp for the start of the recording.
{hour} - The hour of the timestamp for the start of the recording.
{minute} - The minute of the timestamp for the start of the recording.
{second} - The second of the timestamp for the start of the recording.
{take} - The take number.
{slate} - The slate string.

<a id="unreal.TakeRecorderMicrophoneAudioSourceSettings.audio_sub_directory"></a>

#### audio_sub_directory

```python
@audio_sub_directory.setter
def audio_sub_directory(value: str) -> None
```

<a id="unreal.TakeRecorderMicrophoneAudioSource"></a>