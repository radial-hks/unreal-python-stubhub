## InterchangeUserDefinedAttributesAPI Objects

```python
class InterchangeUserDefinedAttributesAPI(Object)
```

UInterchangeUserDefinedAttributesAPI is used to store and retrieve user-defined attributes such as DCC node attributes, so that pipelines have access to those attributes.
Every user-defined attribute has a name, a value, and an optional AnimationPayloadKey: an FRichCurve that is a float curve.
The value type must be supported by the UE::Interchange::EAttributeTypes enumeration.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeUserDefinedAttribute.h

<a id="unreal.InterchangeUserDefinedAttributesAPI.remove_user_defined_attribute"></a>

#### remove_user_defined_attribute

```python
@classmethod
def remove_user_defined_attribute(cls, interchange_node: InterchangeBaseNode,
                                  user_defined_attribute_name: str) -> bool
```

X.remove_user_defined_attribute(interchange_node, user_defined_attribute_name) -> bool
Remove the specified user-defined attribute.

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): The name of the user-defined attribute to remove.

Returns:
    bool: True if the attribute exists and was removed, or if the attribute doesn't exist. Returns false if the attribute exists but could not be removed. Note - User-defined attributes are the user custom attributes from the DCC translated node (for example, extra attributes in Maya). The payload key points to an FRichCurve payload.

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_infos"></a>

#### get_user_defined_attribute_infos

```python
@classmethod
def get_user_defined_attribute_infos(
    cls, interchange_node: InterchangeBaseNode
) -> Array[InterchangeUserDefinedAttributeInfo]
```

X.get_user_defined_attribute_infos(interchange_node) -> Array[InterchangeUserDefinedAttributeInfo]
Get User Defined Attribute Infos

Args:
    interchange_node (InterchangeBaseNode): 

Returns:
    Array[InterchangeUserDefinedAttributeInfo]: 

    user_defined_attribute_infos (Array[InterchangeUserDefinedAttributeInfo]):

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_int32"></a>

#### get_user_defined_attribute_int32

```python
@classmethod
def get_user_defined_attribute_int32(
        cls, interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str) -> Optional[Tuple[int, str]]
```

X.get_user_defined_attribute_int32(interchange_node, user_defined_attribute_name) -> (out_value=int32, out_payload_key=str) or None
Get User Defined Attribute Int 32

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 

Returns:
    tuple or None: 

    out_value (int32): 

    out_payload_key (str):

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_f_string"></a>

#### get_user_defined_attribute_f_string

```python
@classmethod
def get_user_defined_attribute_f_string(
        cls, interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str) -> Optional[Tuple[str, str]]
```

X.get_user_defined_attribute_f_string(interchange_node, user_defined_attribute_name) -> (out_value=str, out_payload_key=str) or None
Get User Defined Attribute FString

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 

Returns:
    tuple or None: 

    out_value (str): 

    out_payload_key (str):

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_float"></a>

#### get_user_defined_attribute_float

```python
@classmethod
def get_user_defined_attribute_float(
        cls, interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str) -> Optional[Tuple[float, str]]
```

X.get_user_defined_attribute_float(interchange_node, user_defined_attribute_name) -> (out_value=float, out_payload_key=str) or None
Get User Defined Attribute Float

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 

Returns:
    tuple or None: 

    out_value (float): 

    out_payload_key (str):

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_double"></a>

#### get_user_defined_attribute_double

```python
@classmethod
def get_user_defined_attribute_double(
        cls, interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str) -> Optional[Tuple[float, str]]
```

X.get_user_defined_attribute_double(interchange_node, user_defined_attribute_name) -> (out_value=double, out_payload_key=str) or None
Get User Defined Attribute Double

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 

Returns:
    tuple or None: 

    out_value (double): 

    out_payload_key (str):

<a id="unreal.InterchangeUserDefinedAttributesAPI.get_user_defined_attribute_boolean"></a>

#### get_user_defined_attribute_boolean

```python
@classmethod
def get_user_defined_attribute_boolean(
        cls, interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str) -> Optional[Tuple[bool, str]]
```

X.get_user_defined_attribute_boolean(interchange_node, user_defined_attribute_name) -> (out_value=bool, out_payload_key=str) or None
Get User Defined Attribute Boolean

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 

Returns:
    tuple or None: 

    out_value (bool): 

    out_payload_key (str):

<a id="unreal.InterchangeUserDefinedAttributesAPI.duplicate_all_user_defined_attribute"></a>

#### duplicate_all_user_defined_attribute

```python
@classmethod
def duplicate_all_user_defined_attribute(
        cls, interchange_source_node: InterchangeBaseNode,
        interchange_destination_node: InterchangeBaseNode,
        add_source_node_name: bool) -> None
```

X.duplicate_all_user_defined_attribute(interchange_source_node, interchange_destination_node, add_source_node_name) -> None
Duplicate All User Defined Attribute

Args:
    interchange_source_node (InterchangeBaseNode): 
    interchange_destination_node (InterchangeBaseNode): 
    add_source_node_name (bool):

<a id="unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_int32"></a>

#### create_user_defined_attribute_int32

```python
@classmethod
def create_user_defined_attribute_int32(
        cls,
        interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str,
        value: int,
        payload_key: str,
        requires_delegate: bool = False) -> bool
```

X.create_user_defined_attribute_int32(interchange_node, user_defined_attribute_name, value, payload_key, requires_delegate=False) -> bool
Create User Defined Attribute Int 32

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 
    value (int32): 
    payload_key (str): 
    requires_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_f_string"></a>

#### create_user_defined_attribute_f_string

```python
@classmethod
def create_user_defined_attribute_f_string(
        cls,
        interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str,
        value: str,
        payload_key: str,
        requires_delegate: bool = False) -> bool
```

X.create_user_defined_attribute_f_string(interchange_node, user_defined_attribute_name, value, payload_key, requires_delegate=False) -> bool
Create User Defined Attribute FString

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 
    value (str): 
    payload_key (str): 
    requires_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_float"></a>

#### create_user_defined_attribute_float

```python
@classmethod
def create_user_defined_attribute_float(
        cls,
        interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str,
        value: float,
        payload_key: str,
        requires_delegate: bool = False) -> bool
```

X.create_user_defined_attribute_float(interchange_node, user_defined_attribute_name, value, payload_key, requires_delegate=False) -> bool
Create User Defined Attribute Float

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 
    value (float): 
    payload_key (str): 
    requires_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_double"></a>

#### create_user_defined_attribute_double

```python
@classmethod
def create_user_defined_attribute_double(
        cls,
        interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str,
        value: float,
        payload_key: str,
        requires_delegate: bool = False) -> bool
```

X.create_user_defined_attribute_double(interchange_node, user_defined_attribute_name, value, payload_key, requires_delegate=False) -> bool
Create User Defined Attribute Double

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 
    value (double): 
    payload_key (str): 
    requires_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeUserDefinedAttributesAPI.create_user_defined_attribute_boolean"></a>

#### create_user_defined_attribute_boolean

```python
@classmethod
def create_user_defined_attribute_boolean(
        cls,
        interchange_node: InterchangeBaseNode,
        user_defined_attribute_name: str,
        value: bool,
        payload_key: str,
        requires_delegate: bool = False) -> bool
```

X.create_user_defined_attribute_boolean(interchange_node, user_defined_attribute_name, value, payload_key, requires_delegate=False) -> bool
Create User Defined Attribute Boolean

Args:
    interchange_node (InterchangeBaseNode): 
    user_defined_attribute_name (str): 
    value (bool): 
    payload_key (str): 
    requires_delegate (bool): 

Returns:
    bool:

<a id="unreal.PropertyPathTestObject"></a>