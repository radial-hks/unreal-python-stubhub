## UserListEntryLibrary Objects

```python
class UserListEntryLibrary(BlueprintFunctionLibrary)
```

Static library to supply "for free" functionality to widgets that implement IUserListEntry

**C++ Source:**

- **Module**: UMG
- **File**: IUserListEntry.h

<a id="unreal.UserListEntryLibrary.is_list_item_selected"></a>

#### is_list_item_selected

```python
@classmethod
def is_list_item_selected(cls, user_list_entry: UserListEntry) -> bool
```

X.is_list_item_selected(user_list_entry) -> bool
Returns true if the item represented by this entry is currently selected in the owning list view.

Args:
    user_list_entry (UserListEntry): Note: Visually not transmitted, but this defaults to "self". No need to hook up if calling internally.

Returns:
    bool:

<a id="unreal.UserListEntryLibrary.is_list_item_expanded"></a>

#### is_list_item_expanded

```python
@classmethod
def is_list_item_expanded(cls, user_list_entry: UserListEntry) -> bool
```

X.is_list_item_expanded(user_list_entry) -> bool
Returns true if the item represented by this entry is currently expanded and showing its children. Tree view entries only.

Args:
    user_list_entry (UserListEntry): Note: Visually not transmitted, but this defaults to "self". No need to hook up if calling internally.

Returns:
    bool:

<a id="unreal.UserListEntryLibrary.get_owning_list_view"></a>

#### get_owning_list_view

```python
@classmethod
def get_owning_list_view(cls, user_list_entry: UserListEntry) -> ListViewBase
```

X.get_owning_list_view(user_list_entry) -> ListViewBase
Returns the list view that contains this entry.

Args:
    user_list_entry (UserListEntry): Note: Visually not transmitted, but this defaults to "self". No need to hook up if calling internally.

Returns:
    ListViewBase:

<a id="unreal.UserObjectListEntry"></a>