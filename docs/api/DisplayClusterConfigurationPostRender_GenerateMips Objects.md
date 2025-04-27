## DisplayClusterConfigurationPostRender_GenerateMips Objects

```python
class DisplayClusterConfigurationPostRender_GenerateMips(StructBase)
```

Display Cluster Configuration Post Render Generate Mips

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_PostRender.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_generate_mips`` (bool):  [Read-Write] Generate and use mipmaps for the inner frustum.  Disabling this can improve performance but result in visual artifacts on the inner frustum.
- ``enabled_max_num_mips`` (bool):  [Read-Write] Performance: Allows a limited number of MIPs for high resolution.
- ``max_num_mips`` (int32):  [Read-Write] Performance: Use this value as the maximum number of MIPs for high resolution.
- ``mips_address_u`` (TextureAddress):  [Read-Write] AutoGenerateMips sampler address mode for U channel. Defaults to clamp.
- ``mips_address_v`` (TextureAddress):  [Read-Write] AutoGenerateMips sampler address mode for V channel. Defaults to clamp.
- ``mips_sampler_filter`` (TextureFilter):  [Read-Write] Mips Sampler Filter

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.__init__"></a>

#### __init__

```python
def __init__(auto_generate_mips: bool = False,
             mips_sampler_filter: TextureFilter = TextureFilter.TF_NEAREST,
             mips_address_u: TextureAddress = TextureAddress.TA_WRAP,
             mips_address_v: TextureAddress = TextureAddress.TA_WRAP,
             enabled_max_num_mips: bool = False,
             max_num_mips: int = 0) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.auto_generate_mips"></a>

#### auto_generate_mips

```python
@property
def auto_generate_mips() -> bool
```

(bool):  [Read-Write] Generate and use mipmaps for the inner frustum.  Disabling this can improve performance but result in visual artifacts on the inner frustum.

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.auto_generate_mips"></a>

#### auto_generate_mips

```python
@auto_generate_mips.setter
def auto_generate_mips(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_sampler_filter"></a>

#### mips_sampler_filter

```python
@property
def mips_sampler_filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] Mips Sampler Filter

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_sampler_filter"></a>

#### mips_sampler_filter

```python
@mips_sampler_filter.setter
def mips_sampler_filter(value: TextureFilter) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_address_u"></a>

#### mips_address_u

```python
@property
def mips_address_u() -> TextureAddress
```

(TextureAddress):  [Read-Write] AutoGenerateMips sampler address mode for U channel. Defaults to clamp.

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_address_u"></a>

#### mips_address_u

```python
@mips_address_u.setter
def mips_address_u(value: TextureAddress) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_address_v"></a>

#### mips_address_v

```python
@property
def mips_address_v() -> TextureAddress
```

(TextureAddress):  [Read-Write] AutoGenerateMips sampler address mode for V channel. Defaults to clamp.

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.mips_address_v"></a>

#### mips_address_v

```python
@mips_address_v.setter
def mips_address_v(value: TextureAddress) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.enabled_max_num_mips"></a>

#### enabled_max_num_mips

```python
@property
def enabled_max_num_mips() -> bool
```

(bool):  [Read-Write] Performance: Allows a limited number of MIPs for high resolution.

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.enabled_max_num_mips"></a>

#### enabled_max_num_mips

```python
@enabled_max_num_mips.setter
def enabled_max_num_mips(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.max_num_mips"></a>

#### max_num_mips

```python
@property
def max_num_mips() -> int
```

(int32):  [Read-Write] Performance: Use this value as the maximum number of MIPs for high resolution.

<a id="unreal.DisplayClusterConfigurationPostRender_GenerateMips.max_num_mips"></a>

#### max_num_mips

```python
@max_num_mips.setter
def max_num_mips(value: int) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_BlurPostprocess"></a>