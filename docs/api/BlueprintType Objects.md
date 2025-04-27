## BlueprintType Objects

```python
class BlueprintType(EnumBase)
```

Enumerates types of blueprints.

**C++ Source:**

- **Module**: Engine
- **File**: Blueprint.h

<a id="unreal.BlueprintType.BPTYPE_NORMAL"></a>

#### BPTYPE_NORMAL

0: Normal blueprint.

<a id="unreal.BlueprintType.BPTYPE_CONST"></a>

#### BPTYPE_CONST

1: Blueprint that is const during execution (no state graph and methods cannot modify member variables).

<a id="unreal.BlueprintType.BPTYPE_MACRO_LIBRARY"></a>

#### BPTYPE_MACRO_LIBRARY

2: Blueprint that serves as a container for macros to be used in other blueprints.

<a id="unreal.BlueprintType.BPTYPE_INTERFACE"></a>

#### BPTYPE_INTERFACE

3: Blueprint that serves as an interface to be implemented by other blueprints.

<a id="unreal.BlueprintType.BPTYPE_LEVEL_SCRIPT"></a>

#### BPTYPE_LEVEL_SCRIPT

4: Blueprint that handles level scripting.

<a id="unreal.BlueprintType.BPTYPE_FUNCTION_LIBRARY"></a>

#### BPTYPE_FUNCTION_LIBRARY

5: Blueprint that serves as a container for functions to be used in other blueprints.

<a id="unreal.ContentBrowserDataMenuContext_AddNewMenuDomain"></a>