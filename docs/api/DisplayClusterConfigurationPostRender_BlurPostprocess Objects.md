## DisplayClusterConfigurationPostRender_BlurPostprocess Objects

```python
class DisplayClusterConfigurationPostRender_BlurPostprocess(StructBase)
```

Display Cluster Configuration Post Render Blur Postprocess

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_PostRender.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``kernel_radius`` (int32):  [Read-Write] Kernel Radius
- ``kernel_scale`` (float):  [Read-Write] Kernel Scale
- ``mode`` (DisplayClusterConfiguration_PostRenderBlur):  [Read-Write] Enable/disable Post Process Blur and specify method.

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.__init__"></a>

#### __init__

```python
def __init__(
        mode:
    DisplayClusterConfiguration_PostRenderBlur = DisplayClusterConfiguration_PostRenderBlur
    .NONE,
        kernel_radius: int = 0,
        kernel_scale: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.mode"></a>

#### mode

```python
@property
def mode() -> DisplayClusterConfiguration_PostRenderBlur
```

(DisplayClusterConfiguration_PostRenderBlur):  [Read-Write] Enable/disable Post Process Blur and specify method.

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DisplayClusterConfiguration_PostRenderBlur) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.kernel_radius"></a>

#### kernel_radius

```python
@property
def kernel_radius() -> int
```

(int32):  [Read-Write] Kernel Radius

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.kernel_radius"></a>

#### kernel_radius

```python
@kernel_radius.setter
def kernel_radius(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.kernel_scale"></a>

#### kernel_scale

```python
@property
def kernel_scale() -> float
```

(float):  [Read-Write] Kernel Scale

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess.kernel_scale"></a>

#### kernel_scale

```python
@kernel_scale.setter
def kernel_scale(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_Override"></a>