## OptimusNodeGraphType Objects

```python
class OptimusNodeGraphType(EnumBase)
```

The use type of a particular graph

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusNodeGraph.h

<a id="unreal.OptimusNodeGraphType.SETUP"></a>

#### SETUP

0: Execution graphs

<a id="unreal.OptimusNodeGraphType.UPDATE"></a>

#### UPDATE

1: Called once during an actor's setup event

<a id="unreal.OptimusNodeGraphType.EXTERNAL_TRIGGER"></a>

#### EXTERNAL_TRIGGER

2: Called on every tick

<a id="unreal.OptimusNodeGraphType.FUNCTION"></a>

#### FUNCTION

3: Called when triggered from a blueprint // Storage graphs

<a id="unreal.OptimusNodeGraphType.SUB_GRAPH"></a>

#### SUB_GRAPH

4: Used to store function graphs

<a id="unreal.OptimusNodeGraphType.TRANSIENT"></a>

#### TRANSIENT

5: Used to store sub-graphs within other graphs

<a id="unreal.RetargetSourceOrTarget"></a>