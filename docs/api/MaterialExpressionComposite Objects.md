## MaterialExpressionComposite Objects

```python
class MaterialExpressionComposite(MaterialExpression)
```

Composite (subgraph) expression. Exists purely for organzational purposes.
Under the hood uses reroute expressions for graph compilation. See below
to understand how a particular reroute's input / output correlates to
the inputs / outputs of composites and their pin bases.

     _________________          _________________
    |   INPUT BASE    |        |   OUTPUT BASE   |
    +--------+--------+        +--------+--------+
    |        |   (>)  |   ->   |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |   (>)  |        |  (>)   |        |
    |        |        |        |        |        |
    +--------+--------+        +--------+--------+
    | NODE IN:  NONE  |        | NODE IN:  PINS  |
    | NODE OUT: PINS  |        | NODE OUT: NONE  |
    |_________________|        |_________________|

                  ^                |
                  |                v
             ____________________________
            |         COMPOSITE          |
            +---------+--------+---------+
        ->  |    (>)  |        |  (>)    |  ->
            |    (>)  |        |  (>)    |
            |    (>)  |        |  (>)    |
            |    (>)  |        |  (>)    |
            |         |        |         |
            +---------+--------+---------+
            | NODE IN:  TO INPUT BASE    |
            | NODE OUT: FROM OUTPUT BASE |
            |____________________________|

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionComposite.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``subgraph_name`` (str):  [Read-Write]

<a id="unreal.MaterialExpressionConstant"></a>