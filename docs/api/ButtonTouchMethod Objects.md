## ButtonTouchMethod Objects

```python
class ButtonTouchMethod(EnumBase)
```

Ways in which touch interactions trigger a "Clicked" event.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateEnums.h

<a id="unreal.ButtonTouchMethod.DOWN_AND_UP"></a>

#### DOWN_AND_UP

0: Most buttons behave this way.

<a id="unreal.ButtonTouchMethod.DOWN"></a>

#### DOWN

1: Click will be triggered immediately on touch down, and touch will not be captured.

<a id="unreal.ButtonTouchMethod.PRECISE_TAP"></a>

#### PRECISE_TAP

2: Inside a list, buttons can only be clicked with precise tap.
Moving the pointer will scroll the list.

<a id="unreal.ButtonPressMethod"></a>