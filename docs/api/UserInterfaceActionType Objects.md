## UserInterfaceActionType Objects

```python
class UserInterfaceActionType(EnumBase)
```

Types of user interfaces that can be associated with a user interface action

**C++ Source:**

- **Module**: Slate
- **File**: UICommandInfo.h

<a id="unreal.UserInterfaceActionType.NONE"></a>

#### NONE

0: An action which should not be associated with a user interface action

<a id="unreal.UserInterfaceActionType.BUTTON"></a>

#### BUTTON

1: Momentary buttons or menu items.  These support enable state, and execute a delegate when clicked.

<a id="unreal.UserInterfaceActionType.TOGGLE_BUTTON"></a>

#### TOGGLE_BUTTON

2: Toggleable buttons or menu items that store on/off state.  These support enable state, and execute a delegate when toggled.

<a id="unreal.UserInterfaceActionType.RADIO_BUTTON"></a>

#### RADIO_BUTTON

3: Radio buttons are similar to toggle buttons in that they are for menu items that store on/off state.  However they should be used to indicate that menu items in a group can only be in one state

<a id="unreal.UserInterfaceActionType.CHECK"></a>

#### CHECK

4: Similar to Button but will display a readonly checkbox next to the item.

<a id="unreal.UserInterfaceActionType.COLLAPSED_BUTTON"></a>

#### COLLAPSED_BUTTON

5: Similar to Button but has the checkbox area collapsed

<a id="unreal.TextJustify"></a>