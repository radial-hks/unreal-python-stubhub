## CurveParameterPair Objects

```python
class CurveParameterPair(StructBase)
```

Curve Parameter Pair

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraAnimNotifies
- **File**: AnimNotifyState_TimedNiagaraEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_curve_name`` (Name):  [Read-Write] Name of the curve in this montage.
- ``user_variable_name`` (Name):  [Read-Write] Name of the Niagara user float variable.

<a id="unreal.CurveParameterPair.__init__"></a>

#### \_\_init\_\_

```python
def __init__(anim_curve_name: Name = "None",
             user_variable_name: Name = "None") -> None
```

<a id="unreal.CurveParameterPair.anim_curve_name"></a>

#### anim\_curve\_name

```python
@property
def anim_curve_name() -> Name
```

(Name):  [Read-Only] Name of the curve in this montage.

<a id="unreal.CurveParameterPair.user_variable_name"></a>

#### user\_variable\_name

```python
@property
def user_variable_name() -> Name
```

(Name):  [Read-Only] Name of the Niagara user float variable.

<a id="unreal.PCGAssetExporterParameters"></a>