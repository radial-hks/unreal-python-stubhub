## DisplayClusterConfigurationMediaNodeBackbuffer Objects

```python
class DisplayClusterConfigurationMediaNodeBackbuffer(StructBase)
```

* Media settings for node backbuffer

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Media.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write] Enable/disable media
- ``media_outputs`` (Array[DisplayClusterConfigurationMediaOutput]):  [Read-Write] Media outputs to use

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer.__init__"></a>

#### __init__

```python
def __init__(
        enable: bool = False,
        media_outputs: Array[DisplayClusterConfigurationMediaOutput] = []
) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enable/disable media

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer.media_outputs"></a>

#### media_outputs

```python
@property
def media_outputs() -> Array[DisplayClusterConfigurationMediaOutput]
```

(Array[DisplayClusterConfigurationMediaOutput]):  [Read-Write] Media outputs to use

<a id="unreal.DisplayClusterConfigurationMediaNodeBackbuffer.media_outputs"></a>

#### media_outputs

```python
@media_outputs.setter
def media_outputs(
        value: Array[DisplayClusterConfigurationMediaOutput]) -> None
```

<a id="unreal.DisplayClusterConfigurationMediaViewport"></a>