## Stretch Objects

```python
class Stretch(EnumBase)
```

EStretch

**C++ Source:**

- **Module**: Slate
- **File**: SScaleBox.h

<a id="unreal.Stretch.NONE"></a>

#### NONE

0: Does not scale the content.

<a id="unreal.Stretch.FILL"></a>

#### FILL

1: Scales the content non-uniformly filling the entire space of the area.

<a id="unreal.Stretch.SCALE_TO_FIT"></a>

#### SCALE_TO_FIT

2: Scales the content uniformly (preserving aspect ratio)
until it can no longer scale the content without clipping it.

<a id="unreal.Stretch.SCALE_TO_FIT_X"></a>

#### SCALE_TO_FIT_X

3: Scales the content uniformly (preserving aspect ratio)
until it can no longer scale the content without clipping it along the x-axis,
the y-axis can/will be clipped.

<a id="unreal.Stretch.SCALE_TO_FIT_Y"></a>

#### SCALE_TO_FIT_Y

4: Scales the content uniformly (preserving aspect ratio)
until it can no longer scale the content without clipping it along the y-axis,
the x-axis can/will be clipped.

<a id="unreal.Stretch.SCALE_TO_FILL"></a>

#### SCALE_TO_FILL

5: Scales the content uniformly (preserving aspect ratio), until all sides meet
or exceed the size of the area.  Will result in clipping the longer side.

<a id="unreal.Stretch.SCALE_BY_SAFE_ZONE"></a>

#### SCALE_BY_SAFE_ZONE

6: Scales the content according to the size of the safe zone currently applied to the viewport.

<a id="unreal.Stretch.USER_SPECIFIED"></a>

#### USER_SPECIFIED

7: Scales the content by the scale specified by the user.

<a id="unreal.Stretch.USER_SPECIFIED_WITH_CLIPPING"></a>

#### USER_SPECIFIED_WITH_CLIPPING

8: Scales the content by the scale specified by the user and also clips.

<a id="unreal.ProgressBarFillType"></a>