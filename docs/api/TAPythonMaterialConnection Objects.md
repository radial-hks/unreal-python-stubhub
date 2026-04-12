## TAPythonMaterialConnection Objects

```python
class TAPythonMaterialConnection(StructBase)
```

TAPython Material Connection

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonMaterialLib.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``left_expression_index`` (int32):  [Read-Write] The index of material expression in source material's expressions, which the connection from
- ``left_output_index`` (int32):  [Read-Write] The index of output in the expression
- ``left_output_name`` (str):  [Read-Write] The name of output pin
- ``right_expression_index`` (int32):  [Read-Write] The index of material expression in source material's expressions, which the connection to
- ``right_expression_input_index`` (int32):  [Read-Write] The index of input in the expression
- ``right_expression_input_name`` (str):  [Read-Write] The name of input pin

<a id="unreal.TAPythonMaterialConnection.__init__"></a>

#### \_\_init\_\_

```python
def __init__(left_expression_index: int = 0,
             left_output_index: int = 0,
             left_output_name: str = "",
             right_expression_index: int = 0,
             right_expression_input_index: int = 0,
             right_expression_input_name: str = "") -> None
```

<a id="unreal.TAPythonMaterialConnection.left_expression_index"></a>

#### left\_expression\_index

```python
@property
def left_expression_index() -> int
```

(int32):  [Read-Write] The index of material expression in source material's expressions, which the connection from

<a id="unreal.TAPythonMaterialConnection.left_expression_index"></a>

#### left\_expression\_index

```python
@left_expression_index.setter
def left_expression_index(value: int) -> None
```

<a id="unreal.TAPythonMaterialConnection.left_output_index"></a>

#### left\_output\_index

```python
@property
def left_output_index() -> int
```

(int32):  [Read-Write] The index of output in the expression

<a id="unreal.TAPythonMaterialConnection.left_output_index"></a>

#### left\_output\_index

```python
@left_output_index.setter
def left_output_index(value: int) -> None
```

<a id="unreal.TAPythonMaterialConnection.left_output_name"></a>

#### left\_output\_name

```python
@property
def left_output_name() -> str
```

(str):  [Read-Write] The name of output pin

<a id="unreal.TAPythonMaterialConnection.left_output_name"></a>

#### left\_output\_name

```python
@left_output_name.setter
def left_output_name(value: str) -> None
```

<a id="unreal.TAPythonMaterialConnection.right_expression_index"></a>

#### right\_expression\_index

```python
@property
def right_expression_index() -> int
```

(int32):  [Read-Write] The index of material expression in source material's expressions, which the connection to

<a id="unreal.TAPythonMaterialConnection.right_expression_index"></a>

#### right\_expression\_index

```python
@right_expression_index.setter
def right_expression_index(value: int) -> None
```

<a id="unreal.TAPythonMaterialConnection.right_expression_input_index"></a>

#### right\_expression\_input\_index

```python
@property
def right_expression_input_index() -> int
```

(int32):  [Read-Write] The index of input in the expression

<a id="unreal.TAPythonMaterialConnection.right_expression_input_index"></a>

#### right\_expression\_input\_index

```python
@right_expression_input_index.setter
def right_expression_input_index(value: int) -> None
```

<a id="unreal.TAPythonMaterialConnection.right_expression_input_name"></a>

#### right\_expression\_input\_name

```python
@property
def right_expression_input_name() -> str
```

(str):  [Read-Write] The name of input pin

<a id="unreal.TAPythonMaterialConnection.right_expression_input_name"></a>

#### right\_expression\_input\_name

```python
@right_expression_input_name.setter
def right_expression_input_name(value: str) -> None
```

<a id="unreal.StaticSwitchInfo"></a>