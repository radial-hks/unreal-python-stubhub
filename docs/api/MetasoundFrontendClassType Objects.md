## MetasoundFrontendClassType Objects

```python
class MetasoundFrontendClassType(EnumBase)
```

EMetasound Frontend Class Type

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

<a id="unreal.MetasoundFrontendClassType.EXTERNAL"></a>

#### EXTERNAL

0: The MetaSound class is defined externally, in compiled code or in another document.

<a id="unreal.MetasoundFrontendClassType.GRAPH"></a>

#### GRAPH

1: The MetaSound class is a graph within the containing document.

<a id="unreal.MetasoundFrontendClassType.INPUT"></a>

#### INPUT

2: The MetaSound class is an input into a graph in the containing document.

<a id="unreal.MetasoundFrontendClassType.OUTPUT"></a>

#### OUTPUT

3: The MetaSound class is an output from a graph in the containing document.

<a id="unreal.MetasoundFrontendClassType.LITERAL"></a>

#### LITERAL

4: The MetaSound class is an literal requiring a literal value to construct.

<a id="unreal.MetasoundFrontendClassType.VARIABLE"></a>

#### VARIABLE

5: The MetaSound class is an variable requiring a literal value to construct.

<a id="unreal.MetasoundFrontendClassType.VARIABLE_DEFERRED_ACCESSOR"></a>

#### VARIABLE_DEFERRED_ACCESSOR

6: The MetaSound class accesses variables.

<a id="unreal.MetasoundFrontendClassType.VARIABLE_ACCESSOR"></a>

#### VARIABLE_ACCESSOR

7: The MetaSound class accesses variables.

<a id="unreal.MetasoundFrontendClassType.VARIABLE_MUTATOR"></a>

#### VARIABLE_MUTATOR

8: The MetaSound class mutates variables.

<a id="unreal.MetasoundFrontendClassType.TEMPLATE"></a>

#### TEMPLATE

9: The MetaSound class is defined only by the Frontend, and associatively
performs a functional operation within the given document in a registration/cook step.

<a id="unreal.AutoMapChainType"></a>