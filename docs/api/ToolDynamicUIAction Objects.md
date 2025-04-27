## ToolDynamicUIAction Objects

```python
class ToolDynamicUIAction(StructBase)
```

Tool Dynamic UIAction

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuDelegates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_execute_action`` (ToolMenuDynamicCanExecuteAction):  [Read-Write]
- ``execute_action`` (ToolMenuDynamicExecuteAction):  [Read-Write]
- ``get_action_check_state`` (ToolMenuDynamicGetActionCheckState):  [Read-Write]
- ``is_action_visible_delegate`` (ToolMenuDynamicIsActionButtonVisible):  [Read-Write]

<a id="unreal.ToolDynamicUIAction.__init__"></a>

#### __init__

```python
def __init__(
        execute_action:
    ToolMenuDynamicExecuteAction = ToolMenuDynamicExecuteAction(),
        can_execute_action:
    ToolMenuDynamicCanExecuteAction = ToolMenuDynamicCanExecuteAction(),
        get_action_check_state:
    ToolMenuDynamicGetActionCheckState = ToolMenuDynamicGetActionCheckState(),
        is_action_visible_delegate:
    ToolMenuDynamicIsActionButtonVisible = ToolMenuDynamicIsActionButtonVisible(
    )) -> None
```

<a id="unreal.ToolDynamicUIAction.execute_action"></a>

#### execute_action

```python
@property
def execute_action() -> ToolMenuDynamicExecuteAction
```

(ToolMenuDynamicExecuteAction):  [Read-Write]

<a id="unreal.ToolDynamicUIAction.execute_action"></a>

#### execute_action

```python
@execute_action.setter
def execute_action(value: ToolMenuDynamicExecuteAction) -> None
```

<a id="unreal.ToolDynamicUIAction.can_execute_action"></a>

#### can_execute_action

```python
@property
def can_execute_action() -> ToolMenuDynamicCanExecuteAction
```

(ToolMenuDynamicCanExecuteAction):  [Read-Write]

<a id="unreal.ToolDynamicUIAction.can_execute_action"></a>

#### can_execute_action

```python
@can_execute_action.setter
def can_execute_action(value: ToolMenuDynamicCanExecuteAction) -> None
```

<a id="unreal.ToolDynamicUIAction.get_action_check_state"></a>

#### get_action_check_state

```python
@property
def get_action_check_state() -> ToolMenuDynamicGetActionCheckState
```

(ToolMenuDynamicGetActionCheckState):  [Read-Write]

<a id="unreal.ToolDynamicUIAction.get_action_check_state"></a>

#### get_action_check_state

```python
@get_action_check_state.setter
def get_action_check_state(value: ToolMenuDynamicGetActionCheckState) -> None
```

<a id="unreal.ToolDynamicUIAction.is_action_visible_delegate"></a>

#### is_action_visible_delegate

```python
@property
def is_action_visible_delegate() -> ToolMenuDynamicIsActionButtonVisible
```

(ToolMenuDynamicIsActionButtonVisible):  [Read-Write]

<a id="unreal.ToolDynamicUIAction.is_action_visible_delegate"></a>

#### is_action_visible_delegate

```python
@is_action_visible_delegate.setter
def is_action_visible_delegate(
        value: ToolMenuDynamicIsActionButtonVisible) -> None
```

<a id="unreal.ToolMenuStringCommand"></a>