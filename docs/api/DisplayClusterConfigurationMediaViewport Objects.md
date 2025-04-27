## DisplayClusterConfigurationMediaViewport Objects

```python
class DisplayClusterConfigurationMediaViewport(StructBase)
```

* Media settings for viewports

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write] Enable/disable media
- ``media_input`` (DisplayClusterConfigurationMediaInput):  [Read-Write] Media source to use
- ``media_output`` (MediaOutput):  [Read-Write]
  deprecated: This property has been deprecated. Please refer new MediaOutputs property.
- ``media_outputs`` (Array[DisplayClusterConfigurationMediaOutput]):  [Read-Write] Media outputs to use
- ``media_sharing_node`` (str):  [Read-Write]
  deprecated: This property has been deprecated
- ``media_source`` (MediaSource):  [Read-Write]
  deprecated: This property has been deprecated. Please refer new MediaInput property.
- ``output_sync_policy`` (DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write]
  deprecated: This property has been deprecated.

<a id="unreal.DisplayClusterConfigurationMediaViewport.__init__"></a>

#### __init__

```python
def __init__(
        enable: bool = False,
        media_input: DisplayClusterConfigurationMediaInput = [None],
        media_outputs: Array[DisplayClusterConfigurationMediaOutput] = []
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable/disable media

<a id="unreal.DisplayClusterConfigurationMediaViewport.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_input"></a>

#### media_input

```python
@property
def media_input() -> DisplayClusterConfigurationMediaInput
```

(DisplayClusterConfigurationMediaInput):  [Read-Write] Media source to use

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_input"></a>

#### media_input

```python
@media_input.setter
def media_input(value: DisplayClusterConfigurationMediaInput) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_outputs"></a>

#### media_outputs

```python
@property
def media_outputs() -> Array[DisplayClusterConfigurationMediaOutput]
```

(Array[DisplayClusterConfigurationMediaOutput]):  [Read-Write] Media outputs to use

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_outputs"></a>

#### media_outputs

```python
@media_outputs.setter
def media_outputs(
        value: Array[DisplayClusterConfigurationMediaOutput]) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_sharing_node"></a>

#### media_sharing_node

```python
@property
def media_sharing_node() -> str
```

(str):  [Read-Write]
deprecated: This property has been deprecated

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_sharing_node"></a>

#### media_sharing_node

```python
@media_sharing_node.setter
def media_sharing_node(value: str) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_source"></a>

#### media_source

```python
@property
def media_source() -> MediaSource
```

(MediaSource):  [Read-Write]
deprecated: This property has been deprecated. Please refer new MediaInput property.

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_source"></a>

#### media_source

```python
@media_source.setter
def media_source(value: MediaSource) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_output"></a>

#### media_output

```python
@property
def media_output() -> MediaOutput
```

(MediaOutput):  [Read-Write]
deprecated: This property has been deprecated. Please refer new MediaOutputs property.

<a id="unreal.DisplayClusterConfigurationMediaViewport.media_output"></a>

#### media_output

```python
@media_output.setter
def media_output(value: MediaOutput) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport.output_sync_policy"></a>

#### output_sync_policy

```python
@property
def output_sync_policy() -> DisplayClusterMediaOutputSynchronizationPolicy
```

(DisplayClusterMediaOutputSynchronizationPolicy):  [Read-Write]
deprecated: This property has been deprecated.

<a id="unreal.DisplayClusterConfigurationMediaViewport.output_sync_policy"></a>

#### output_sync_policy

```python
@output_sync_policy.setter
def output_sync_policy(
        value: DisplayClusterMediaOutputSynchronizationPolicy) -> None
```

<a id="unreal.DisplayClusterConfigurationMedia"></a>