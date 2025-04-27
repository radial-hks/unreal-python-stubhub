## AnimatedBoneAttribute Objects

```python
class AnimatedBoneAttribute(StructBase)
```

Structure encapsulating animated (bone) attribute data.

**C++ Source:**

- **Module**: Engine
- **File**: IAnimationDataModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (AttributeCurve):  [Read-Only] Curve containing the (animated) attribute data
- ``identifier`` (AnimationAttributeIdentifier):  [Read-Only] Identifier to reference this attribute by

<a id="unreal.AnimatedBoneAttribute.__init__"></a>

#### __init__

```python
def __init__(identifier: AnimationAttributeIdentifier = [
    "None", "None", -1, None, [""]
],
             curve: AttributeCurve = []) -> None
```

<a id="unreal.AnimatedBoneAttribute.identifier"></a>

#### identifier

```python
@property
def identifier() -> AnimationAttributeIdentifier
```

(AnimationAttributeIdentifier):  [Read-Only] Identifier to reference this attribute by

<a id="unreal.AnimatedBoneAttribute.curve"></a>

#### curve

```python
@property
def curve() -> AttributeCurve
```

(AttributeCurve):  [Read-Only] Curve containing the (animated) attribute data

<a id="unreal.IndexedCurve"></a>