## MontageBlendSettings Objects

```python
class MontageBlendSettings(StructBase)
```

Montage blend settings. Can be used to overwrite default Montage settings on Play/Stop

**C++ Source:**

- **Module**: Engine
- **File**: AnimMontage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend`` (AlphaBlendArgs):  [Read-Write] AlphaBlend options (time, curve, etc.)
- ``blend_mode`` (MontageBlendMode):  [Read-Write] Type of blend mode (Standard vs Inertial)
- ``blend_profile`` (BlendProfile):  [Read-Write] Blend Profile to use for this blend

<a id="unreal.MontageBlendSettings.__init__"></a>

#### __init__

```python
def __init__(blend_profile: BlendProfile = None,
             blend: AlphaBlendArgs = [None, 0.200000, AlphaBlendOption.LINEAR],
             blend_mode: MontageBlendMode = MontageBlendMode.STANDARD) -> None
```

<a id="unreal.MontageBlendSettings.blend_profile"></a>

#### blend_profile

```python
@property
def blend_profile() -> BlendProfile
```

(BlendProfile):  [Read-Write] Blend Profile to use for this blend

<a id="unreal.MontageBlendSettings.blend_profile"></a>

#### blend_profile

```python
@blend_profile.setter
def blend_profile(value: BlendProfile) -> None
```

<a id="unreal.MontageBlendSettings.blend"></a>

#### blend

```python
@property
def blend() -> AlphaBlendArgs
```

(AlphaBlendArgs):  [Read-Write] AlphaBlend options (time, curve, etc.)

<a id="unreal.MontageBlendSettings.blend"></a>

#### blend

```python
@blend.setter
def blend(value: AlphaBlendArgs) -> None
```

<a id="unreal.MontageBlendSettings.blend_mode"></a>

#### blend_mode

```python
@property
def blend_mode() -> MontageBlendMode
```

(MontageBlendMode):  [Read-Write] Type of blend mode (Standard vs Inertial)

<a id="unreal.MontageBlendSettings.blend_mode"></a>

#### blend_mode

```python
@blend_mode.setter
def blend_mode(value: MontageBlendMode) -> None
```

<a id="unreal.AnimNodeData"></a>