## TargetChainSettings Objects

```python
class TargetChainSettings(StructBase)
```

Target Chain Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fk`` (TargetChainFKSettings):  [Read-Write] All settings for FK retargeting of this chain.
  FK retargeting runs before the IK pass.
- ``ik`` (TargetChainIKSettings):  [Read-Write] All settings controlling the IK Goal assigned to this chain.
  The IK pass runs AFTER the FK pass and can be used to fix contacts.
- ``speed_planting`` (TargetChainSpeedPlantSettings):  [Read-Write] All settings associated with planting IK goals based on the speed of the source.
  Speed planting will pin the IK goal to the location determined by the IK settings above.

<a id="unreal.TargetChainSettings.__init__"></a>

#### __init__

```python
def __init__(
    fk: TargetChainFKSettings = [
        True, RetargetRotationMode.INTERPOLATED, 1.000000,
        RetargetTranslationMode.NONE, 1.000000, 0.000000, False, 0.000000
    ],
    ik: TargetChainIKSettings = [
        True, 0.000000, [1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], 1.000000, 1.000000, True
    ],
    speed_planting: TargetChainSpeedPlantSettings = [
        False, "None", 15.000000, 250.000000, 1.000000
    ]
) -> None
```

<a id="unreal.TargetChainSettings.fk"></a>

#### fk

```python
@property
def fk() -> TargetChainFKSettings
```

(TargetChainFKSettings):  [Read-Write] All settings for FK retargeting of this chain.
FK retargeting runs before the IK pass.

<a id="unreal.TargetChainSettings.fk"></a>

#### fk

```python
@fk.setter
def fk(value: TargetChainFKSettings) -> None
```

<a id="unreal.TargetChainSettings.ik"></a>

#### ik

```python
@property
def ik() -> TargetChainIKSettings
```

(TargetChainIKSettings):  [Read-Write] All settings controlling the IK Goal assigned to this chain.
The IK pass runs AFTER the FK pass and can be used to fix contacts.

<a id="unreal.TargetChainSettings.ik"></a>

#### ik

```python
@ik.setter
def ik(value: TargetChainIKSettings) -> None
```

<a id="unreal.TargetChainSettings.speed_planting"></a>

#### speed_planting

```python
@property
def speed_planting() -> TargetChainSpeedPlantSettings
```

(TargetChainSpeedPlantSettings):  [Read-Write] All settings associated with planting IK goals based on the speed of the source.
Speed planting will pin the IK goal to the location determined by the IK settings above.

<a id="unreal.TargetChainSettings.speed_planting"></a>

#### speed_planting

```python
@speed_planting.setter
def speed_planting(value: TargetChainSpeedPlantSettings) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings"></a>