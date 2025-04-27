## UINavigationRule Objects

```python
class UINavigationRule(EnumBase)
```

EUINavigation Rule

**C++ Source:**

- **Module**: SlateCore
- **File**: NavigationReply.h

<a id="unreal.UINavigationRule.ESCAPE"></a>

#### ESCAPE

0: Allow the movement to continue in that direction, seeking the next navigable widget automatically.

<a id="unreal.UINavigationRule.EXPLICIT"></a>

#### EXPLICIT

1: Move to a specific widget.

<a id="unreal.UINavigationRule.WRAP"></a>

#### WRAP

2: Wrap movement inside this container, causing the movement to cycle around from the opposite side,
if the navigation attempt would have escaped.

<a id="unreal.UINavigationRule.STOP"></a>

#### STOP

3: Stops movement in this direction

<a id="unreal.UINavigationRule.CUSTOM"></a>

#### CUSTOM

4: Custom navigation handled by user code.

<a id="unreal.UINavigationRule.CUSTOM_BOUNDARY"></a>

#### CUSTOM_BOUNDARY

5: Custom navigation handled by user code if the boundary is hit.

<a id="unreal.UINavigationRule.INVALID"></a>

#### INVALID

6: Invalid Rule

<a id="unreal.ButtonClickMethod"></a>