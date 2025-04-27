## MappingQueryIssue Objects

```python
class MappingQueryIssue(StructBase)
```

Potential issue raised with a mapping request

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputMappingQuery.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocking_action`` (InputAction):  [Read-Write] Action within the input context that caused the blockage
- ``blocking_context`` (InputMappingContext):  [Read-Write] Input context that contains a blocking action bound to the queried key
- ``issue`` (MappingQueryIssueFlag):  [Read-Write]

<a id="unreal.MappingQueryIssue.__init__"></a>

#### __init__

```python
def __init__(issue: MappingQueryIssueFlag = MappingQueryIssueFlag.NO_ISSUE,
             blocking_context: InputMappingContext = None,
             blocking_action: InputAction = None) -> None
```

<a id="unreal.MappingQueryIssue.issue"></a>

#### issue

```python
@property
def issue() -> MappingQueryIssueFlag
```

(MappingQueryIssueFlag):  [Read-Only]

<a id="unreal.MappingQueryIssue.blocking_context"></a>

#### blocking_context

```python
@property
def blocking_context() -> InputMappingContext
```

(InputMappingContext):  [Read-Only] Input context that contains a blocking action bound to the queried key

<a id="unreal.MappingQueryIssue.blocking_action"></a>

#### blocking_action

```python
@property
def blocking_action() -> InputAction
```

(InputAction):  [Read-Only] Action within the input context that caused the blockage

<a id="unreal.PlayerMappableKeySlotData"></a>