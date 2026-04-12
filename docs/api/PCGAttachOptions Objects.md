## PCGAttachOptions Objects

```python
class PCGAttachOptions(EnumBase)
```

EPCGAttach Options

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

<a id="unreal.PCGAttachOptions.NOT_ATTACHED"></a>

#### NOT\_ATTACHED

0: Actor will not be attached to the target actor nor placed in an actor folder

<a id="unreal.PCGAttachOptions.ATTACHED"></a>

#### ATTACHED

1: Actor will be attached to the target actor in the given node

<a id="unreal.PCGAttachOptions.IN_FOLDER"></a>

#### IN\_FOLDER

2: Actor will be placed in an actor folder containing the name of the target actor.

<a id="unreal.PCGAttachOptions.IN_GRAPH_FOLDER"></a>

#### IN\_GRAPH\_FOLDER

3: Actor will be placed in a folder named after the top graph it was generated from.

<a id="unreal.PCGAttachOptions.IN_GENERATED_FOLDER"></a>

#### IN\_GENERATED\_FOLDER

4: Actor will be placed in the PCG_Generated folder.

<a id="unreal.PCGGetDataFromActorMode"></a>