## ReimportStrategyFlags Objects

```python
class ReimportStrategyFlags(EnumBase)
```

namespace UE::Interchange

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeFactoryBaseNode.h

<a id="unreal.ReimportStrategyFlags.APPLY_NO_PROPERTIES"></a>

#### APPLY_NO_PROPERTIES

0: Do not apply any properties when reimporting. Simply change the source data

<a id="unreal.ReimportStrategyFlags.APPLY_PIPELINE_PROPERTIES"></a>

#### APPLY_PIPELINE_PROPERTIES

1: Always apply all properties specified by the pipeline.

<a id="unreal.ReimportStrategyFlags.APPLY_EDITOR_CHANGED_PROPERTIES"></a>

#### APPLY_EDITOR_CHANGED_PROPERTIES

2: Always apply all properties specified by the pipeline, but leave the properties that were modified in the editor since the last import.

<a id="unreal.PropertyPathTestEnum"></a>