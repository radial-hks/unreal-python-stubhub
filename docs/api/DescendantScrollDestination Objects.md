## DescendantScrollDestination Objects

```python
class DescendantScrollDestination(EnumBase)
```

Where to scroll the descendant to

**C++ Source:**

- **Module**: Slate
- **File**: SScrollBox.h

<a id="unreal.DescendantScrollDestination.INTO_VIEW"></a>

#### INTO_VIEW

0: Scroll the widget into view using the least amount of energy possible.  So if the new item
is above the visible set, it will stop as soon as it's in view at the top.  If it's below the
visible set, it stop it comes into view at the bottom.

<a id="unreal.DescendantScrollDestination.TOP_OR_LEFT"></a>

#### TOP_OR_LEFT

1: Always scroll the widget so it appears at the top/Left of the scrollable area.

<a id="unreal.DescendantScrollDestination.CENTER"></a>

#### CENTER

2: Always scroll the widget so it appears at the center of the scrollable area, if possible.
This won't be possible for the first few items and the last few items, as there's not enough
slack.

<a id="unreal.DescendantScrollDestination.BOTTOM_OR_RIGHT"></a>

#### BOTTOM_OR_RIGHT

3: Always scroll the widget so it appears at the bottom/Right of the scrollable area.

<a id="unreal.ScrollWhenFocusChanges"></a>