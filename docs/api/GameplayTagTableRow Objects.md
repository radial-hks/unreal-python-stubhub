## GameplayTagTableRow Objects

```python
class GameplayTagTableRow(TableRowBase)
```

Simple struct for a table row in the gameplay tag table and element in the ini list

**C++ Source:**

- **Module**: GameplayTags
- **File**: GameplayTagsManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dev_comment`` (str):  [Read-Write] Developer comment clarifying the usage of a particular tag, not user facing
- ``tag`` (Name):  [Read-Write] Tag specified in the table

<a id="unreal.GameplayTagTableRow.__init__"></a>

#### __init__

```python
def __init__(tag: Name = "None", dev_comment: str = "") -> None
```

<a id="unreal.GameplayTagTableRow.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Only] Tag specified in the table

<a id="unreal.GameplayTagTableRow.dev_comment"></a>

#### dev_comment

```python
@property
def dev_comment() -> str
```

(str):  [Read-Only] Developer comment clarifying the usage of a particular tag, not user facing

<a id="unreal.RestrictedGameplayTagTableRow"></a>