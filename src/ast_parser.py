# coding:utf-8
#!/usr/bin/env python3

'''
This file is the main parser.
'''

from .util import *
from .ast_structs import *
import json


class AstParser:
    ast_json = None
    # all elements after parsed
    parsed_unit = SourceUnit()
    # all parser functions
    parsers = {}
    # stack depth
    stack_depth = 0

    def __init__(self):
        self.parsers['ContractDefinition'] = self.parser_contract
        self.parsers['FunctionDefinition'] = self.parser_function
        self.parsers['EventDefinition'] = self.parser_event
        self.parsers['ParameterList'] = self.parser_parameterlist
        self.parsers['VariableDeclaration'] = self.parser_variable
        self.parsers['ModifierDefinition'] = self.parser_modifierdef
        self.parsers['ModifierInvocation'] = self.parser_modifierinv
        self.parsers['Identifier'] = self.parser_identifier
        self.parsers['InheritanceSpecifier'] = self.parser_inheritance
        self.parsers['UserDefinedTypeName'] = self.parser_userdefinedtype
        self.parsers['Block'] = self.parser_block
        self.parsers['Return'] = self.parser__return
        self.parsers['ExpressionStatement'] = self.parser_expressionsta
        self.parsers['IfStatement'] = self.parser_ifsta
        self.parsers['Assignment'] = self.parser_assignment
        self.parsers['IndexAccess'] = self.parser_indexaccess
        self.parsers['MemberAccess'] = self.parser_membermccess
        self.parsers['FunctionCall'] = self.parser_functioncall
        self.parsers['Literal'] = self.parser_literal
        self.parsers['BinaryOperation'] = self.parser_binaryoperation
        self.parsers['TupleExpression'] = self.parser_tupleexpression
        self.parsers['VariableDeclarationStatement'] = self.parser_variabledecsta
        self.parsers['ForStatement'] = self.parser_forsta
        self.parsers['UnaryOperation'] = self.parser_unaryoperation

    def parser_contract(self, contract):
        '''
        a parser for one contract.
        '''
        parsed_contract = ContractDefinition()
        parsed_contract._id = contract['id']
        parsed_contract.name = contract['attributes']['name']
        self.log_node_begain(
            contract['name'], parsed_contract.name, parsed_contract._id)

        # parse attributes
        parsed_contract.contractKind = self.item_loader(self.item_loader(
            contract, 'attributes'), 'contractKind')
        parsed_contract.baseContracts = self.item_loader(self.item_loader(
            contract, 'attributes'), 'baseContracts')
        parsed_contract.contractDependencies = self.item_loader(self.item_loader(
            contract, 'attributes'), 'contractDependencies')
        parsed_contract.linearizedBaseContracts = self.item_loader(self.item_loader(
            contract, 'attributes'), 'linearizedBaseContracts')

        # parse childern nodes
        children = self.children_parser(contract)
        if(self.check_childern(children, parsed_contract.name)):
            parsed_contract.function_list = self.item_loader(
                children, 'FunctionDefinition')
            parsed_contract.variable_list = self.item_loader(
                children, 'VariableDeclaration')
            parsed_contract.modifierdef_list = self.item_loader(
                children, 'ModifierDefinition')
            parsed_contract.inheritance_list = self.item_loader(
                children, 'InheritanceSpecifier')
            parsed_contract.block_list = self.item_loader(
                children, 'Block')

        self.log_node_end(contract['name'],
                          parsed_contract.name, parsed_contract._id)

        return parsed_contract

    def parser_function(self, function):
        '''
        a parser for one function.
        '''
        parsed_function = FunctionDefinition()
        parsed_function._id = function['id']
        parsed_function.name = function['attributes']['name']
        self.log_node_begain(
            function['name'], parsed_function.name, parsed_function._id)

        # parse attributes

        # parse childern nodes
        children = self.children_parser(function)
        if(self.check_childern(children, parsed_function.name)):
            parsed_function.parameterlist_list = self.item_loader(
                children, 'ParameterList')
            parsed_function.modifierinv_list = self.item_loader(
                children, 'ModifierInvocation')
            parsed_function.block_list = self.item_loader(
                children, 'Block')

        self.log_node_end(function['name'],
                          parsed_function.name, parsed_function._id)

        return parsed_function

    def parser_event(self, event):
        '''
        a parser for one event.
        '''
        parsed_event = EventDefinition()
        parsed_event._id = event['id']
        parsed_event.name = event['attributes']['name']
        self.log_node_begain(
            event['name'], parsed_event.name, parsed_event._id)

        # parse attributes

        # parse childern nodes
        children = self.children_parser(event)
        if(self.check_childern(children, parsed_event.name)):
            parsed_event.parameterlist_list = self.item_loader(
                children, 'ParameterList')

        self.log_node_end(event['name'],
                          parsed_event.name, parsed_event._id)

        return parsed_event

    def parser_modifierdef(self, modifierdef):
        '''
        a parser for one event.
        '''
        parsed_modifierdef = ModifierDefinition()
        parsed_modifierdef._id = modifierdef['id']
        parsed_modifierdef.name = modifierdef['attributes']['name']
        self.log_node_begain(
            modifierdef['name'], parsed_modifierdef.name, parsed_modifierdef._id)

        # parse attributes
        parsed_modifierdef.visibility = self.item_loader(self.item_loader(
            modifierdef, 'attributes'), 'visibility')

        # parse childern nodes
        children = self.children_parser(modifierdef)
        if(self.check_childern(children, parsed_modifierdef.name)):
            parsed_modifierdef.parameterlist_list = self.item_loader(
                children, 'ParameterList')
            parsed_modifierdef.block_list = self.item_loader(
                children, 'Block')

        self.log_node_end(modifierdef['name'],
                          parsed_modifierdef.name, parsed_modifierdef._id)

        return parsed_modifierdef

    def parser_parameterlist(self, parameterlist):
        '''
        `ParameterList` itself contain a list of variable
        '''
        parsed_parameterlist = ParameterList()
        parsed_parameterlist._id = parameterlist['id']
        # parsed_parameterlist.name = parameterlist['attributes']['name']
        parsed_parameterlist.name = parameterlist['name']
        self.log_node_begain(
            parameterlist['name'], parsed_parameterlist.name, parsed_parameterlist._id)

        # parse attributes
        # **There is no attributes for ParameterList**

        # parse childern nodes
        children = self.children_parser(parameterlist)
        if(self.check_childern(children, parsed_parameterlist.name)):
            parsed_parameterlist.variable_list = self.item_loader(
                children, 'VariableDeclaration')

        self.log_node_end(
            parameterlist['name'], parsed_parameterlist.name, parsed_parameterlist._id)

        return parsed_parameterlist

    def parser_modifierinv(self, modifierinv):
        '''
        `ModifierInvocation` itself contain a list of Identifier
        '''
        parsed_modifierinv = ModifierInvocation()
        parsed_modifierinv._id = modifierinv['id']
        # parsed_modifierinv.name = modifierinv['attributes']['name']
        parsed_modifierinv.name = modifierinv['name']
        self.log_node_begain(
            modifierinv['name'], parsed_modifierinv.name, parsed_modifierinv._id)

        # parse attributes
        # **There is no attributes for modifierinv**

        # parse childern nodes
        children = self.children_parser(modifierinv)
        if(self.check_childern(children, parsed_modifierinv.name)):
            parsed_modifierinv.identifier_list = self.item_loader(
                children, 'Identifier')

        self.log_node_end(
            modifierinv['name'], parsed_modifierinv.name, parsed_modifierinv._id)

        return parsed_modifierinv

    def parser_identifier(self, identifier):
        '''
        a parser for one identifier.
        '''
        parsed_identifier = Identifier()
        parsed_identifier._id = identifier['id']
        # parsed_identifier.name = identifier['attributes']['name']
        parsed_identifier.name = identifier['attributes']['value']
        self.log_node_begain(
            identifier['name'], parsed_identifier.name, parsed_identifier._id)

        # parse attributes
        parsed_identifier.referencedDeclaration = self.item_loader(self.item_loader(
            identifier, 'attributes'), 'referencedDeclaration')
        parsed_identifier.value = self.item_loader(self.item_loader(
            identifier, 'attributes'), 'value')

        # parse childern nodes
        # children = self.children_parser(identifier)
        # if(self.check_childern(children, parsed_identifier.name)):
        #     parsed_identifier.identifier_list = self.item_loader(
        #         children, 'identifierDefinition')

        self.log_node_end(identifier['name'],
                          parsed_identifier.name, parsed_identifier._id)

        return parsed_identifier

    def parser_variable(self, variable):
        '''
        a parser for one variable.
        '''
        parsed_variable = VariableDeclaration()
        parsed_variable._id = variable['id']
        parsed_variable.name = variable['attributes']['name']
        self.log_node_begain(
            variable['name'], parsed_variable.name, parsed_variable._id)

        # parse attributes
        parsed_variable._type = self.item_loader(self.item_loader(
            variable, 'attributes'), 'type')
        parsed_variable.value = self.item_loader(self.item_loader(
            variable, 'attributes'), 'value')
        parsed_variable.scope = self.item_loader(self.item_loader(
            variable, 'attributes'), 'scope')
        parsed_variable.visibility = self.item_loader(self.item_loader(
            variable, 'attributes'), 'visibility')

        # parse childern nodes
        # children = self.children_parser(variable)
        # if(self.check_childern(children, parsed_variable.name)):
        #     parsed_variable.variable_list = self.item_loader(
        #         children, 'variableDefinition')

        self.log_node_end(variable['name'],
                          parsed_variable.name, parsed_variable._id)

        return parsed_variable

    def parser_inheritance(self, inheritance):
        '''
        `InheritanceSpecifier` itself contain a list of Identifier
        '''
        parsed_inheritance = InheritanceSpecifier()
        parsed_inheritance._id = inheritance['id']
        # parsed_inheritance.name = inheritance['attributes']['name']
        parsed_inheritance.name = inheritance['name']
        self.log_node_begain(
            inheritance['name'], parsed_inheritance.name, parsed_inheritance._id)

        # parse attributes
        # **There is no attributes for inheritance**

        # parse childern nodes
        children = self.children_parser(inheritance)
        if(self.check_childern(children, parsed_inheritance.name)):
            parsed_inheritance.userdefinedtype_list = self.item_loader(
                children, 'UserDefinedTypeName')

        self.log_node_end(
            inheritance['name'], parsed_inheritance.name, parsed_inheritance._id)

        return parsed_inheritance

    def parser_userdefinedtype(self, userdefinedtype):
        '''
        a parser for one UserDefinedTypeName.
        '''
        parsed_userdefinedtype = UserDefinedTypeName()
        parsed_userdefinedtype._id = userdefinedtype['id']
        parsed_userdefinedtype.name = userdefinedtype['attributes']['name']
        self.log_node_begain(
            userdefinedtype['name'], parsed_userdefinedtype.name, parsed_userdefinedtype._id)

        # parse attributes
        parsed_userdefinedtype._type = self.item_loader(self.item_loader(
            userdefinedtype, 'attributes'), 'type')
        parsed_userdefinedtype.referencedDeclaration = self.item_loader(self.item_loader(
            userdefinedtype, 'attributes'), 'referencedDeclaration')

        # parse childern nodes
        # children = self.children_parser(userdefinedtype)
        # if(self.check_childern(children, parsed_userdefinedtype.name)):
        #     parsed_userdefinedtype.userdefinedtype_list = self.item_loader(
        #         children, 'userdefinedtypeDefinition')

        self.log_node_end(userdefinedtype['name'],
                          parsed_userdefinedtype.name, parsed_userdefinedtype._id)

        return parsed_userdefinedtype

    def parser_block(self, block):
        '''
        block is code area.
        '''
        parsed_block = Block()
        parsed_block._id = block['id']
        # parsed_block.name = block['attributes']['name']
        parsed_block.name = block['name']
        self.log_node_begain(
            block['name'], parsed_block.name, parsed_block._id)

        # parse attributes
        # **There is no attributes for Block**

        # parse childern nodes
        children = self.children_parser(block)
        if(self.check_childern(children, parsed_block.name)):
            parsed_block.expressionstatement_list = self.item_loader(
                children, 'ExpressionStatement')
        if(self.check_childern(children, parsed_block.name)):
            parsed_block.return_list = self.item_loader(
                children, 'Return')
        if(self.check_childern(children, parsed_block.name)):
            parsed_block.ifstatement_list = self.item_loader(
                children, 'IfStatement')

        self.log_node_end(
            block['name'], parsed_block.name, parsed_block._id)

        return parsed_block

    def parser_expressionsta(self, expressionsta):
        '''
        ExpressionStatement
        '''
        parsed_expressionsta = ExpressionStatement()
        parsed_expressionsta._id = expressionsta['id']
        # parsed_expressionsta.name = expressionsta['attributes']['name']
        parsed_expressionsta.name = expressionsta['name']
        self.log_node_begain(
            expressionsta['name'], parsed_expressionsta.name, parsed_expressionsta._id)

        # parse attributes
        # **There is no attributes for expressionsta**

        # parse childern nodes
        children = self.children_parser(expressionsta)
        if(self.check_childern(children, parsed_expressionsta.name)):
            parsed_expressionsta.assignment_list = self.item_loader(
                children, 'Assignment')

        self.log_node_end(
            expressionsta['name'], parsed_expressionsta.name, parsed_expressionsta._id)

        return parsed_expressionsta

    def parser__return(self, _return):
        '''
        Return
        '''
        parsed__return = Return()
        parsed__return._id = _return['id']
        # parsed__return.name = _return['attributes']['name']
        parsed__return.name = _return['name']
        self.log_node_begain(
            _return['name'], parsed__return.name, parsed__return._id)

        # parse attributes
        parsed__return.functionreturnparameters = self.item_loader(self.item_loader(
            _return, 'attributes'), 'functionReturnParameters')

        # parse childern nodes
        children = self.children_parser(_return)
        # if(self.check_childern(children, parsed__return.name)):
        #     parsed__return.userdefinedtype_list = self.item_loader(
        #         children, 'UserDefinedTypeName')

        self.log_node_end(
            _return['name'], parsed__return.name, parsed__return._id)

        return parsed__return

    def parser_ifsta(self, ifsta):
        '''
        IfStatement
        '''
        parsed_ifsta = IfStatement()
        parsed_ifsta._id = ifsta['id']
        # parsed_ifsta.name = ifsta['attributes']['name']
        parsed_ifsta.name = ifsta['name']
        self.log_node_begain(
            ifsta['name'], parsed_ifsta.name, parsed_ifsta._id)

        # parse attributes
        parsed_ifsta.falsebody = self.item_loader(self.item_loader(
            ifsta, 'attributes'), 'falseBody')

        # parse childern nodes
        children = self.children_parser(ifsta)
        # if(self.check_childern(children, parsed_ifsta.name)):
        #     parsed_ifsta.userdefinedtype_list = self.item_loader(
        #         children, 'UserDefinedTypeName')

        self.log_node_end(
            ifsta['name'], parsed_ifsta.name, parsed_ifsta._id)

        return parsed_ifsta

    def parser_assignment(self, assignment):
        '''
        Assignment
        '''
        parsed_assignment = Assignment()
        parsed_assignment._id = assignment['id']
        # parsed_assignment.name = assignment['attributes']['name']
        parsed_assignment.name = assignment['name']
        self.log_node_begain(
            assignment['name'], parsed_assignment.name, parsed_assignment._id)

        # parse attributes
        parsed_assignment.operator = self.item_loader(self.item_loader(
            assignment, 'attributes'), 'operator')
        parsed_assignment._type = self.item_loader(self.item_loader(
            assignment, 'attributes'), 'type')

        # parse childern nodes
        children = self.children_parser(assignment)
        if(self.check_childern(children, parsed_assignment.name)):
            parsed_assignment.indexaccess_list = self.item_loader(
                children, 'IndexAccess')
        if(self.check_childern(children, parsed_assignment.name)):
            parsed_assignment.functioncall_list = self.item_loader(
                children, 'FunctionCall')
        if(self.check_childern(children, parsed_assignment.name)):
            parsed_assignment.identifier_list = self.item_loader(
                children, 'Identifier')
        if(self.check_childern(children, parsed_assignment.name)):
            parsed_assignment.literal_list = self.item_loader(
                children, 'Literal')

        self.log_node_end(
            assignment['name'], parsed_assignment.name, parsed_assignment._id)

        return parsed_assignment

    def parser_indexaccess(self, indexaccess):
        '''
        IndexAccess
        '''
        parsed_indexaccess = IndexAccess()
        parsed_indexaccess._id = indexaccess['id']
        # parsed_indexaccess.name = indexaccess['attributes']['name']
        parsed_indexaccess.name = indexaccess['name']
        self.log_node_begain(
            indexaccess['name'], parsed_indexaccess.name, parsed_indexaccess._id)

        # parse attributes
        parsed_indexaccess._type = self.item_loader(self.item_loader(
            indexaccess, 'attributes'), 'type')

        # parse childern nodes
        children = self.children_parser(indexaccess)
        if(self.check_childern(children, parsed_indexaccess.name)):
            parsed_indexaccess.membermccess_list = self.item_loader(
                children, 'MemberAccess')
        if(self.check_childern(children, parsed_indexaccess.name)):
            parsed_indexaccess.identifier_list = self.item_loader(
                children, 'Identifier')

        self.log_node_end(
            indexaccess['name'], parsed_indexaccess.name, parsed_indexaccess._id)

        return parsed_indexaccess

    def parser_membermccess(self, membermccess):
        '''
        membermccess
        '''
        parsed_membermccess = MemberAccess()
        parsed_membermccess._id = membermccess['id']
        # parsed_membermccess.name = membermccess['attributes']['name']
        parsed_membermccess.name = membermccess['name']
        self.log_node_begain(
            membermccess['name'], parsed_membermccess.name, parsed_membermccess._id)

        # parse attributes
        parsed_membermccess._type = self.item_loader(self.item_loader(
            membermccess, 'attributes'), 'type')
        parsed_membermccess.member_name = self.item_loader(self.item_loader(
            membermccess, 'attributes'), 'member_name')
        parsed_membermccess.referenceddeclaration = self.item_loader(self.item_loader(
            membermccess, 'attributes'), 'referencedDeclaration')
        parsed_membermccess.argument_types = self.item_loader(self.item_loader(
            membermccess, 'attributes'), 'argumentTypes')

        # parse childern nodes
        children = self.children_parser(membermccess)
        if(self.check_childern(children, parsed_membermccess.name)):
            parsed_membermccess.identifier_list = self.item_loader(
                children, 'Identifier')

        self.log_node_end(
            membermccess['name'], parsed_membermccess.name, parsed_membermccess._id)

        return parsed_membermccess

    def parser_functioncall(self, functioncall):
        '''
        FunctionCall
        '''
        parsed_functioncall = FunctionCall()
        parsed_functioncall._id = functioncall['id']
        # parsed_functioncall.name = functioncall['attributes']['name']
        parsed_functioncall.name = functioncall['name']
        self.log_node_begain(
            functioncall['name'], parsed_functioncall.name, parsed_functioncall._id)

        # parse attributes
        parsed_functioncall._type = self.item_loader(self.item_loader(
            functioncall, 'attributes'), 'type')
        parsed_functioncall.type_conversion = self.item_loader(self.item_loader(
            functioncall, 'attributes'), 'type_conversion')

        # parse childern nodes
        children = self.children_parser(functioncall)
        if(self.check_childern(children, parsed_functioncall.name)):
            parsed_functioncall.identifier_list = self.item_loader(
                children, 'Identifier')

        self.log_node_end(
            functioncall['name'], parsed_functioncall.name, parsed_functioncall._id)

        return parsed_functioncall

    def parser_literal(self, literal):
        '''
        Literal
        '''
        parsed_literal = Literal()
        parsed_literal._id = literal['id']
        # parsed_literal.name = literal['attributes']['name']
        parsed_literal.name = literal['name']
        self.log_node_begain(
            literal['name'], parsed_literal.name, parsed_literal._id)

        # parse attributes
        parsed_literal.hexvalue = self.item_loader(self.item_loader(
            literal, 'attributes'), 'hexvalue')
        parsed_literal.token = self.item_loader(self.item_loader(
            literal, 'attributes'), 'token')
        parsed_literal._type = self.item_loader(self.item_loader(
            literal, 'attributes'), 'type')
        parsed_literal.value = self.item_loader(self.item_loader(
            literal, 'attributes'), 'value')

        # parse childern nodes
        # **There is no child for literal**

        self.log_node_end(
            literal['name'], parsed_literal.name, parsed_literal._id)

        return parsed_literal

    def parser_binaryoperation(self, binaryoperation):
        '''
        BinaryOperation
        '''
        parsed_binaryoperation = BinaryOperation()
        parsed_binaryoperation._id = binaryoperation['id']
        # parsed_binaryoperation.name = binaryoperation['attributes']['name']
        parsed_binaryoperation.name = binaryoperation['name']
        self.log_node_begain(
            binaryoperation['name'], parsed_binaryoperation.name, parsed_binaryoperation._id)

        # parse attributes
        parsed_binaryoperation.common_type = self.item_loader(self.item_loader(
            binaryoperation, 'attributes'), 'commonType')
        parsed_binaryoperation._type = self.item_loader(self.item_loader(
            binaryoperation, 'attributes'), 'type')
        parsed_binaryoperation.operator = self.item_loader(self.item_loader(
            binaryoperation, 'attributes'), 'operator')

        # parse childern nodes
        children = self.children_parser(binaryoperation)
        if(self.check_childern(children, parsed_binaryoperation.name)):
            parsed_binaryoperation.identifier_list = self.item_loader(
                children, 'Identifier')
        if(self.check_childern(children, parsed_binaryoperation.name)):
            parsed_binaryoperation.literal_list = self.item_loader(
                children, 'Literal')
        if(self.check_childern(children, parsed_binaryoperation.name)):
            parsed_binaryoperation.binaryoperation_list = self.item_loader(
                children, 'BinaryOperation')
        if(self.check_childern(children, parsed_binaryoperation.name)):
            parsed_binaryoperation.indexaccess_list = self.item_loader(
                children, 'IndexAccess')

        self.log_node_end(
            binaryoperation['name'], parsed_binaryoperation.name, parsed_binaryoperation._id)

        return parsed_binaryoperation

    def parser_tupleexpression(self, tupleexpression):
        '''
        TupleExpression
        '''
        parsed_tupleexpression = TupleExpression()
        parsed_tupleexpression._id = tupleexpression['id']
        # parsed_tupleexpression.name = tupleexpression['attributes']['name']
        parsed_tupleexpression.name = tupleexpression['name']
        self.log_node_begain(
            tupleexpression['name'], parsed_tupleexpression.name, parsed_tupleexpression._id)

        # parse attributes
        parsed_tupleexpression._type = self.item_loader(self.item_loader(
            tupleexpression, 'attributes'), 'type')

        # parse childern nodes
        children = self.children_parser(tupleexpression)
        if(self.check_childern(children, parsed_tupleexpression.name)):
            parsed_tupleexpression.binaryoperation_list = self.item_loader(
                children, 'BinaryOperation')

        self.log_node_end(
            tupleexpression['name'], parsed_tupleexpression.name, parsed_tupleexpression._id)

        return parsed_tupleexpression

    def parser_variabledecsta(self, variabledecsta):
        '''
        VariableDeclarationStatement
        '''
        parsed_variabledecsta = VariableDeclarationStatement()
        parsed_variabledecsta._id = variabledecsta['id']
        # parsed_variabledecsta.name = variabledecsta['attributes']['name']
        parsed_variabledecsta.name = variabledecsta['name']
        self.log_node_begain(
            variabledecsta['name'], parsed_variabledecsta.name, parsed_variabledecsta._id)

        # parse attributes
        parsed_variabledecsta.assignments = self.item_loader(self.item_loader(
            variabledecsta, 'attributes'), 'assignments')

        # parse childern nodes
        children = self.children_parser(variabledecsta)
        if(self.check_childern(children, parsed_variabledecsta.name)):
            parsed_variabledecsta.variable_list = self.item_loader(
                children, 'VariableDeclaration')
        if(self.check_childern(children, parsed_variabledecsta.name)):
            parsed_variabledecsta.literal_list = self.item_loader(
                children, 'Literal')
        if(self.check_childern(children, parsed_variabledecsta.name)):
            parsed_variabledecsta.binaryoperation_list = self.item_loader(
                children, 'BinaryOperation')
        if(self.check_childern(children, parsed_variabledecsta.name)):
            parsed_variabledecsta.membermccess_list = self.item_loader(
                children, 'MemberAccess')

        self.log_node_end(
            variabledecsta['name'], parsed_variabledecsta.name, parsed_variabledecsta._id)

        return parsed_variabledecsta

    def parser_forsta(self, forsta):
        '''
        ForStatement
        '''
        parsed_forsta = ForStatement()
        parsed_forsta._id = forsta['id']
        # parsed_forsta.name = forsta['attributes']['name']
        parsed_forsta.name = forsta['name']
        self.log_node_begain(
            forsta['name'], parsed_forsta.name, parsed_forsta._id)

        # parse attributes
        # **There is no attributes for ForStatement**

        # parse childern nodes
        children = self.children_parser(forsta)
        if(self.check_childern(children, parsed_forsta.name)):
            parsed_forsta.block_list = self.item_loader(
                children, 'Block')

        self.log_node_end(
            forsta['name'], parsed_forsta.name, parsed_forsta._id)

        return parsed_forsta

    def parser_unaryoperation(self, unaryoperation):
        '''
        UnaryOperation
        '''
        parsed_unaryoperation = UnaryOperation()
        parsed_unaryoperation._id = unaryoperation['id']
        # parsed_unaryoperation.name = unaryoperation['attributes']['name']
        parsed_unaryoperation.name = unaryoperation['name']
        self.log_node_begain(
            unaryoperation['name'], parsed_unaryoperation.name, parsed_unaryoperation._id)

        # parse attributes
        parsed_unaryoperation._type = self.item_loader(self.item_loader(
            unaryoperation, 'attributes'), 'type')
        parsed_unaryoperation.operator = self.item_loader(self.item_loader(
            unaryoperation, 'attributes'), 'operator')

        # parse childern nodes
        children = self.children_parser(unaryoperation)
        if(self.check_childern(children, parsed_unaryoperation.name)):
            parsed_unaryoperation.identifier_list = self.item_loader(
                children, 'Identifier')
        if(self.check_childern(children, parsed_unaryoperation.name)):
            parsed_unaryoperation.functioncall_list = self.item_loader(
                children, 'FunctionCall')

        self.log_node_end(
            unaryoperation['name'], parsed_unaryoperation.name, parsed_unaryoperation._id)

        return parsed_unaryoperation

#########################################################
############# Above need to be updating  ################
#########################################################

    def children_parser(self, parent_node):
        '''
        recusive to parse nodes.
        return a list.
        '''
        children=[]
        parsed_children = {}
        try:
            children = parent_node['children']
        except:
            parseLog.warn("[!] There is no child here.")
        for child in children:
            child_type = self.item_loader(child, 'name')
            if not (child_type in parsed_children):
                parsed_children[child_type] = []

            # check wether there is a parser for current child
            try:
                _parser_func = self.parsers[child_type]
            except:
                parseLog.debug(
                    "[!] There is no parsers for {0} now.".format(child_type))
                continue

            parsed_child = _parser_func(child)
            parsed_children[child_type].append(parsed_child)

        return parsed_children

    @staticmethod
    def item_loader(dict, item_name):
        '''
        Get one level item from dictory loading from json.
        The purpose of the function is to add checks for item.
        Sometimes you may choose a non-existent item name and it will log warnning here.
        '''
        try:
            item = dict[item_name]
        except:
            item = None
            parseLog.warn("[!] `{0}` is not found here.".format(item_name))
        return item

    @staticmethod
    def check_childern(children, father):
        if len(children) == 0:
            parseLog.warn("[!] There is no child for {0}.".format(father))
        return len(children)

    def log_node_begain(self, node_type, node_name, node_id):
        '''
        Easy to log the begain info.
        '''
        self.stack_depth += 1
        parseLog.info('[+]'+'--'*self.stack_depth+' Node [{0}, {1}, {2}] Start'.format(
            node_type, node_name, node_id))

    def log_node_end(self, node_type, node_name, node_id):
        '''
        Easy to log the end info.
        '''
        parseLog.info('[-]'+'--'*self.stack_depth+' Node [{0}, {1}, {2}] End'.format(
            node_type, node_name, node_id))
        self.stack_depth -= 1

    def main_parser(self):
        '''
        main parser
        '''
        self.parsed_unit._id = self.ast_json['id']
        self.parsed_unit.name = self.ast_json['attributes']['absolutePath']
        self.log_node_begain(
            self.ast_json['name'], self.parsed_unit.name, self.parsed_unit._id)

        # parse the exportedSymbols
        sym_dict = self.item_loader(self.item_loader(
            self.ast_json, 'attributes'), 'exportedSymbols')
        self.parsed_unit.exportedSymbols = sym_dict

        # parse childern nodes
        children = self.children_parser(self.ast_json)
        if(self.check_childern(children, self.parsed_unit.name)):
            # self.parsed_unit.contract_list = children['ContractDefinition']
            self.parsed_unit.contract_list = self.item_loader(
                children, 'ContractDefinition')

        self.log_node_end(
            self.ast_json['name'], self.parsed_unit.name, self.parsed_unit._id)

    def run(self, ast_filename):
        '''
        run the AstParser
        '''
        parseLog.info('Start up.')
        try:
            self.ast_json = json.load(open(ast_filename, 'r'))
            parseLog.info('Load ast from {0} success.'.format(ast_filename))
        except:
            parseLog.error('Error occurred: {0}'.format(sys.exc_info()[0]))
            exit()

        self.main_parser()

        parseLog.info('Done.')
