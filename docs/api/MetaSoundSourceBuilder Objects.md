## MetaSoundSourceBuilder Objects

```python
class MetaSoundSourceBuilder(MetaSoundBuilderBase)
```

Builder in charge of building a MetaSound Source

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundBuilderSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_name`` (MetasoundFrontendClassName):  [Read-Write]
  deprecated: 5.5 - No longer used. ClassName should be queried from associated FrontendBuilder's MetaSound
- ``is_attached`` (bool):  [Read-Write]
  deprecated: 5.4 - All source builders now operate on an underlying document source document that is also used to audition.

<a id="unreal.MetaSoundSourceBuilder.set_sample_rate_override"></a>

#### set_sample_rate_override

```python
def set_sample_rate_override(sample_rate: int) -> None
```

x.set_sample_rate_override(sample_rate) -> None
Sets the MetaSound's SampleRate override

Args:
    sample_rate (int32):

<a id="unreal.MetaSoundSourceBuilder.set_quality"></a>

#### set_quality

```python
def set_quality(quality: Name) -> None
```

x.set_quality(quality) -> None
Sets the MetaSound's Quality level

Args:
    quality (Name):

<a id="unreal.MetaSoundSourceBuilder.set_format"></a>

#### set_format

```python
def set_format(
        output_format: MetaSoundOutputAudioFormat) -> MetaSoundBuilderResult
```

x.set_format(output_format) -> MetaSoundBuilderResult
Sets the output audio format of the source

Args:
    output_format (MetaSoundOutputAudioFormat): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundSourceBuilder.set_block_rate_override"></a>

#### set_block_rate_override

```python
def set_block_rate_override(block_rate: float) -> None
```

x.set_block_rate_override(block_rate) -> None
Sets the MetaSound's BlockRate override

Args:
    block_rate (float):

<a id="unreal.MetaSoundSourceBuilder.get_live_updates_enabled"></a>

#### get_live_updates_enabled

```python
def get_live_updates_enabled() -> bool
```

x.get_live_updates_enabled() -> bool
Returns whether or not live updates are both globally enabled (via cvar) and are enabled on this builder's last built sound, which may or may not still be playing.

Returns:
    bool:

<a id="unreal.MetaSoundSourceBuilder.audition"></a>

#### audition

```python
def audition(parent: Object,
             audio_component: AudioComponent,
             on_create_generator: OnCreateAuditionGeneratorHandleDelegate,
             live_updates_enabled: bool = False) -> None
```

x.audition(parent, audio_component, on_create_generator, live_updates_enabled=False) -> None
Audition

Args:
    parent (Object): 
    audio_component (AudioComponent): 
    on_create_generator (OnCreateAuditionGeneratorHandleDelegate): 
    live_updates_enabled (bool):

<a id="unreal.MetaSoundBuilderSubsystem"></a>