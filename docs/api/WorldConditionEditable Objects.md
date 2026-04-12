## WorldConditionEditable Objects

```python
class WorldConditionEditable(StructBase)
```

Struct used to store a world condition in editor. Used internally.
Note that the Operator and ExpressionDepth are stored here separately from the World Condition to make sure they are not reset if the Condition is empty.

**C++ Source:**

- **Plugin**: WorldConditions
- **Module**: WorldConditions
- **File**: WorldConditionQuery.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (InstancedStruct):  [Read-Write] Instance of a world condition.
- ``expression_depth`` (uint8):  [Read-Write] Expression depth controlling the parenthesis of the expression.
- ``invert`` (bool):  [Read-Write] Controls whether the value of the expressions as calculated by IsTrue should be inverted.
- ``operator`` (WorldConditionOperator):  [Read-Write] Operator describing how the results of the condition is combined with other conditions.

<a id="unreal.WorldConditionEditable.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SpriteGeometryShape"></a>