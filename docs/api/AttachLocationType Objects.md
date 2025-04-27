## AttachLocationType Objects

```python
class AttachLocationType(EnumBase)
```

deprecated: 'AttachLocationType' was renamed to 'AttachLocation'.

<a id="unreal.AttachLocationType.KEEP_RELATIVE_OFFSET"></a>

#### KEEP_RELATIVE_OFFSET

0: Keeps current relative transform as the relative transform to the new parent.

<a id="unreal.AttachLocationType.KEEP_WORLD_POSITION"></a>

#### KEEP_WORLD_POSITION

1: Automatically calculates the relative transform such that the attached component maintains the same world transform.

<a id="unreal.AttachLocationType.SNAP_TO_TARGET"></a>

#### SNAP_TO_TARGET

2: Snaps location and rotation to the attach point. Calculates the relative scale so that the final world scale of the component remains the same.

<a id="unreal.AttachLocationType.SNAP_TO_TARGET_INCLUDING_SCALE"></a>

#### SNAP_TO_TARGET_INCLUDING_SCALE

3: Snaps entire transform to target, including scale.

<a id="unreal.PSCPoolMethod"></a>