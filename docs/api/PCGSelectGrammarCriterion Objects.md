## PCGSelectGrammarCriterion Objects

```python
class PCGSelectGrammarCriterion(StructBase)
```

Criteria to compare against an input value for conditionally selecting a grammar.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSelectGrammar.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``comparator`` (PCGSelectGrammarComparator):  [Read-Write] Comparison operator of a selected input value against a criterion's value.
- ``first_value`` (double):  [Read-Write] Compared against the input value.
- ``grammar`` (str):  [Read-Write] The selected grammar result if the condition evaluates to true.
- ``key`` (Name):  [Read-Write] Key representation of a potential grammar selection.
- ``second_value`` (double):  [Read-Write] Used for comparison in range-based or ternary conditions.

<a id="unreal.PCGSelectGrammarCriterion.__init__"></a>

#### __init__

```python
def __init__(key: Name = "None",
             comparator: PCGSelectGrammarComparator = 0,
             first_value: float = 0.000000,
             second_value: float = 0.000000,
             grammar: str = "") -> None
```

<a id="unreal.PCGSelectGrammarCriterion.key"></a>

#### key

```python
@property
def key() -> Name
```

(Name):  [Read-Write] Key representation of a potential grammar selection.

<a id="unreal.PCGSelectGrammarCriterion.key"></a>

#### key

```python
@key.setter
def key(value: Name) -> None
```

<a id="unreal.PCGSelectGrammarCriterion.comparator"></a>

#### comparator

```python
@property
def comparator() -> PCGSelectGrammarComparator
```

(PCGSelectGrammarComparator):  [Read-Write] Comparison operator of a selected input value against a criterion's value.

<a id="unreal.PCGSelectGrammarCriterion.comparator"></a>

#### comparator

```python
@comparator.setter
def comparator(value: PCGSelectGrammarComparator) -> None
```

<a id="unreal.PCGSelectGrammarCriterion.first_value"></a>

#### first_value

```python
@property
def first_value() -> float
```

(double):  [Read-Write] Compared against the input value.

<a id="unreal.PCGSelectGrammarCriterion.first_value"></a>

#### first_value

```python
@first_value.setter
def first_value(value: float) -> None
```

<a id="unreal.PCGSelectGrammarCriterion.second_value"></a>

#### second_value

```python
@property
def second_value() -> float
```

(double):  [Read-Write] Used for comparison in range-based or ternary conditions.

<a id="unreal.PCGSelectGrammarCriterion.second_value"></a>

#### second_value

```python
@second_value.setter
def second_value(value: float) -> None
```

<a id="unreal.PCGSelectGrammarCriterion.grammar"></a>

#### grammar

```python
@property
def grammar() -> str
```

(str):  [Read-Write] The selected grammar result if the condition evaluates to true.

<a id="unreal.PCGSelectGrammarCriterion.grammar"></a>

#### grammar

```python
@grammar.setter
def grammar(value: str) -> None
```

<a id="unreal.PCGSelectGrammarCriteriaAttributeNames"></a>