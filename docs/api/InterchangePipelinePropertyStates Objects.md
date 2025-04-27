## InterchangePipelinePropertyStates Objects

```python
class InterchangePipelinePropertyStates(StructBase)
```

Interchange Pipeline Property States

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangePipelineBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``basic_layout_states`` (InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the import context.
- ``import_states`` (InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the import context
- ``locked`` (bool):  [Read-Write] If true, the property is locked.
- ``pre_dialog_reset`` (bool):  [Read-Write] If true, the property will be reset to default when loading the import dialog.
- ``reimport_states`` (InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the reimport context.

<a id="unreal.InterchangePipelinePropertyStates.__init__"></a>

#### __init__

```python
def __init__(
    locked: bool = False,
    pre_dialog_reset: bool = False,
    basic_layout_states: InterchangePipelinePropertyStatePerContext = [True],
    import_states: InterchangePipelinePropertyStatePerContext = [True],
    reimport_states: InterchangePipelinePropertyStatePerContext = [True
                                                                   ]) -> None
```

<a id="unreal.InterchangePipelinePropertyStates.locked"></a>

#### locked

```python
@property
def locked() -> bool
```

(bool):  [Read-Write] If true, the property is locked.

<a id="unreal.InterchangePipelinePropertyStates.locked"></a>

#### locked

```python
@locked.setter
def locked(value: bool) -> None
```

<a id="unreal.InterchangePipelinePropertyStates.pre_dialog_reset"></a>

#### pre_dialog_reset

```python
@property
def pre_dialog_reset() -> bool
```

(bool):  [Read-Write] If true, the property will be reset to default when loading the import dialog.

<a id="unreal.InterchangePipelinePropertyStates.pre_dialog_reset"></a>

#### pre_dialog_reset

```python
@pre_dialog_reset.setter
def pre_dialog_reset(value: bool) -> None
```

<a id="unreal.InterchangePipelinePropertyStates.basic_layout_states"></a>

#### basic_layout_states

```python
@property
def basic_layout_states() -> InterchangePipelinePropertyStatePerContext
```

(InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the import context.

<a id="unreal.InterchangePipelinePropertyStates.basic_layout_states"></a>

#### basic_layout_states

```python
@basic_layout_states.setter
def basic_layout_states(
        value: InterchangePipelinePropertyStatePerContext) -> None
```

<a id="unreal.InterchangePipelinePropertyStates.import_states"></a>

#### import_states

```python
@property
def import_states() -> InterchangePipelinePropertyStatePerContext
```

(InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the import context

<a id="unreal.InterchangePipelinePropertyStates.import_states"></a>

#### import_states

```python
@import_states.setter
def import_states(value: InterchangePipelinePropertyStatePerContext) -> None
```

<a id="unreal.InterchangePipelinePropertyStates.reimport_states"></a>

#### reimport_states

```python
@property
def reimport_states() -> InterchangePipelinePropertyStatePerContext
```

(InterchangePipelinePropertyStatePerContext):  [Read-Write] The property states for the reimport context.

<a id="unreal.InterchangePipelinePropertyStates.reimport_states"></a>

#### reimport_states

```python
@reimport_states.setter
def reimport_states(value: InterchangePipelinePropertyStatePerContext) -> None
```

<a id="unreal.InterchangeUserDefinedAttributeInfo"></a>