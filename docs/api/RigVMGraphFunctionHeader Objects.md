## RigVMGraphFunctionHeader Objects

```python
class RigVMGraphFunctionHeader(StructBase)
```

Rig VMGraph Function Header

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMGraphFunctionDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arguments`` (Array[RigVMGraphFunctionArgument]):  [Read-Only]
- ``category`` (str):  [Read-Only]
- ``description`` (str):  [Read-Only]
- ``keywords`` (str):  [Read-Only]
- ``library_pointer`` (RigVMGraphFunctionIdentifier):  [Read-Only]
- ``name`` (Name):  [Read-Only]
- ``node_color`` (LinearColor):  [Read-Only]
- ``node_title`` (str):  [Read-Only]
- ``tooltip`` (Text):  [Read-Write]
  deprecated: Property 'Tooltip' is deprecated.
- ``variant`` (RigVMVariant):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.__init__"></a>

#### __init__

```python
def __init__(library_pointer: RigVMGraphFunctionIdentifier = [[""]],
             variant: RigVMVariant = [[], []],
             name: Name = "None",
             node_title: str = "",
             node_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             description: str = "",
             category: str = "",
             keywords: str = "",
             arguments: Array[RigVMGraphFunctionArgument] = []) -> None
```

<a id="unreal.RigVMGraphFunctionHeader.library_pointer"></a>

#### library_pointer

```python
@property
def library_pointer() -> RigVMGraphFunctionIdentifier
```

(RigVMGraphFunctionIdentifier):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.variant"></a>

#### variant

```python
@property
def variant() -> RigVMVariant
```

(RigVMVariant):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.node_title"></a>

#### node_title

```python
@property
def node_title() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.node_color"></a>

#### node_color

```python
@property
def node_color() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.tooltip"></a>

#### tooltip

```python
@property
def tooltip() -> Text
```

(Text):  [Read-Write]
deprecated: Property 'Tooltip' is deprecated.

<a id="unreal.RigVMGraphFunctionHeader.tooltip"></a>

#### tooltip

```python
@tooltip.setter
def tooltip(value: Text) -> None
```

<a id="unreal.RigVMGraphFunctionHeader.description"></a>

#### description

```python
@property
def description() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.category"></a>

#### category

```python
@property
def category() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.keywords"></a>

#### keywords

```python
@property
def keywords() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionHeader.arguments"></a>

#### arguments

```python
@property
def arguments() -> Array[RigVMGraphFunctionArgument]
```

(Array[RigVMGraphFunctionArgument]):  [Read-Only]

<a id="unreal.RigVMNodeLayout"></a>