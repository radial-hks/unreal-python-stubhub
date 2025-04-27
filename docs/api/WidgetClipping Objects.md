## WidgetClipping Objects

```python
class WidgetClipping(EnumBase)
```

This enum controls clipping of widgets in Slate.  By default all SWidgets do not need to clip their children.
Most of the time, you don't need to clip, the only times it becomes important is when something might become hidden
due to panning.  You should use this wisely, as Slate can not batch across clipping areas, so if widget A and widget B
are set to EWidgetClipping::Yes, no drawing that happens inside their widget trees will ever be batch together, adding
additional GPU overhead.

**C++ Source:**

- **Module**: SlateCore
- **File**: Clipping.h

<a id="unreal.WidgetClipping.INHERIT"></a>

#### INHERIT

0: This widget does not clip children, it and all children inherit the clipping area of the last widget that clipped.

<a id="unreal.WidgetClipping.CLIP_TO_BOUNDS"></a>

#### CLIP_TO_BOUNDS

1: This widget clips content the bounds of this widget.  It intersects those bounds with any previous clipping area.

<a id="unreal.WidgetClipping.CLIP_TO_BOUNDS_WITHOUT_INTERSECTING"></a>

#### CLIP_TO_BOUNDS_WITHOUT_INTERSECTING

2: This widget clips to its bounds.  It does NOT intersect with any existing clipping geometry, it pushes a new clipping
state.  Effectively allowing it to render outside the bounds of hierarchy that does clip.

NOTE: This will NOT allow you ignore the clipping zone that is set to [Yes - Always].

<a id="unreal.WidgetClipping.CLIP_TO_BOUNDS_ALWAYS"></a>

#### CLIP_TO_BOUNDS_ALWAYS

3: This widget clips to its bounds.  It intersects those bounds with any previous clipping area.

NOTE: This clipping area can NOT be ignored, it will always clip children.  Useful for hard barriers
in the UI where you never want animations or other effects to break this region.

<a id="unreal.WidgetClipping.ON_DEMAND"></a>

#### ON_DEMAND

4: This widget clips to its bounds when it's Desired Size is larger than the allocated geometry
the widget is given.  If that occurs, it work like [Yes].

NOTE: This mode was primarily added for Text, which is often placed into containers that eventually
are resized to not be able to support the length of the text.  So rather than needing to tag every
container that could contain text with [Yes], which would result in almost no batching, this mode
was added to dynamically adjust the clipping if needed.  The reason not every panel is set to OnDemand,
is because not every panel returns a Desired Size that matches what it plans to render at.

<a id="unreal.SlateBrushDrawType"></a>