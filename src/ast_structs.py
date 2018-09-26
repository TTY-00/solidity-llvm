# coding:utf-8
#!/usr/bin/env python3

'''
This file defines structs in ast file.
'''



class SourceUnit:
    '''
    A struct for one source file.
    ps: the `name` in SourceUint is the `absolutePath` in json file,which is ['attributes']['absolutePath']
    e.g. eos.sol
    '''
    _id = 0
    name = ''
    exportedSymbols = {}
    contract_list = []


class ContractDefinition:
    '''
    A struct for one contract. 
    ps: the `name` means ['attributes']['name']
    e.g. function_list is a list for FunctionDefinition elements.
    '''
    _id = 0
    name = ''
    contractKind = ''
    baseContracts = []
    contractDependencies = []
    linearizedBaseContracts = []
    variable_list = []
    struct_list = []
    enum_list = []
    modifierdef_list = []
    function_list = []
    event_list = []
    inheritance_list = []
    block_list = []


class FunctionDefinition:
    '''
    A struct for one function. 
    '''
    _id = 0
    name = ''
    parameterlist_list = []
    modifierinv_list = []
    block_list = []


class EventDefinition:
    '''
    A struct for one event.
    '''
    _id = 0
    name = ''
    parameterlist_list = []


class ModifierDefinition:
    '''
    ModifierDefinition is a function for contract. 
    '''
    _id = 0
    name = ''
    visibility = ''
    parameterlist_list = []
    block_list = []


class ModifierInvocation:
    '''
    ModifierInvocation is a child for function.
    '''
    _id = 0
    name = 'ModifierInvocation'
    identifier_list = []


class Identifier:
    '''
    Identifier is a child for ModifierInvocation.
    '''
    _id = 0
    name = 'Identifier'
    referencedDeclaration = 0
    value = ''

    ir_result = None

class ParameterList:
    '''
    This a list of VariableDeclaration.
    '''
    _id = 0
    name = 'ParameterList'
    variable_list = []

    def get_type_list(self):
        type_list = []

        for var in self.variable_list:

            type_list.append(var._type)

        return type_list

    def get_varname_list(self):
        var_list = []

        for var in self.variable_list:
            var_list.append(var.name)

        return var_list

    def get_varptr_list(self):
        ptr_list = []

        for var in self.variable_list:
            ptr_list.append(var.ir_result)

        return ptr_list


class VariableDeclaration:
    '''
    A struct for one variable.
    '''
    _id = 0
    name = ''
    _type = ''
    value = ''
    scope = 0
    visibility = ''

    ir_result = None

class InheritanceSpecifier:
    '''
    A child of contract which contains the farther contratcs.
    '''
    _id = 0
    name = 'InheritanceSpecifier'
    userdefinedtype_list = []


class UserDefinedTypeName:
    '''
    A child of InheritanceSpecifier.
    '''
    _id = 0
    name = ''
    referencedDeclaration = 0
    _type = ''


class Block:
    '''
    A whole block of code.
    '''
    _id = 0
    name = 'Block'
    expressionstatement_list = []
    ifstatement_list = []
    return_list = []


class ExpressionStatement:
    '''
    What is it ?
    '''
    _id = 0
    name = 'ExpressionStatement'
    assignment_list = []


class Return:
    '''
    What is it ?
    '''
    _id = 0
    name = 'Return'
    functionreturnparameters = 0

    ir_result = None

class IfStatement:
    '''
    if
    '''
    _id = 0
    name = 'IfStatement'
    falsebody = "null"


class Assignment:
    '''
    Assignment
    '''
    _id = 0
    name = 'Assignment'
    operator = ''
    _type = ''
    identifier_list = []
    indexaccess_list = []
    functioncall_list = []
    literal_list = []


class IndexAccess:
    '''
    IndexAccess
    '''
    _id = 0
    name = 'IndexAccess'
    _type = ''
    identifier_list = []
    membermccess_list = []


class MemberAccess:
    '''
    argument_types is an attribute but not a child
    '''
    _id = 0
    name = 'MemberAccess'
    _type = ''
    member_name = ''
    referenceddeclaration = 0
    argument_types = []
    identifier_list = []
    indexaccess_list = []


class FunctionCall:
    '''
    FunctionCall
    '''
    _id = 0
    name = 'FunctionCall'
    _type = ''
    type_conversion = 'false'
    identifier_list = []


class Literal:
    '''
    Literal
    '''
    _id = 0
    name = 'Literal'
    hexvalue = ''
    token = ''
    _type = ''
    value = ''


class BinaryOperation:
    '''
    BinaryOperation
    '''
    _id = 0
    name = 'BinaryOperation'
    common_type = ''
    operator = ''
    _type = ''
    identifier_list = []
    literal_list = []
    binaryoperation_list = []
    indexaccess_list = []

    ir_result = None

class TupleExpression:
    '''
    TupleExpression
    '''
    _id = 0
    name = 'TupleExpression'
    _type = ''
    binaryoperation_list = []


class VariableDeclarationStatement:
    '''
    VariableDeclarationStatement
    `assignments` is an attribute but not a child
    '''
    _id = 0
    name = 'VariableDeclarationStatement'
    assignments = []
    variable_list = []
    literal_list = []
    binaryoperation_list = []
    membermccess_list = []


class ForStatement:
    '''
    ForStatement
    '''
    _id = 0
    name = 'ForStatement'
    block_list = []


class UnaryOperation:
    '''
    UnaryOperation
    '''
    _id = 0
    name = 'UnaryOperation'
    operator = ''
    _type = ''
    identifier_list = []
    functioncall_list = []
