## ButtonPressMethod Objects

```python
class ButtonPressMethod(EnumBase)
```

Enumerates different methods that a button can be triggered with keyboard/controller. Normally, DownAndUp is appropriate.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateEnums.h

<a id="unreal.ButtonPressMethod.DOWN_AND_UP"></a>

#### DOWN_AND_UP

0: User must press the button, then release while the button has focus to trigger the click.
This is the most common type of button.

<a id="unreal.ButtonPressMethod.BUTTON_PRESS"></a>

#### BUTTON_PRESS

1: Click will be triggered immediately on button press.

<a id="unreal.ButtonPressMethod.BUTTON_RELEASE"></a>

#### BUTTON_RELEASE

2: Click will always be triggered when a button release occurs on the focused button,
even if the button wasn't pressed while focused.

<a id="unreal.UINavigation"></a>