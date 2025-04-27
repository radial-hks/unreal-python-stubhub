## UserObjectListEntryLibrary Objects

```python
class UserObjectListEntryLibrary(BlueprintFunctionLibrary)
```

Static library to supply "for free" functionality to widgets that implement IUserListEntry

**C++ Source:**

- **Module**: UMG
- **File**: IUserObjectListEntry.h

<a id="unreal.UserObjectListEntryLibrary.get_list_item_object"></a>

#### get_list_item_object

```python
@classmethod
def get_list_item_object(
        cls, user_object_list_entry: UserObjectListEntry) -> Object
```

X.get_list_item_object(user_object_list_entry) -> Object
Returns the item in the owning list view that this entry is currently assigned to represent.

Args:
    user_object_list_entry (UserObjectListEntry): Note: Visually not transmitted, but this defaults to "self". No need to hook up if calling internally.

Returns:
    Object:

<a id="unreal.PanelWidget"></a>