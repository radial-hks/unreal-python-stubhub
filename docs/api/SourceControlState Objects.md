## SourceControlState Objects

```python
class SourceControlState(StructBase)
```

Snapshot of source control state of a file
see: USourceControlHelpers::QueryFileState()

**C++ Source:**

- **Module**: SourceControl
- **File**: SourceControlHelpers.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_add`` (bool):  [Read-Only] Determine if this file can be added to source control (i.e. is part of the directory
  structure currently under source control)
- ``can_check_in`` (bool):  [Read-Only] Determine if this file can be checked in.
- ``can_check_out`` (bool):  [Read-Only] Determine if this file can be checked out
- ``can_delete`` (bool):  [Read-Only] Determine if source control allows this file to be deleted.
- ``can_edit`` (bool):  [Read-Only] Determine if source control allows this file to be edited
- ``can_revert`` (bool):  [Read-Only] Determine if this file can be reverted, i.e. discard changes and the file will no longer be checked-out.
- ``checked_out_other`` (str):  [Read-Only] Get name of other user who this file already checked out or "" if no other user has it checked out
- ``filename`` (str):  [Read-Only] Get the local filename that this state represents
- ``is_added`` (bool):  [Read-Only] Determine if this file is marked for add
  note: if already checked in then not considered mid add
- ``is_checked_out`` (bool):  [Read-Only] Determine if this file is checked out
- ``is_checked_out_other`` (bool):  [Read-Only] Determine if this file is checked out by someone else
- ``is_conflicted`` (bool):  [Read-Only] Determine if this file is in a conflicted state
- ``is_current`` (bool):  [Read-Only] Determine if this file is up-to-date with the version in source control
- ``is_deleted`` (bool):  [Read-Only] Determine if this file is marked for delete
- ``is_ignored`` (bool):  [Read-Only] Determine if this file is ignored by source control
- ``is_modified`` (bool):  [Read-Only] Determine if this file is modified compared to the version in source control.
- ``is_source_controlled`` (bool):  [Read-Only] Determine if this file is under source control
- ``is_unknown`` (bool):  [Read-Only] Determine if we know anything about the source control state of this file
- ``is_valid`` (bool):  [Read-Only] Indicates whether this source control state has valid information (true) or not (false)

<a id="unreal.SourceControlState.__init__"></a>

#### __init__

```python
def __init__(filename: str = "",
             is_valid: bool = False,
             is_unknown: bool = False,
             can_check_in: bool = False,
             can_check_out: bool = False,
             is_checked_out: bool = False,
             is_current: bool = False,
             is_source_controlled: bool = False,
             is_added: bool = False,
             is_deleted: bool = False,
             is_ignored: bool = False,
             can_edit: bool = False,
             can_delete: bool = False,
             is_modified: bool = False,
             can_add: bool = False,
             is_conflicted: bool = False,
             can_revert: bool = False,
             is_checked_out_other: bool = False,
             checked_out_other: str = "") -> None
```

<a id="unreal.SourceControlState.filename"></a>

#### filename

```python
@property
def filename() -> str
```

(str):  [Read-Only] Get the local filename that this state represents

<a id="unreal.SourceControlState.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Only] Indicates whether this source control state has valid information (true) or not (false)

<a id="unreal.SourceControlState.is_unknown"></a>

#### is_unknown

```python
@property
def is_unknown() -> bool
```

(bool):  [Read-Only] Determine if we know anything about the source control state of this file

<a id="unreal.SourceControlState.can_check_in"></a>

#### can_check_in

```python
@property
def can_check_in() -> bool
```

(bool):  [Read-Only] Determine if this file can be checked in.

<a id="unreal.SourceControlState.can_check_out"></a>

#### can_check_out

```python
@property
def can_check_out() -> bool
```

(bool):  [Read-Only] Determine if this file can be checked out

<a id="unreal.SourceControlState.is_checked_out"></a>

#### is_checked_out

```python
@property
def is_checked_out() -> bool
```

(bool):  [Read-Only] Determine if this file is checked out

<a id="unreal.SourceControlState.is_current"></a>

#### is_current

```python
@property
def is_current() -> bool
```

(bool):  [Read-Only] Determine if this file is up-to-date with the version in source control

<a id="unreal.SourceControlState.is_source_controlled"></a>

#### is_source_controlled

```python
@property
def is_source_controlled() -> bool
```

(bool):  [Read-Only] Determine if this file is under source control

<a id="unreal.SourceControlState.is_added"></a>

#### is_added

```python
@property
def is_added() -> bool
```

(bool):  [Read-Only] Determine if this file is marked for add
note: if already checked in then not considered mid add

<a id="unreal.SourceControlState.is_deleted"></a>

#### is_deleted

```python
@property
def is_deleted() -> bool
```

(bool):  [Read-Only] Determine if this file is marked for delete

<a id="unreal.SourceControlState.is_ignored"></a>

#### is_ignored

```python
@property
def is_ignored() -> bool
```

(bool):  [Read-Only] Determine if this file is ignored by source control

<a id="unreal.SourceControlState.can_edit"></a>

#### can_edit

```python
@property
def can_edit() -> bool
```

(bool):  [Read-Only] Determine if source control allows this file to be edited

<a id="unreal.SourceControlState.can_delete"></a>

#### can_delete

```python
@property
def can_delete() -> bool
```

(bool):  [Read-Only] Determine if source control allows this file to be deleted.

<a id="unreal.SourceControlState.is_modified"></a>

#### is_modified

```python
@property
def is_modified() -> bool
```

(bool):  [Read-Only] Determine if this file is modified compared to the version in source control.

<a id="unreal.SourceControlState.can_add"></a>

#### can_add

```python
@property
def can_add() -> bool
```

(bool):  [Read-Only] Determine if this file can be added to source control (i.e. is part of the directory
structure currently under source control)

<a id="unreal.SourceControlState.is_conflicted"></a>

#### is_conflicted

```python
@property
def is_conflicted() -> bool
```

(bool):  [Read-Only] Determine if this file is in a conflicted state

<a id="unreal.SourceControlState.can_revert"></a>

#### can_revert

```python
@property
def can_revert() -> bool
```

(bool):  [Read-Only] Determine if this file can be reverted, i.e. discard changes and the file will no longer be checked-out.

<a id="unreal.SourceControlState.is_checked_out_other"></a>

#### is_checked_out_other

```python
@property
def is_checked_out_other() -> bool
```

(bool):  [Read-Only] Determine if this file is checked out by someone else

<a id="unreal.SourceControlState.checked_out_other"></a>

#### checked_out_other

```python
@property
def checked_out_other() -> str
```

(str):  [Read-Only] Get name of other user who this file already checked out or "" if no other user has it checked out

<a id="unreal.RevisionInfo"></a>