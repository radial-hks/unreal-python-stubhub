## CameraLensEffectInterfaceClassSupportLibrary Objects

```python
class CameraLensEffectInterfaceClassSupportLibrary(BlueprintFunctionLibrary)
```

Camera Lens Effect Interface Class Support Library

**C++ Source:**

- **Module**: Engine
- **File**: CameraLensEffectInterface.h

<a id="unreal.CameraLensEffectInterfaceClassSupportLibrary.set_interface_class"></a>

#### set_interface_class

```python
@classmethod
def set_interface_class(
    cls, class_: Class, var: CameraLensInterfaceClassSupport
) -> Tuple[CameraLensInterfaceClassSupport, InterfaceValidResult]
```

X.set_interface_class(class_, var) -> (var=CameraLensInterfaceClassSupport, result=InterfaceValidResult)
Set the represented class of the passed in variable. Note: Check the tooltips on the individual pins.
You cannot bypass the validation by connecting a wires to this node!!

Args:
    class_ (type(Class)): MUST implement CameraLensEffectInterface - when connecting variables to the input, take care that the input class does in fact implement the interface.
    var (CameraLensInterfaceClassSupport): The wrapper (for validation purposes) of the lens effect class.

Returns:
    tuple: 

    var (CameraLensInterfaceClassSupport): The wrapper (for validation purposes) of the lens effect class.

    result (InterfaceValidResult):

<a id="unreal.CameraLensEffectInterfaceClassSupportLibrary.is_interface_valid"></a>

#### is_interface_valid

```python
@classmethod
def is_interface_valid(
        cls, camera_lens: CameraLensEffectInterface) -> InterfaceValidResult
```

X.is_interface_valid(camera_lens) -> InterfaceValidResult
Evaluate the live interface to see if it is a valid reference.

Args:
    camera_lens (CameraLensEffectInterface): 

Returns:
    InterfaceValidResult: 

    result (InterfaceValidResult):

<a id="unreal.CameraLensEffectInterfaceClassSupportLibrary.is_interface_class_valid"></a>

#### is_interface_class_valid

```python
@classmethod
def is_interface_class_valid(
        cls,
        camera_lens: CameraLensInterfaceClassSupport) -> InterfaceValidResult
```

X.is_interface_class_valid(camera_lens) -> InterfaceValidResult
Check whether or not the interface class is valid

Args:
    camera_lens (CameraLensInterfaceClassSupport): 

Returns:
    InterfaceValidResult: 

    result (InterfaceValidResult):

<a id="unreal.CameraLensEffectInterfaceClassSupportLibrary.get_interface_class"></a>

#### get_interface_class

```python
@classmethod
def get_interface_class(cls,
                        camera_lens: CameraLensInterfaceClassSupport) -> Class
```

X.get_interface_class(camera_lens) -> type(Class)
Returns the class represented by this lens effect wrapper...

Args:
    camera_lens (CameraLensInterfaceClassSupport): 

Returns:
    type(Class):

<a id="unreal.CameraModifier"></a>