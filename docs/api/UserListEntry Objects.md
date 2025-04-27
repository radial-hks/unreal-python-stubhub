## UserListEntry Objects

```python
class UserListEntry(Interface)
```

User List Entry

**C++ Source:**

- **Module**: UMG
- **File**: IUserListEntry.h

<a id="unreal.UserListEntry.bp_on_item_selection_changed"></a>

#### bp_on_item_selection_changed

```python
def bp_on_item_selection_changed(is_selected: bool) -> None
```

x.bp_on_item_selection_changed(is_selected) -> None
Called when the selection state of the item represented by this entry changes.

Args:
    is_selected (bool):

<a id="unreal.UserListEntry.bp_on_item_expansion_changed"></a>

#### bp_on_item_expansion_changed

```python
def bp_on_item_expansion_changed(is_expanded: bool) -> None
```

x.bp_on_item_expansion_changed(is_expanded) -> None
Called when the expansion state of the item represented by this entry changes. Tree view entries only.

Args:
    is_expanded (bool):

<a id="unreal.UserListEntry.bp_on_entry_released"></a>

#### bp_on_entry_released

```python
def bp_on_entry_released() -> None
```

x.bp_on_entry_released() -> None
Called when this entry is released from the owning table and no longer represents any list item

<a id="unreal.UserListEntryLibrary"></a>