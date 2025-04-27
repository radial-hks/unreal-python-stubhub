## DisplayClusterConfigurationViewport_CustomPostprocessSettings Objects

```python
class DisplayClusterConfigurationViewport_CustomPostprocessSettings(
        StructBase)
```

Display Cluster Configuration Viewport Custom Postprocess Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Override blend weight
- ``is_enabled`` (bool):  [Read-Write] Enable custom postprocess
- ``is_one_frame`` (bool):  [Read-Write] Apply postprocess for one frame
- ``post_process_settings`` (PostProcessSettings):  [Read-Write] Custom postprocess settings

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.__init__"></a>

#### __init__

```python
def __init__(is_enabled: bool = False,
             is_one_frame: bool = False,
             post_process_settings: PostProcessSettings = [],
             blend_weight: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Write] Enable custom postprocess

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.is_enabled"></a>

#### is_enabled

```python
@is_enabled.setter
def is_enabled(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.is_one_frame"></a>

#### is_one_frame

```python
@property
def is_one_frame() -> bool
```

(bool):  [Read-Write] Apply postprocess for one frame

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.is_one_frame"></a>

#### is_one_frame

```python
@is_one_frame.setter
def is_one_frame(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.post_process_settings"></a>

#### post_process_settings

```python
@property
def post_process_settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write] Custom postprocess settings

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.post_process_settings"></a>

#### post_process_settings

```python
@post_process_settings.setter
def post_process_settings(value: PostProcessSettings) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] Override blend weight

<a id="unreal.DisplayClusterConfigurationViewport_CustomPostprocessSettings.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_CameraMotionBlurOverridePPS"></a>