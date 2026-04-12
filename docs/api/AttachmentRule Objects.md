## AttachmentRule Objects

```python
class AttachmentRule(EnumBase)
```

Rules for attaching components - needs to be kept synced to EDetachmentRule

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.AttachmentRule.KEEP_RELATIVE"></a>

#### KEEP\_RELATIVE

0: Keeps current relative transform as the relative transform to the new parent.

<a id="unreal.AttachmentRule.KEEP_WORLD"></a>

#### KEEP\_WORLD

1: Automatically calculates the relative transform such that the attached component maintains the same world transform.

<a id="unreal.AttachmentRule.SNAP_TO_TARGET"></a>

#### SNAP\_TO\_TARGET

2: Snaps transform to the attach point

<a id="unreal.GameplayEffectScopedModifierAggregatorType"></a>