## RestrictedGameplayTagTableRow Objects

```python
class RestrictedGameplayTagTableRow(GameplayTagTableRow)
```

Simple struct for a table row in the restricted gameplay tag table and element in the ini list

**C++ Source:**

- **Module**: GameplayTags
- **File**: GameplayTagsManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_non_restricted_children`` (bool):  [Read-Write] Tag specified in the table
- ``dev_comment`` (str):  [Read-Write] Developer comment clarifying the usage of a particular tag, not user facing
- ``tag`` (Name):  [Read-Write] Tag specified in the table

<a id="unreal.RestrictedGameplayTagTableRow.__init__"></a>

#### __init__

```python
def __init__(tag: Name = "None",
             dev_comment: str = "",
             allow_non_restricted_children: bool = False) -> None
```

<a id="unreal.RestrictedGameplayTagTableRow.allow_non_restricted_children"></a>

#### allow_non_restricted_children

```python
@property
def allow_non_restricted_children() -> bool
```

(bool):  [Read-Only] Tag specified in the table

<a id="unreal.EnvNamedValue"></a>