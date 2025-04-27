## MappingQueryResult Objects

```python
class MappingQueryResult(EnumBase)
```

Result summary from a QueryMapKeyIn... call

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputMappingQuery.h

<a id="unreal.MappingQueryResult.ERROR_ENHANCED_INPUT_NOT_ENABLED"></a>

#### ERROR_ENHANCED_INPUT_NOT_ENABLED

0: Query failed because the player controller being queried is not configured to support enhanced input (PlayerInput is not Enhanced).

<a id="unreal.MappingQueryResult.ERROR_INPUT_CONTEXT_NOT_IN_ACTIVE_CONTEXTS"></a>

#### ERROR_INPUT_CONTEXT_NOT_IN_ACTIVE_CONTEXTS

1: Query failed because the input context being queried against is not part of the active context list.

<a id="unreal.MappingQueryResult.ERROR_INVALID_ACTION"></a>

#### ERROR_INVALID_ACTION

2: Query failed because the action being queried against is None/null

<a id="unreal.MappingQueryResult.NOT_MAPPABLE"></a>

#### NOT_MAPPABLE

3: Mapping cannot be applied due to blocking issues. Check OutIssues for details.

<a id="unreal.MappingQueryResult.MAPPING_AVAILABLE"></a>

#### MAPPING_AVAILABLE

4: Mapping will not affect any existing mappings and is safe to apply.

<a id="unreal.MappingQueryIssueFlag"></a>