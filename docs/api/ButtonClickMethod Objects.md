## ButtonClickMethod Objects

```python
class ButtonClickMethod(EnumBase)
```

Enumerates different methods that a button click can be triggered. Normally, DownAndUp is appropriate.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateEnums.h

<a id="unreal.ButtonClickMethod.DOWN_AND_UP"></a>

#### DOWN_AND_UP

0: User must press the button, then release while over the button to trigger the click.
This is the most common type of button.

<a id="unreal.ButtonClickMethod.MOUSE_DOWN"></a>

#### MOUSE_DOWN

1: Click will be triggered immediately on mouse down, and mouse will not be captured.

<a id="unreal.ButtonClickMethod.MOUSE_UP"></a>

#### MOUSE_UP

2: Click will always be triggered when mouse button is released over the button,
even if the button wasn't pressed down over it.

<a id="unreal.ButtonClickMethod.PRECISE_CLICK"></a>

#### PRECISE_CLICK

3: Inside a list, buttons can only be clicked with precise tap.
Moving the pointer will scroll the list, also allows drag-droppable buttons.

<a id="unreal.ButtonTouchMethod"></a>