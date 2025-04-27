## DisplayClusterConfigurationMediaOutput Objects

```python
class DisplayClusterConfigurationMediaOutput(StructBase)
```

* Media output item

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``media_output`` (MediaOutput):  [Read-Write] Media output to use
- ``output_sync_policy`` (DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write] Media output synchronization policy

<a id="unreal.DisplayClusterConfigurationMediaOutput.__init__"></a>

#### __init__

```python
def __init__(
    media_output: MediaOutput = None,
    output_sync_policy: DisplayClusterMediaOutputSynchronizationPolicy = None
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaOutput.media_output"></a>

#### media_output

```python
@property
def media_output() -> MediaOutput
```

(MediaOutput):  [Read-Write] Media output to use

<a id="unreal.DisplayClusterConfigurationMediaOutput.media_output"></a>

#### media_output

```python
@media_output.setter
def media_output(value: MediaOutput) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaOutput.output_sync_policy"></a>

#### output_sync_policy

```python
@property
def output_sync_policy() -> DisplayClusterMediaOutputSynchronizationPolicy
```

(DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write] Media output synchronization policy

<a id="unreal.DisplayClusterConfigurationMediaOutput.output_sync_policy"></a>

#### output_sync_policy

```python
@output_sync_policy.setter
def output_sync_policy(
        value: DisplayClusterMediaOutputSynchronizationPolicy) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaOutputGroup"></a>