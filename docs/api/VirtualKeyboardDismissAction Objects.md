## VirtualKeyboardDismissAction Objects

```python
class VirtualKeyboardDismissAction(EnumBase)
```

EVirtual Keyboard Dismiss Action

**C++ Source:**

- **Module**: Slate
- **File**: ISlateEditableTextWidget.h

<a id="unreal.VirtualKeyboardDismissAction.TEXT_CHANGE_ON_DISMISS"></a>

#### TEXT_CHANGE_ON_DISMISS

0: Sends a text changed message when the virtual keyboard is dismissed by the user.

<a id="unreal.VirtualKeyboardDismissAction.TEXT_COMMIT_ON_ACCEPT"></a>

#### TEXT_COMMIT_ON_ACCEPT

1: Send a text commit message if the user dismisses the keyboard by accepting text. Send a text changed message if the user cancels the virtual keyboard.

<a id="unreal.VirtualKeyboardDismissAction.TEXT_COMMIT_ON_DISMISS"></a>

#### TEXT_COMMIT_ON_DISMISS

2: Send a text commit message when the virtual keyboard is dismissed by the user.

<a id="unreal.MultiBoxType"></a>