## MirrorTableRow Objects

```python
class MirrorTableRow(TableRowBase)
```

Base Mirror Table containing all data required by the animation mirroring system.

**C++ Source:**

- **Module**: Engine
- **File**: MirrorDataTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mirror_entry_type`` (MirrorRowType):  [Read-Write]
- ``mirrored_name`` (Name):  [Read-Write]
- ``name`` (Name):  [Read-Write]

<a id="unreal.MirrorTableRow.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             mirrored_name: Name = "None",
             mirror_entry_type: MirrorRowType = MirrorRowType.BONE) -> None
```

<a id="unreal.MirrorTableRow.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.MirrorTableRow.mirrored_name"></a>

#### mirrored_name

```python
@property
def mirrored_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.MirrorTableRow.mirror_entry_type"></a>

#### mirror_entry_type

```python
@property
def mirror_entry_type() -> MirrorRowType
```

(MirrorRowType):  [Read-Only]

<a id="unreal.TrajectorySample"></a>